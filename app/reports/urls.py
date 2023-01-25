from django.urls import path

from .views import StudentDetailView, StudentListView, RemarkCreateView, RemarkDetailView, YearClassListView, YearClassDetailView

urlpatterns = [
    path("", YearClassListView.as_view(), name="year-class-list"),
    path("year-class/detail/<int:pk>/", YearClassDetailView.as_view(), name="year-class-detail"),
    path("students/", StudentListView.as_view(), name="student-list"),
    path("student/detail/<int:pk>/", StudentDetailView.as_view(), name="student-detail"),
    path("remark/create/", RemarkCreateView.as_view(), name="remark-create"),
    path("remark/detail/<int:pk>/", RemarkDetailView.as_view(), name="remark-detail"),
    
]
