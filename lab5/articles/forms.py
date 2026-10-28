from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'text')
        widgets = {'text': forms.Textarea(attrs={'rows': 8})}

    def clean_title(self):
        title = self.cleaned_data['title'].strip()
        titles = Article.objects.values_list('title', flat=True)
        if any(value.casefold() == title.casefold() for value in titles):
            raise forms.ValidationError('Статья с таким названием уже существует.')
        return title
