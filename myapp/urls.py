from django.urls import path
from myapp import views
from django.urls import include

app_name = 'techavant'
urlpatterns = [
 path(r'', views.index, name='index'),
 path(r'login/', views.user_login, name='login'),
 path(r'adminlogin/', views.admin_login, name='adminlogin'),
 path(r'empdet/', views.empdet, name='empdet'),
 path(r'admindet/', views.admindet, name='admindet'),
 path(r'adminedit/<int:id>', views.adminedit, name='admin_edit'),

 path(r'test', views.test, name='test'),

]