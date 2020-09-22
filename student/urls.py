from django.contrib import admin
from django.urls import path
from . import views

app_name = "student"

urlpatterns = [
    path('register/',views.register,name = "register"),
    path('login/',views.loginUser,name = "login"),
    path('logout/',views.logoutUser,name = "logout"),
    path('student/<int:id>',views.detail,name = "detail"),
    path('student_list/',views.student_list,name = "student_list"),

]
 