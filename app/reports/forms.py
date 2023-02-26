from django import forms

from .models import Remark


class RemarkCreateForm(forms.ModelForm):
    class Meta:
        model = Remark
        fields = "__all__"
        exclude = ["created_by"]
