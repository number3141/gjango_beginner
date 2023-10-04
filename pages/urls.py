from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'), 
    # pk = id 
    path('post/<int:pk>/', views.PostDet.as_view(), name = 'post'),
    path('about/', views.AboutView.as_view(), name='about')
]