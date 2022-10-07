from django.urls import path

from app import views

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path('store/search/', views.search, name='search'),
    path('store/category/<int:category_id>/', views.category, name='category'),
    path('store/brand/<int:brand_id>/', views.brand, name='brand'),
    path('store/<int:id>/', views.item, name='item'),
]
