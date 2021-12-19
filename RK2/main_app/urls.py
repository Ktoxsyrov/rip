from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('manufacturer', views.manufacturer_list),
    path('manufacturer/create', views.ManufacturerCreate.as_view()),
    path('manufacturer/<int:id_man>/update', views.ManufacturerUpdate.as_view(), name='man_update'),
    path('manufacturer/<int:id_man>/delete', views.ManufacturerDelete.as_view(), name='man_delete'),
    path('detail', views.detail_list),
    path('detail/create', views.DetailCreate.as_view()),
    path('detail/<int:id_det>/update', views.DetailUpdate.as_view(), name='det_update'),
    path('detail/<int:id_det>/delete', views.DetailDelete.as_view(), name='det_delete'),
    path('report', views.report)
]