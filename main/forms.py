from django import forms

from main.models import User

class MainForm(forms.ModelForm):

   
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MainForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})
        

    