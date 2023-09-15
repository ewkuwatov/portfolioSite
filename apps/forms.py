from django import forms
from .models import Testimonial, Team, Price, Contact
from django.forms import ModelForm, TextInput, Textarea

class TestimonialForm(ModelForm):
    class Meta:
        model = Testimonial
        fields = ["name", "description", "position"]
        widgets = {
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите свой отзыв',
        }),
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите свое имя',
        }),
            "position": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Должность'
        })}

class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ["name", "position", "urls_facebook", "urls_telegram", "urls_linkedin", "urls_instagram",]

class PriceForm(ModelForm):
    class Meta:
        model = Price
        fields = ["package_name", "package_price",]

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'number', 'comments']
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя',
        }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
        }),
            "number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер'

        }),
            "comments": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Коментарии'
        })}



