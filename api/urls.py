from django.urls import path
from .import views

urlpatterns = [
    path('products/', views.ProductListCreateAPIView.as_view(), name='products'),
    path('products/info/', views.ProductInfoAPIView.as_view(), name='products-info'),
    path('products/<int:product_id>/', views.ProductDetailAPIView.as_view(), name='product-detail'),
    path('orders/', views.OrderListAPIView.as_view(), name='orders'),
    path('user-orders/', views.UserOrderListAPIView.as_view(), name='user-orders'),
]
