from django.urls import path
from card_startup import views

urlpatterns = [
    path('list/',views.CardListView.as_view(), name='card-list'),
    path('create/',views.CardCreateView.as_view(), name='card-create'),
    path('update/<int:pk>',views.CardUpdateView.as_view(), name ='update-card'),
    
]
