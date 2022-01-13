from django import forms

class ContactMeForm(forms.Form):
    emailid = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg fs-6 border-0 shadow-sm', 'style':'background-color:#f6f6f8', 'placeholder':'Your email', 'required':'true'}), required=True)
    subject = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg fs-6 border-0 shadow-sm', 'style':'background-color:#f6f6f8','placeholder':'Subject', 'required':'true'}), required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control form-control-lg fs-6 border-0 shadow-sm', 'style':'background-color:#f6f6f8', 'placeholder':'Your Message', 'required':'true'}), required=True)