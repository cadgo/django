from django import forms
from django.forms import formset_factory

class TitleBook(forms.Form):
    BookName = forms.CharField(label='Nombre del Libro', max_length=20)
    Aditional = forms.CharField(label='Aditional', max_length=20)

BookNameFormSet = formset_factory(TitleBook, min_num=1,extra=0, max_num=10)