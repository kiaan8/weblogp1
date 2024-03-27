from django.urls import path

import blog.views
from . import views
from django.conf.urls import handler404




urlpatterns = [
    path('', views.post, name='posts_list'),
    path('<int:pk>',views.post_detil_view, name='posts_detail'),
    path('add/',views.post_add_view, name='post_create'),
    path('<int:pk>/update/',views.post_update_view, name='post_update'),
    path('<int:pk>/delete/ ',views.post_delete_view, name='post_delete')



]