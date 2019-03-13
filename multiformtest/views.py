from django.shortcuts import render
from django.views import View
from .forms import TitleBook

# Create your views here.
from django.views import generic
from .forms import BookNameFormSet, RuleBasesForm, RuleBaseFormSet
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


class r80apitest(View):
    template_name = 'multiformtest/form2.html'
    tcpObjects = [['80', '80'], ['443', '443'], ['22', '22'], ['21', '21'], ['25', '25']]
    udpObjects = [['53', '53'], ['65', '65'], ['34', '34'], ['56', '56']]
    hostObjects = [['1.1.1.1', '1.1.1.1'], ['2.2.2.2', '2.2.2.2'], ['3.3.3.3', '3.3.3.3']]
    networkObjects = [['1.1.1.1', '1.1.1.1'], ['2.2.2.2', '2.2.2.2'], ['3.3.3.3', '3.3.3.3']]
    form_class = RuleBaseFormSet

    def get(self, request, *args, **kwargs):
        formset = RuleBaseFormSet(form_kwargs={'tcplist': self.tcpObjects, 'udplist': self.udpObjects, 'hostlists': self.hostObjects,
                                               'networks': self.networkObjects})
        #return render(request, self.template_name, {'rulesform': self.form_class(self.tcpObjects, self.udpObjects,self.hostObjects, self.networkObjects)})
        return render(request, self.template_name, {'rulesform': self.form_class(form_kwargs={'tcplist': self.tcpObjects, 'udplist': self.udpObjects, 'hostlists': self.hostObjects,
                     'networks': self.networkObjects})})


    def post(self, request, *args, **kwargs):
        print(request.POST)
        form = self.form_class(data=request.POST, form_kwargs={'tcplist': self.tcpObjects, 'udplist': self.udpObjects, 'hostlists': self.hostObjects,
                     'networks': self.networkObjects})
        if form.is_valid():
            print("Es valida")
        else:
            print("No es valida")
            SuspiciousOperation("Invalid request: not able to process the form")
        return render(request, self.template_name, {'rulesform': self.form_class(
            form_kwargs={'tcplist': self.tcpObjects, 'udplist': self.udpObjects, 'hostlists': self.hostObjects,
                         'networks': self.networkObjects})})