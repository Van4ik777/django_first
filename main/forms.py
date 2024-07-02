from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import forms, TextInput, PasswordInput, CharField, EmailField, EmailInput, ModelForm, ChoiceField, \
    Textarea, RadioSelect, HiddenInput
from .models import Review


class ReviewForm(ModelForm):
    '''
    форма для коментарів, де можна вибрати від 1 до 5 зірок на написати текст
    '''

    RATING_CHOICES = [(i, f'Star {i}') for i in range(1, 6)]
    stars = ChoiceField(choices=RATING_CHOICES, widget=RadioSelect(), label='Stars')
    content = CharField(widget=Textarea(attrs={'rows': 5}), label='Content')

    class Meta:
        model = Review
        fields = ['content', 'stars']




class RegisterUserForm(UserCreationForm):
    '''
    Форма регестрації юзера
    '''
    username = CharField(label='Username', widget=TextInput(attrs={'class': 'form-input'}))
    email = EmailField(label='Email', widget=EmailInput(attrs={'class': 'form-input'}))
    password1 = CharField(label='Password', widget=PasswordInput(attrs={'class': 'form-input'}))
    password2 = CharField(label='Repeat password', widget=PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



class OrderForm(forms.Form):
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Наличные'),
        ('online', 'Онлайн'),
    ]
    
    DELIVERY_TIME_CHOICES = [
        ('now', 'Сейчас'),
        ('scheduled', 'На время'),
    ]

    name = CharField(max_length=100, label='Имя')
    phone = CharField(max_length=20, label='Телефон')
    city = CharField(max_length=100, label='Город')
    house_number = CharField(max_length=10, label='Номер дома')
    apartment_number = CharField(max_length=10, label='Номер квартиры')
    payment_method = ChoiceField(choices=PAYMENT_METHOD_CHOICES, label='Способ оплаты')
    delivery_time = ChoiceField(choices=DELIVERY_TIME_CHOICES, label='Когда доставлять')
    delivery_time_details = CharField(max_length=100, required=False, label='Время доставки', help_text='Укажите время, если выбрали "На время"')

    def clean(self):
        cleaned_data = super().clean()
        delivery_time = cleaned_data.get('delivery_time')
        delivery_time_details = cleaned_data.get('delivery_time_details')

        if delivery_time == 'scheduled' and not delivery_time_details:
            self.add_error('delivery_time_details', 'Укажите время доставки, если выбрали "На время".')
        return cleaned_data