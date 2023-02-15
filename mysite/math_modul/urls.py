from django.urls import path
from . import views

urlpatterns=[
    path('', views.calculator, name='calculator'),
    path('graph/', views.graph, name='graph'),
    path('info/', views.InfoCategoryListView.as_view(), name='info'),
    path('info_modul/<int:id>/', views.InfoModulListView.as_view(), name='info_modul'),
]