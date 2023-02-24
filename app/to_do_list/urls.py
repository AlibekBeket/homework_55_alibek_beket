from django.urls import path

from to_do_list.views.to_do_list import *

urlpatterns = [
    path('', home_view, name='to_do_list'),
    path('to_do/', home_view, name='to_do_list'),
    path('to_do/add/', add_view, name='to_do_add'),
    path('to_do/<int:pk>', detail_view, name='to_do_detail'),
    path('to_do/<int:pk>/update', update_view, name='to_do_update'),
    path('to_do/<int:pk>/delete', delete_view, name='to_do_delete'),
    path('to_do/<int:pk>/confirm_delete', confirm_delete, name='confirm_delete')
]
