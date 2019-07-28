from django.urls import path
from register_startup import views

urlpatterns = [
    path('list/',views.RegisterCreateList.as_view(), name ='register-list'),
    path('create/',views.RegisterCreateView.as_view(),  name ='register-create'),
    path('update/<int:pk>' ,views.RegisterUpdateView.as_view(), name='regiser-update' ),
    # path('email/',views.index, name ='register-email'),
]