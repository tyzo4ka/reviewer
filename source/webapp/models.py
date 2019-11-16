from django.db import models
from django.contrib.auth.models import User


CATEGORY_CHOICES = (
    ('other', 'Other'),
    ('food', 'Food'),
    ('clothes', 'Clothes'),
    ('households', 'Households'),
)


class Product(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name="Product")
    category = models.CharField(max_length=50, null=False, blank=False, choices=CATEGORY_CHOICES, default=CATEGORY_CHOICES[0][0], verbose_name="Category")
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name="Description")
    picture = models.ImageField(upload_to="product_images", null=True, blank=True)


class Review(models.Model):
    author = models.ForeignKey(User, related_name="review", on_delete=models.CASCADE, verbose_name='User')
    product = models.ForeignKey("webapp.Product", related_name='review', on_delete=models.CASCADE, verbose_name="Product")
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name="Review")
    grade = models.IntegerField(null=False, blank=False, verbose_name="Grade")

