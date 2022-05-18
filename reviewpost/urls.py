from django.urls import path
from .views import signupview, loginview, listview, CreateClass, logoutview, playview

urlpatterns = [
    path('signup/', signupview, name='signup'),
    path('login/', loginview, name='login'),
    path('list/', listview, name='list'),
    path('create/', CreateClass.as_view(), name='create'),
    path('logout/', logoutview, name='logout'),
    path('play/', playview, name='play'),
]
