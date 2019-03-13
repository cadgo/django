from django import forms
from django.forms import formset_factory

class TitleBook(forms.Form):
    BookName = forms.CharField(label='Nombre del Libro', max_length=20)
    Aditional = forms.CharField(label='Aditional', max_length=20)

BookNameFormSet = formset_factory(TitleBook, min_num=1,extra=0, max_num=10)


class RuleBasesForm(forms.Form):
    ActionChoice = (('Accept', 'Accept'), ('Drop', 'Drop'),)
    LogChoice = (('Log', 'Log'), ('Full Log', 'Full Log'),('Network Log', 'Network Log'), ('None', 'None'),)
    RuleName = forms.CharField(label='Rule Name',max_length=20, strip=True,
                               widget = forms.TextInput(attrs={'class': 'form-control',
                                                               'placeholder': 'RuleName'}))
    FWRuleOrigin = forms.ChoiceField(label='Src IP')
    FwRuleDst = forms.ChoiceField(label='Dst IP')
    #FWRulePort = forms.IntegerField(min_value=1, max_value=65525)
    FWRulePort = forms.ChoiceField(label='Port')
    ActionRule = forms.ChoiceField(label='Action', choices=ActionChoice)
    LogRule = forms.ChoiceField(label='Log', choices = LogChoice)
    #UsersFormChoice = forms.ChoiceField(label='Users', choices=UsersQuery)
    #MgmtFormChoice = forms.ChoiceField(label='SMSServer', choices=MgmtQuery)

    def __init__(self, tcplist, udplist, hostlists, networks, *args, **kwargs):
        #Validar que las listas vengan con información que no esten en cero
        super().__init__(*args, **kwargs)
        self.fields['FWRulePort'].choices = tcplist + udplist
        if hostlists == None:
            self.fields['FWRuleOrigin'].choices = networks
            self.fields['FwRuleDst'].choices = networks
        elif networks == None:
            self.fields['FWRuleOrigin'].choices = hostlists
            self.fields['FwRuleDst'].choices = hostlists
        else:
            self.fields['FWRuleOrigin'].choices = hostlists + networks
            self.fields['FwRuleDst'].choices = hostlists + networks


RuleBaseFormSet = formset_factory(RuleBasesForm, min_num=2,extra=0, max_num=10)