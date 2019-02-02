from django.shortcuts import render
from django.views import View
from .forms import TitleBook

# Create your views here.
from django.views import generic
from .forms import BookNameFormSet
#class form1test(generic.TemplateView):
#    template_name = 'multiformtest/form1.html'

class form1test(View):
    template_name = 'multiformtest/form1.html'
    form_class = BookNameFormSet

    def get(self, request):
        print(request.GET)
        form = self.form_class(request.GET)
        print(form.is_bound)
        return render(request, self.template_name, {'formset': self.form_class()})

    def post(self, request):
        print(request.POST)
        form = self.form_class(request.POST)
        if form.is_valid():
            print('es valida')
            return render(request, self.template_name, {'form': self.form_class()})
        return render(request, self.template_name, {'form': self.form_class()})