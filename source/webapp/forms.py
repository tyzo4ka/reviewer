from django import forms
from django.core.exceptions import ValidationError

from webapp.models import Product, Review, User


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "category", "description", "picture"]


class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["text", "grade"]


class ReviewForm(forms.ModelForm):
    #
    # def __init__(self, user, product, **kwargs):
    #     # self.user = kwargs.pop('user')
    #     # print("Self user", self.user)
    #     super().__init__(**kwargs)
    #     grade = self.fields['grade']
    #     print(grade, "GRADE")
    #     # grade = self.fields['grade'].queryset = User.objects.filter(teams__project__in=self.projects)
    #
    #     # self.user = user
    #     if user and not user.is_authenticated:
    #         self.user = None
    #     super().__init__(**kwargs)

    # def clean_grade(self):
    #     if self.grade not in range(1, 6):
    #         raise ValidationError('You grade must be from 1 to 5')
    #     return self.cleaned_data.get('grade')

    class Meta:
        model = Review
        fields = ['text', 'grade']
