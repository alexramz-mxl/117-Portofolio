from django import forms    

class ContactForm(forms.Form):
    name = forms.CharField(max_length=225, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.CharField(max_length=225, widget=forms.TextInput(attrs={'placeholder': 'Email', 'type': 'email'}))
    message = forms.CharField(widget=forms.Textarea({'placeholder': 'Message' }))
    