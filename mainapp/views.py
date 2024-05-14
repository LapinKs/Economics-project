from django.shortcuts import render
from .utils import *
import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json


def get_dollar_rate():
    with urlopen("https://www.cbr.ru/scripts/XML_daily.asp", timeout=10) as r:
        return float((ET.parse(r).findtext('.//Valute[@ID="R01235"]/Value')).replace(',','.'))
def main_page(request):
    return render(request, 'main_page.html', {'content':7})
def gk_page(request):
    return render(request, 'gk.html')
def hk_page(request):
    return render(request, 'hk.html')
def js_page(request):
    return render(request, 'js.html')
def oc_page(request):
    return render(request, 'oc.html')
def pl_page(request):
    return render(request, 'pl.html')
def plitog(request):
    cities_to_reg = get_cities_reg()
    cities_to_prip = get_cities_pripl()
    reg_to_pri ={'1':20,'2':20,'3':5,'4':5,'5':0}
    city = request.GET['city']
    lr = request.GET["rul/list"]
    width = int(request.GET["width"])
    thickness = float(request.GET["thickness"])
    amount = int(request.GET["amount"])
    credit = request.GET["credit"]
    sort = int(request.GET["sort"])
    type_color = request.GET["type_color"]
    dogovor = request.GET["dogovor"]
    clas = request.GET["class"]
    profiles = request.GET["profiles"]
    not_recover = request.GET["not_recover"]

    polimer= get_pol_for_width()[thickness]

    ocink=get_oc_for_width()[thickness]
    dogovor = 1 if dogovor=='on'else 0
    match int(credit):
        case 0:
            credit=0
        case 15:
            credit = 0.5
        case 30:
            credit =1


    lr = 15 if lr == 'l' else 0

    pripl = int(cities_to_prip[city])

    req_pripl=cities_to_reg[city]
    req_pripl =int(reg_to_pri[req_pripl])
    profiles = 50 if profiles=='on' else 0

    type_color = 20 if int(type_color) ==20 else 0

    nac = 25 if 950 < int(width) and int(width) < 999 else 0

    nac2 = 20 if (thickness>0.4)and(width>1100) else 0

    clas = 50 if clas=='on' else 0

    not_recover = 10 if not_recover=='on' else 0

    dollar = get_dollar_rate()

    skidka = 0
    if amount <127:
        skidka = 0
    elif amount <253 and amount>126:
        skidka = 1
    elif amount >252 and amount < 505:
        skidka=1.5
    elif amount >504 and amount < 1009:
        skidka=2
    else:
        skidka=3

    total = - 72167*sort//100 +72167 + float(dollar)*(profiles+type_color+nac+nac2+clas+lr+not_recover+polimer+ocink)
    total = credit*total/100 + total - total*skidka/100 + pripl + req_pripl
    total += total*dogovor/100
    return render(request, 'plitog.html',{"context":round(total*amount,2)})
def ocitog(request):
    cities_to_reg = get_cities_reg()
    cities_to_prip = get_cities_pripl()
    reg_to_pri = {'1': 20, '2': 20, '3': 5, '4': 5, '5': 0}
    city = request.GET['city']
    lr = request.GET["rul/list"]
    width = int(request.GET["width"])
    thickness = float(request.GET["thickness"])
    amount = int(request.GET["amount"])
    credit = request.GET["credit"]
    sort = int(request.GET["sort"])
    dogovor = request.GET["dogovor"]
    profiles = request.GET["profiles"]
    not_recover = request.GET["not_recover"]
    cover = request.GET["cover"]
    nac = 25 if 950 < int(width) and int(width) < 999 else 0
    dogovor = 1 if dogovor == 'on' else 0
    skidka = 0
    if amount < 260:
        skidka = 0
    elif amount < 1040 and amount > 519:
        skidka = 0.5
    elif amount > 1039 and amount < 1501:
        skidka = 1
    elif amount > 1500and amount < 2001:
        skidka = 1.5
    else:
        skidka = 2
    profiles = 50 if profiles == 'on' else 0
    pripl = int(cities_to_prip[city])
    req_pripl = cities_to_reg[city]
    req_pripl = int(reg_to_pri[req_pripl])
    not_recover = 10 if not_recover == 'on' else 0
    match int(credit):
        case 0:
            credit = 0
        case 15:
            credit = 0.5
        case 30:
            credit = 1
    oc_pripl = get_for_ocink()[thickness][cover]
    dollar = get_dollar_rate()
    lr = 15 if lr == 'l' else 0
    total = - 59167 * sort // 100 + 59167 + float(dollar) * (
                profiles + nac + lr + not_recover + oc_pripl)
    total = credit * total / 100 + total - total * skidka / 100 + pripl + req_pripl
    total += total * dogovor / 100
    return render(request, 'ocitog.html',{"context":round(total*amount,2)})
