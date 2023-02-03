from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class CartView(TemplateView):
    template_name = "cart/cart-page.html"

    def get(self, *args, **kwargs):
        return render(self.request, "cart/cart-page.html")


class DetailView(TemplateView):
    template_name = "cart/cart-detail-page.html"

    def get(self, *args, **kwargs):
        return render(self.request, "cart/cart-detail-page.html")