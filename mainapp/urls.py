from django.urls import path
from .views import *
urlpatterns = [
    path('', main_page, name = 'page'),
    path('gk/', gk_page, name='gk'),
    path('hk/', hk_page, name='hk'),
    path('js/', js_page, name='js'),
    path('oc/', oc_page, name='oc'),
    path('pl/', pl_page, name='pl'),
    path('plitog/', plitog, name='plitog'),
    path('ocitog/', ocitog, name='ocitog'),
    path('jsitog/', jsitog, name='jsitog'),
    path('gkitog/', gkitog, name='gkitog'),
    path('hkitog/', hkitog, name='hkitog'),
]