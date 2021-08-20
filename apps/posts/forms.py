from django import forms
from .models import Posts, Category


class PostForm(forms.ModelForm):

    class Meta:
        model = Posts
        fields = ('title', 'body', 'image', 'category')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.URLInput(attrs={'class': 'form-control'}),
            'category': forms.Select(),

    }


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
