from django import forms

class ContactMeForm(forms.Form):
    emailid = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg fs-6 border-0 shadow-sm', 'placeholder':'email yawe'}), required=True)
    subject = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg fs-6 border-0 shadow-sm', 'placeholder':'igituma '}), required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control form-control-lg fs-6 border-0 shadow-sm', 'placeholder':'Twandikire nyaha'}), required=True)