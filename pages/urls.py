from django.urls import path

from pages.views import L1


urlpatterns =[
    path('',L1,name='home'),
    path('<str:section>/',L1,name='section'),

]