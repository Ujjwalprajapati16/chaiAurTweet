from django import forms
from .models import Tweet, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'bg-black text- p-2 rounded',
                'placeholder': 'What\'s happening?',
                'rows': 4,
            }),
            'photo': forms.ClearableFileInput(attrs={
                'class': 'bg-black text-white p-2 rounded',
            }),
        }

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'bg-white dark:bg-gray-800 text-black dark:text-white p-2 rounded',
        'placeholder': 'Email',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'bg-white dark:bg-gray-800 text-black dark:text-white p-2 rounded',
        'placeholder': 'Password',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'bg-white dark:bg-gray-800 text-black dark:text-white p-2 rounded',
        'placeholder': 'Confirm Password',
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'bg-black dark:bg-gray-800 text-black dark:text-white p-2 rounded',
                'placeholder': 'Username',
            }),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']