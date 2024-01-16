from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('client_list/', views.client_list, name="client_list"),
    path('client_form/', views.client_form, name="client_form"),
    path('instrument_list/', views.instrument_list, name="instrument_list"),
    path('instrument_form/', views.instrument_form, name="instrument_form"),
    path('type_instrument_list/', views.type_instrument_list, name="type_instrument_list"),
    path('type_instrument_form/', views.type_instrument_form, name="type_instrument_form"),

]