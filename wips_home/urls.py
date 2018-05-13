from django.urls import path
from wips_home import views

urlpatterns = [
    path('', views.block_list, name='block_list'),
    path('post/<int:pk>', views.block_list_post, name='block_list_post'),
    #path('edit/',views.edit_data, name='edit_data')
]