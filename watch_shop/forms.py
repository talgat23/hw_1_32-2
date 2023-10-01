from django import forms
from . import models


class ShopForm(forms.ModelForm):
    class Meta:
        model = models.Shop
        fields = '__all__'


class WatchesReviewForm(forms.ModelForm):
    class Meta:
        model = models.Reviews
        fields = '__all__'


class DeleteWatchesReview(forms.ModelForm):

    class Meta:
        model = models.Reviews
        fields = '__all__'
