from django.db import models

CATEGORY_CHOICES = (
    ('other', 'Other'),
    ('food', 'Food'),
    ('clothes', 'Clothes'),
    ('households', 'Households'),
)


class Product(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name="Product")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default=CATEGORY_CHOICES[0][0], verbose_name="Category")
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name="Description")
    picture = models.ImageField(upload_to="product_images", null=True, blank=True)

