from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProductForm
from webapp.models import Product, Review


class IndexView(ListView):
    model = Product
    template_name = 'products/index.html'

    def get_queryset(self):
        return Product.objects.all()


class ProductDetailView(DetailView):
    template_name = "products/product.html"
    context_object_name = "product"
    model = Product


class ProductCreateView(CreateView):
    model = Product
    template_name = "products/create_product.html"
    form_class = ProductForm

    def get_success_url(self):
        return reverse("webapp:product_detail", kwargs={"pk": self.object.pk})


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "products/update_product.html"
    context_object_name = "product"

    def get_success_url(self):
        return reverse("webapp:product_detail", kwargs={"pk": self.object.pk})


class ProductDeleteView(DeleteView):
    form_class = ProductForm
    template_name = "issue/delete_product.html"
    model = Product
    success_url = reverse_lazy("webapp:index")
    context_object_name = "product"