def jsitog(request):
    cities_to_reg =get_cities_reg()
    cities_to_prip = get_cities_pripl()
    city = request.GET['city']
    lr = request.GET["rul/list"]
    class_of_width = request.GET["class_of_width"]
    width = int(request.GET["width"])
    thickness = float(request.GET["thickness"])
    amount = int(request.GET["amount"])
    credit = request.GET["credit"]
    match int(credit):
        case 0:
            credit = 0
        case 15:
            credit = 0.5
        case 30:
            credit = 1
    pripl = int(cities_to_prip[city])
    reg = int(cities_to_reg[city])
    region = cities_to_reg[city]
    jest_pripl = get_for_jest()[float(thickness)][class_of_width]

    lr = 4 if lr == 'l' else 0

    skidka = 0
    if amount < 251:
        skidka = 0
    elif amount < 500 and amount > 250:
        skidka = 1
    elif amount > 499 and amount < 1000:
        skidka = 2
    elif amount > 999 and amount < 1501:
        skidka = 3
    else:
        skidka = 4
    dollar = get_dollar_rate()
    width_pripl=0
    match width:
        case 17:
            width_pripl=85
        case 18:
            width_pripl=50
        case 19:
            width_pripl=35
        case 20:
            width_pripl=10
        case 21:
            width_pripl=10
        case 22:
            width_pripl=5
        case 23:
            width_pripl = 5
        case 24:
            width_pripl = 5
    skidka_proc=0
    skidka2=0
    shabolda=0
    if lr !=4:
        skidka_proc=4
    elif width not in [712,724,765,820,836,865,910]:
        skidka_proc=2
    elif width in [704,724,836] and amount >240:
        jest_pripl=0
    elif region==1:
        skidka_proc=2
    elif int(class_of_width)==2:
        skidka2=500
    elif int(class_of_width)==5:
        skidka2=300
    else:
        shabolda=1
    total = 80800
    total = total - total*skidka/100
    total += (jest_pripl+width_pripl)*dollar
    total = total - skidka_proc*total/100 -skidka2*dollar + pripl
    total = total + credit*total/100
    return render(request, 'jsitog.html',{"context":round(total*amount,2)})
