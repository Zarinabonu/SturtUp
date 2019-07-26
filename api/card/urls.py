from django.urls import path

from api.card.views import CardCreate, CardUpdate , CardDelete

urlpatterns = [
    path('create',CardCreate.as_view(), name ='card-create-api'),
    path('update/<int:id>',CardUpdate.as_view(), name ='card-update-api'),
    path('delete/<int:id>',CardDelete.as_view(), name ='card-api-delete'),
    
]