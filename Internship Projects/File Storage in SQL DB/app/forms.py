from django import forms
from .models import MediaStore
import os

class MediaFileForm(forms.ModelForm):
    upload_file = forms.FileField()  # Add a FileField for file uploads

    file_number = forms.IntegerField(required=True)
    file_name = forms.CharField(max_length=30)
    
    class Meta:
        model = MediaStore
        fields = ['file_number', 'file_name', 'file_type', 'file_extension']  # Exclude file_data

    def save(self, commit=True):
        instance = super(MediaFileForm, self).save(commit=False)
        uploaded_file = self.cleaned_data['upload_file']
        instance.file_extension = os.path.splitext(uploaded_file.name)[1][1:]  # Extract the file extension
        instance.file_data = uploaded_file.read()  # Read the file data
        if commit:
            instance.save()
        return instance
    
    def __init__(self, *args, **kwargs):
        super(MediaFileForm, self).__init__(*args, **kwargs)
        self.fields['file_number'].widget.attrs.update({ 'maxlength': 8})
        self.fields['file_name'].widget.attrs.update({ 'maxlength': 8})
        self.fields.pop('file_extension')  
    
    FILE_TYPE_CHOICES = [
        ('document', 'Document'),
        ('image', 'Image'),
    ]
