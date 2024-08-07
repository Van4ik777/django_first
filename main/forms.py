from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import forms, TextInput, PasswordInput, CharField, EmailField, EmailInput, ModelForm, ChoiceField, \
    Textarea, RadioSelect
from .models import Review


class ReviewForm(ModelForm):
    RATING_CHOICES = [(i, f'Star {i}') for i in range(1, 6)]
    stars = ChoiceField(choices=RATING_CHOICES, widget=RadioSelect(), label='Stars')
    content = CharField(widget=Textarea(attrs={'rows': 5}), label='Content')

    class Meta:
        model = Review
        fields = ['content', 'stars']


class RegisterUserForm(UserCreationForm):
    username = CharField(label='Username', widget=TextInput(attrs={'class': 'form-input'}))
    email = EmailField(label='Email', widget=EmailInput(attrs={'class': 'form-input'}))
    password1 = CharField(label='Password', widget=PasswordInput(attrs={'class': 'form-input'}))
    password2 = CharField(label='Repeat password', widget=PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
