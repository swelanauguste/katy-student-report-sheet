from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView

from .filters import StudentFilter
from .forms import RemarkCreateForm
from .models import Remark, Student, YearClass


class StudentListView(ListView):
    model = Student

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = StudentFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.filterset.form
        return context


class StudentDetailView(DetailView):
    model = Student


class StudentCreateView(SuccessMessageMixin, CreateView):
    model = Student
    fields = "__all__"
    success_message = "%(student_id)s was created successfully"


class RemarkCreateView(SuccessMessageMixin, CreateView):
    model = Remark
    form_class = RemarkCreateForm
    success_message = "%(title)s was created successfully"

    # def form_valid(self, form):
    #     form.instance.created_by = self.request.user
    #     return super().form_valid(form)


class RemarkDetailView(DetailView):
    model = Remark


class YearClassListView(ListView):
    model = YearClass


class YearClassDetailView(DetailView):
    model = YearClass
