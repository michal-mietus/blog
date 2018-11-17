from django import forms
from .models import Article


class AddArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['author', 'pub_date']
