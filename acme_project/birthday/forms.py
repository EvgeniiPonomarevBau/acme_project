from django import forms
from .models import Birthday


class BirthdayForm(forms.ModelForm):
    class Meta:
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }
        # Указываем модель, на основе которой должна строиться форма.
        model = Birthday
        # Указываем, что надо отобразить все поля.
        fields = '__all__' 