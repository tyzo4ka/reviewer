from django import forms
from webapp.models import Product, Review, User


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "category", "description", "picture"]
