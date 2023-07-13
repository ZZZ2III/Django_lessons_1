from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=100)
    file = forms.FileField()

class UploadFileFormHomework(forms.Form):
    title = forms.CharField(max_length=30)
    description = forms.CharField(max_length=100)
    file = forms.FileField()
    pass


class MultiFileForm(forms.Form):
    file_field = forms.FileField(widget = forms.ClearableFileInput(attrs={'multiple':True}))