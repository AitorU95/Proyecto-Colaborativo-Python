from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.show_form, name='registro'),
    path('mostrardatos/', views.post_form, name='mostrardatos')

]
