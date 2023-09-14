from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    
    path('', views.main,name="index"),
    path("get_live_counter/<int:pk>",views.get_count_ajax,name="get_ajax"),
    path("card_detail/<int:pk>",views.card_detail,name="card-detail"),
    path("create_html",views.create,name="create")
]
