from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('departamento/<int:departamento_id>', views.detail, name = 'detail')
]
