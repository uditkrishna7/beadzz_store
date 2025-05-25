from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page view
    path('product/<int:id>/', views.product_detail, name='product_detail'),  # Detail page
]
