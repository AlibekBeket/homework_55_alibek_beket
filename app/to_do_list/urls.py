from django.urls import path

from to_do_list.views.to_do_list import *

urlpatterns = [
    path('', home_view, name='to_do_list'),
    path('to_do/', home_view, name='to_do_list'),
    path('to_do/add/', add_view, name='to_do_add'),
    path('to_do/<int:pk>', detail_view, name='to_do_detail'),
    path('to_do/<int:pk>/update', update_view, name='to_do_update')
]
