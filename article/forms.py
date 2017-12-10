from django import forms
from .models import Article, ArticleCategory

class ArticleForm(forms.ModelForm):

    category = forms.ModelChoiceField(
        ArticleCategory.objects.order_by('title'),
        empty_label='Select',
        required=False,
        help_text='Choose article category',
        )
    image = forms.FileField(required=False)
    class Meta:
        model = Article
        fields = ['title', 'body', 'category', 'image']
        help_texts = {
            'title': 'Article name',
            'body': 'Enter article body here'}

'''def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Select'

'''

class ArticleCategoryForm(forms.ModelForm):

    title = forms.CharField(
        label='Add category',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category name'}))

    class Meta:
        model = ArticleCategory
        fields = ['title']
