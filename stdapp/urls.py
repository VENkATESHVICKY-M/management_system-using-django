from django.urls import path,include
from . import views
urlpatterns = [

    path('', views.base, name="base"),
    path('new/', views.new, name="new"),
    path('update/<int:i>/', views.update, name="update"),
    path('delete/<int:i>/', views.delete, name="delete")

]