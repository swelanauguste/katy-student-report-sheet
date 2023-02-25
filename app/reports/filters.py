import django_filters
from django import forms

from .models import Student, Subject, YearClass


class StudentFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(
        lookup_expr="icontains",
        label="First name",
        widget=forms.TextInput(attrs={"class": "rounded-pill form-control-sm"}),
    )
    last_name = django_filters.CharFilter(
        lookup_expr="icontains",
        label="Last name",
        widget=forms.TextInput(attrs={"class": "rounded-pill form-control-sm"}),
    )

    year_class = django_filters.ModelChoiceFilter(
        queryset=YearClass.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "rounded-pill form-control-sm",
                "onchange": "this.form.submit()",
                "placeholder": "all",
            }
        ),
    )

    subject__name = django_filters.ModelChoiceFilter(
        queryset=Subject.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "rounded-pill form-control-sm",
                "onchange": "this.form.submit()",
            }
        ),
    )

    class Meta:
        model = Student
        fields = ("last_name", "first_name", "year_class", "subject__name")
