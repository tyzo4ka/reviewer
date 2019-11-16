from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from webapp.forms import ProductForm, ProductReviewForm
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object
        context["form"] = ProductReviewForm
        reviews = product.review.order_by('-pk')
        context['reviews'] = reviews
        # reviews = context['product'].reviews.order_by("-created_date")
        # print("Reviews", reviews)
        self.paginate_reviews_to_context(reviews, context)
        # pk = self.kwargs.get('pk')
        # print("Pk", pk)
        return context


    def paginate_reviews_to_context(self, reviews, context):
        paginator = Paginator(reviews, 5, 0)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        context['paginator'] = paginator
        context['page_obj'] = page
        context['issues'] = page.object_list
        context['is_paginated'] = page.has_other_pages()


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
    template_name = "products/delete_product.html"
    model = Product
    success_url = reverse_lazy("webapp:index")
    context_object_name = "product"


# class IndexView(ListView):
#     model = Product
#     template_name = 'products/index.html'
#
#     def get_queryset(self):
#         return Product.objects.all()