from django import forms
from .models import Emp
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator, MaxLengthValidator

class EmpForm(forms.ModelForm):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    ]
    
    emp_no = forms.IntegerField(required=True)
    emp_name = forms.CharField(max_length=30, required=True)
    sex = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select)
    pin = forms.IntegerField(max_value = 100000000)
    
    ph_no = forms.IntegerField(max_value=10000000000)
    
    basic = forms.IntegerField(max_value=100000000)
    
    hra = forms.IntegerField(max_value=100000000)
    
    salary = forms.IntegerField(max_value=10000000000)
    
    
    class Meta:
        model = Emp
        fields = '__all__'
        
   
        
    def __init__(self, *args, **kwargs):
        super(EmpForm, self).__init__(*args, **kwargs)
        self.fields['pin'].widget.attrs.update({'minlength': 6, 'maxlength': 8})
        self.fields['emp_no'].widget.attrs.update({'maxlength': 8})
        self.fields['ph_no'].widget.attrs.update({'minlength': 10, 'maxlength': 10})
        self.fields['hra'].widget.attrs.update({'maxlength': 8})
        self.fields['basic'].widget.attrs.update({'maxlength': 8})
        self.fields['emp_name'].widget.attrs.update({'maxlength': 30})
        self.fields['rep_officer_name'].widget.attrs.update({'maxlength': 30})
        self.fields.pop('salary')  
