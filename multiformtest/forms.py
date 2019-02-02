from django import forms
from django.forms import formset_factory

class TitleBook(forms.Form):
    BookName = forms.CharField(label='Nombre del Libro', max_length=20)

BookNameFormSet = formset_factory(TitleBook, extra=2, max_num=10)