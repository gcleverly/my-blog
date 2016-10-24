from django import forms

from pagedown.widgets import PagedownWidget

from .models import Project


class ProjectForm(forms.ModelForm):
    body = forms.CharField(widget=PagedownWidget)
    publish = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = Project
        fields = [
            "title",
            "author",
            "subject",
            "body",
            "thumbnail",
        ]