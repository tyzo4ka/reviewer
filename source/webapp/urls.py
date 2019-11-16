from django.urls import path
from .views import IndexView, ProductDetailView, ProductCreateView, ProductUpdateView
# ProductView, ProductCreateView, BasketChangeView, BasketView,\
#     ProductUpdateView, ProductDeleteView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    # path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete')
]
