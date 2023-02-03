from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class BuyerView(TemplateView):
    template_name = "transaction/buyer.html"

    def get(self, *args, **kwargs):
        return render(self.request, "transaction/buyer.html")


class SellerView(TemplateView):
    template_name = "transaction/seller.html"

    def get(self, *args, **kwargs):
        return render(self.request, "transaction/seller.html")