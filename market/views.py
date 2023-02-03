from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class DashboardView(TemplateView):
    template_name = "market/dashboard.html"

    def get(self, *args, **kwargs):
        return render(self.request, "market/dashboard.html")


class DetailView(TemplateView):
    template_name = "market/product-detail.html"

    def get(self, *args, **kwargs):
        return render(self.request, "market/product-detail.html")


class WishlistView(TemplateView):
    template_name = "market/wishlist-page.html"

    def get(self, *args, **kwargs):
        return render(self.request, "market/wishlist-page.html")