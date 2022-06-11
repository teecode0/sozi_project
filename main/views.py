from django.shortcuts import render
from django.views import View
# Create your views here.

class HomePageView(View):
    def get(self, request):
        return render(request, 'main/home.html')

class ProductListView(View):
    def get(self, request):
        return render(request, 'main/products-list.html')

class ProductDetailView(View):
    def get(self, request):
        return render(request, 'main/product-detail.html')

class CartPageView(View):
    def get(self, request):
        return render(request, 'main/cart.html')
