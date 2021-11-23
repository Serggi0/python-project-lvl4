from django import forms

from labels.models import Label


class LabelForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = ('name',)
