from django import forms
from .models import UploadFiles

#class UploadFilesForm(forms.Form):
   # file_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
   # files = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))

class UploadFilesForm(forms.ModelForm):
    class Meta:
        model = UploadFiles
        fields = '__all__'
