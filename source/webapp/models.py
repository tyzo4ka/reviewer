from django.db import models
from django.contrib.auth.models import User


CATEGORY_CHOICES = (
    ('other', 'Other'),
    ('food', 'Food'),
    ('clothes', 'Clothes'),
    ('households', 'Households'),
)

# DEFAULT_PRODUCT_IMAGE = "/uploads/products_image/default_image.png"


class Product(models.Model):
    DEFAULT_PRODUCT_IMAGE = "/uploads/products_image/default_image.png"

    name = models.CharField(max_length=200, null=False, blank=False, verbose_name="Product")
    category = models.CharField(max_length=50, null=False, blank=False, choices=CATEGORY_CHOICES, default=CATEGORY_CHOICES[0][0], verbose_name="Category")
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name="Description")
    picture = models.ImageField(upload_to="products_images", null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    author = models.ForeignKey(User, related_name="review", on_delete=models.CASCADE, verbose_name='User')
    product = models.ForeignKey("webapp.Product", related_name='review', on_delete=models.CASCADE, verbose_name="Product")
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name="Review")
    grade = models.IntegerField(null=False, blank=False, verbose_name="Grade")

    def __str__(self):
        return f"{self.author} / {self.product}"


