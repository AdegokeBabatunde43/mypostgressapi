from django.urls import path
from pages import views

urlpatterns = [
    path('createtodo', views.createtodo, name='createtodo'),
    path('alltodo', views.alltodo, name='alltodo'),
    path('detailtodo/<int:id>', views.detailtodo, name='detailtodo'),
    path('edittodo/<int:id>', views.edittodo, name='edittodo'),
    path('deletetodo/<int:id>', views.deletetodo, name='deletetodo'),
]