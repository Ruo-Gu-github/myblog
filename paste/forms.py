from django import forms
from paste.models import Paste

class PasteForm(forms.ModelForm):

    class Meta:
        model = Paste
        fields = ('title', 'poster', 'syntax', 'content')
