from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from webapp.forms import ProductForm, ProductReviewForm, ReviewForm
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


class ReviewCreateView(CreateView):
    model = Review
    template_name = "review/create_review.html"
    form_class = ReviewForm

    # Team.objects.create(user=user, project=self.object, start_date=start_date)
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        product_pk = self.kwargs.get('pk')
        print("product_pk", product_pk)
        product = Product.objects.get(pk=product_pk)
        print("Product", product)
        kwargs['product'] = product
        user = self.request.user
        kwargs["user"] = user
        print("user", user)
        # kwargs['user']
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        # form.instance.product =
        return super().form_valid(form)
    #     project_pk = self.request.POST.get('project')
    #     check = self.check(project_pk, self.request.user)
    #     if check:
    #         return super().form_valid(form)
    #     return HttpResponseForbidden("Access is denied")
    #
    # def get_success_url(self):
    #     return reverse("webapp:issue_view", kwargs={"pk": self.object.pk})

    # def dispatch(self, request, *args, **kwargs):
    #     self.user = self.request.user
    #     return super().dispatch(request, *args, **kwargs)

    # def form_valid(self, form):
    #     # self.object = form.save()
    #     pk = self.object.pk
    #     user = self.request.user
    #     # product = self.object
    #     # print("product", product)
    #     print("self.request.user", self.request.user)
    #     print("pk", pk)

        # for user in users:
        #     Team.objects.create(user=user, project=self.object, start_date=start_date)
        # self.add_author_to_review()
        # return redirect('webapp:product_detail', pk)
        # return redirect('webapp:index')

    # def add_author_to_review(self):
    #     user = self.request.user
    #     print("self.request.user", self.request.user)
    #     product = self.object
    #     print("product", product)
        # author = Team.objects.create(user=user, project=project, start_date=start_date)

    def get_success_url(self):
        return reverse("webapp:project_view", kwargs={"pk": self.object.pk})