def gkitog(request):
    cities_to_reg = get_cities_reg()
    cities_to_prip = get_cities_pripl()
    city = request.GET['city']
    lr = request.GET["rul/list"]
    width = int(request.GET["width"])
    thickness = float(request.GET["thickness"])
    amount = int(request.GET["amount"])
    credit = request.GET["credit"]
    sort = int(request.GET["sort"])
    shtrips = request.GET["shtrips"]
    cromka = request.GET["cromka"]
    rifl = request.GET["rifl"]
    mark = int(request.GET["mark"])
    cromka = 15 if cromka=='on' else 0
    shtrips = 60 if shtrips=='on' else 0
    rifl = 25 if (rifl=='on'and (thickness>=4 and thickness <=12)) else 0
    acces = 10 if (width>859 and width<1501) and lr=='r' else 0
    skidka = 0
    pripl = int(cities_to_prip[city])
    if amount<500:
        skidka=2
    elif amount>499 and amount<1001:
        skidka = 1
    else:
        skidka = 0
    match int(credit):
        case 0:
            credit = 0
        case 15:
            credit = 0.5
        case 30:
            credit = 1
    ves1 = 5 if (lr=='l' and amount < 6) else 0
    ves2 = 15 if (lr == 'r' and amount<10) else 0
    ves3 = 10 if (width <1000) else 0
    tolerance = 0 if (width>859 and width<1500) else 10
    lr = 1 if lr=='l' else 2
    gk_pripl=0
    if width>1.19 and width < 1.25:
        gk_pripl = 115
    elif width>1.24 and width < 1.30:
        gk_pripl = 110
    elif width>1.29 and width < 1.35:
        gk_pripl = 105
    elif width>1.34 and width < 1.4:
        gk_pripl = 95
    elif width>1.39and width < 1.5:
        gk_pripl = 75
    elif width>1.49 and width < 1.6:
        gk_pripl = 50
    elif width>1.59 and width < 1.8:
        gk_pripl = 40
    elif width>1.79 and width < 2:
        gk_pripl = 25
    elif width>1.99 and width < 2.5:
        gk_pripl = 10
    elif width>4 and width < 12:
        gk_pripl = -5
    else:
        gk_pripl=0
    base = int(get_hot()[int(cities_to_reg[city])][str(lr)])
    dollar = get_dollar_rate()
    total = base - sort*base/100 + dollar*(gk_pripl+acces+rifl+shtrips+cromka+ves1+ves2+mark+ves3+tolerance)+ pripl
    total = total + skidka*total/100
    total = total + total*credit/100
    return render(request, 'gkitog.html',{"context":round(total*amount,2)})
def hkitog(request):
    cities_to_reg = get_cities_reg()
    cities_to_prip = get_cities_pripl()
    city = request.GET['city']
    lr = request.GET["rul/list"]
    width = int(request.GET["width"])
    thickness = float(request.GET["thickness"])
    amount = int(request.GET["amount"])
    credit = request.GET["credit"]
    sort = int(request.GET["sort"])
    mark = int(request.GET["mark"])

    ves1 = 5 if (lr == 'l' and amount < 6) else 0
    ves2 = 15 if (lr == 'r' and amount < 10) else 0
    ves3 = 10 if (width < 1000) else 0
    dollar = get_dollar_rate()
    lr = 1 if lr == 'l' else 2
    pripl = int(cities_to_prip[city])
    base = int(get_cold()[int(cities_to_reg[city])][str(lr)])
    match int(credit):
        case 0:
            credit = 0
        case 15:
            credit = 0.5
        case 30:
            credit = 1
    skidka = 0
    if amount<121:
        skidka=2
    elif amount>120and amount<500:
        skidka = 1
    elif amount > 501 and amount < 750:
        skidka = 0
    else:
        skidka = 0

    thickness_plus=0
    if thickness>=0.3 and thickness<=0.34:
        thickness_plus=65
    elif thickness>=0.35 and thickness<=0.39:
        thickness_plus = 50
    elif thickness>=0.4 and thickness<=0.49:
        thickness_plus = 40
    elif thickness>=0.5 and thickness<=0.59:
        thickness_plus = 30
    elif thickness>=0.6 and thickness<=0.69:
        thickness_plus = 6
    elif thickness>=1 and thickness<=1.49:
        thickness_plus = -3
    elif thickness>=1.5 and thickness<=1.69:
        thickness_plus = -5
    elif thickness>=1.7 and thickness<=2:
        thickness_plus = -8
    elif thickness>=2.01 and thickness<=3.9:
        thickness_plus = 20
    else:
        thickness_plus = 0
    tolerance = 0 if (width>899 and width<1251) else 10
    total= base - base*sort/100
    total = total + dollar*(tolerance+thickness_plus+ves1+ves2+ves3+mark)+ pripl
    total = total + total*skidka/100
    total = total + total*credit/100
    return render(request, 'hkitog.html',{"context":round(total*amount,2)})
