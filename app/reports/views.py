from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView

from .forms import RemarkCreateForm
from .models import Remark, Student


class StudentListView(ListView):
    model = Student


class StudentDetailView(DetailView):
    model = Student


class RemarkCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Remark
    form_class = RemarkCreateForm
    success_message = "%(title)s was created successfully"

    # def form_valid(self, form):
    #     form.instance.created_by = self.request.user
    #     return super().form_valid(form)


class RemarkDetailView(DetailView):
    model = Remark
