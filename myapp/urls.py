from myapp import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns= [
    path('', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('newTask', views.newTask, name='newTask'),
    path('projects', views.recordProject, name='recordProject'),
    path('logout/', views.logout_view, name='logout'),
    path('delete/<str:task_id>/', views.deleteTask, name='delete_task'),
    path('download', views.export, name='export'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)