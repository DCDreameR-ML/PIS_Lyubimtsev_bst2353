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


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Email', required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data['username'].strip()
        names = User.objects.values_list('username', flat=True)
        if any(value.casefold() == username.casefold() for value in names):
            raise forms.ValidationError('Этот логин уже занят.')
        return username
