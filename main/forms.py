from django import forms

from main.models import User

class MainForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super(MainForm, self).__init__(*args, **kwargs)
    #     self.fields['myfield'].widget.attrs.update({'class': 'myfieldclass'})

    