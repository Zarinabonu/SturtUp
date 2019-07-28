from django.urls import path
from banner_startup import views

urlpatterns = [
    path('list/',views.BannerListView.as_view(), name ='banner-list'),
    path('create/', views.BannerCreteView.as_view(), name ='banner-create'),
    path('update/<int:pk>', views.BannerUpdateView.as_view(), name ='banner-update'),
    
]