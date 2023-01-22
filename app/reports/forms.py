from django import forms

from .models import Remark


class RemarkCreateForm(forms.ModelForm):
    class Meta:
        model = Remark
        fields = "__all__"
