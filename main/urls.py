from django.urls import path
from .views import *
urlpatterns = [
    path('', HomePageView.as_view(), name='homePage'),
    path('products-list/', ProductListView.as_view(), name='productsList'),
    path('product-detail/', ProductDetailView.as_view(), name='productDetail'),
    path('cart/', CartPageView.as_view(), name='cartPage'),
]
