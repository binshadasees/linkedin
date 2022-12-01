from django.urls import path
from . import views
app_name='play'
urlpatterns = [
    path('index', views.index,name='index'),
    path('home', views.home,name='home'),
    path('post_job', views.post_job,name='post_job'),
    path('join_now',views.join_now),
    path('find',views.find)
]