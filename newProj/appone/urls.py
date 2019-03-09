from django.urls import path
from appone import views 

urlpatterns = [
	path('',views.users,name='users')
]