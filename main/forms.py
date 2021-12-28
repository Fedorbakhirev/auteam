import re

from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from .models import *


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={
        'autocomplete': 'off',
        'placeholder': 'Логин', }))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'autocomplete': 'off',
        'placeholder': 'Пароль', }))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={
        'autocomplete': 'off',
        'placeholder': 'Повторите пароль', }))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={
        'autocomplete': 'off',
        'placeholder': 'Имя', }))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={
        'autocomplete': 'off',
        'placeholder': 'Фамилия', }))
    phone = forms.RegexField(
        regex=r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$',
        widget=forms.TextInput(attrs={'placeholder': 'Номер телефона'}),
        error_messages={'invalid': ('Номер телефона должен быть в формате: +79992345679'), })

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'phone')

    def clean(self):
        username = self.cleaned_data['username']
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        phone = self.cleaned_data['phone']

        if len(username) < 5:
            self.add_error('username', 'Логин должен содержать не менее 5 символов')
        if re.search('\d+', first_name) is not None:
            self.add_error('first_name', 'Имя не может содержать цифры')
        if re.search('\d+', last_name) is not None:
            self.add_error('last_name', 'Фамилия не может содержать цифры')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={
        'autocomplete': 'off',
        'placeholder': 'Логин', }))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'autocomplete': 'off',
        'placeholder': 'Пароль', }))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            return super(LoginUserForm, self).clean()
        else:
            # the authentication system was unable to verify the username and password
            raise ValidationError("Пожалуйста, проверьте правильность написания логина и пароля.")

    class Meta:
        model = User
        fields = ('username', 'password')


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['subject', 'desc']
        widgets = {'user': forms.HiddenInput}


class ContactForm(forms.ModelForm):
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={
        'autocomplete': 'off',
        'placeholder': 'Имя', }))
    desc = forms.CharField(label='Фамилия', widget=forms.Textarea(attrs={
        'autocomplete': 'off',
        'placeholder': 'Сообщение', }))
    phone = forms.RegexField(
        regex=r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$',
        widget=forms.TextInput(attrs={'placeholder': 'Номер телефона'}),
        error_messages={'invalid': ('Номер телефона должен быть в формате: +79992345679'), })

    class Meta:
        model = Contact
        fields = ['name', 'phone', 'desc']

    def clean(self):
        name = self.cleaned_data['name']
        desc = self.cleaned_data['desc']

class RequestForm(forms.ModelForm):
    desc = forms.TextInput()

    class Meta:
        model = TariffHistory
        fields = ('desc',)


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['answer']
