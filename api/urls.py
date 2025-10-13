from django.urls import path
from .import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('products/',
         views.ProductListCreateAPIView.as_view(),
         name='products'),
    path('products/info/',
         views.ProductInfoAPIView.as_view(),
         name='products-info'),
    path('products/<int:product_id>/',
         views.ProductDetailAPIView.as_view(),
         name='product-detail'),
]

router = DefaultRouter()
router.register('orders', views.OrderViewSet)
urlpatterns += router.urls
