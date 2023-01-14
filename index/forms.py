from django import forms

class sendEmail(forms.ModelForm):
    email = forms.EmailField() 
