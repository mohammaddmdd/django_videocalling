from django.urls import path
from agora import views

urlpatterns = [
    # Other URL patterns in your app
    path('', views.index, name='agora_rtm_index'),
    path('users/', views.fetch_users, name='agora_rtm_fetch_users'),
    path('agora-rtm/token/', views.generate_agora_token, name='agora_rtm_generate_token'),
]
