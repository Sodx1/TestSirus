from django import forms

class ImageForm(forms.Form):
    """
    Класс для добавления картинок
    """
    description = forms.CharField(widget=forms.Textarea)
    image_data = forms.ImageField()