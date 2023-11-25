from django import forms

class ImageForm(forms.Form):
    description = forms.CharField(widget=forms.Textarea)
    image_data = forms.ImageField()