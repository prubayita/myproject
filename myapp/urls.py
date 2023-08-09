from myapp import views
from django.urls import path


urlpatterns= [
    path('', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('newTask', views.newTask, name='newTask'),
    path('projects', views.recordProject, name='recordProject'),
    path('logout/', views.logout_view, name='logout'),

]
