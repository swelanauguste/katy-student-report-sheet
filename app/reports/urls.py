from django.urls import path

from .views import StudentDetailView, StudentListView, RemarkCreateView, RemarkDetailView

urlpatterns = [
    path("", StudentListView.as_view(), name="student-list"),
    path("student/detail<int:pk>/", StudentDetailView.as_view(), name="student-detail"),
    path("remark/create/", RemarkCreateView.as_view(), name="remark-create"),
    path("remark/detail<int:pk>/", RemarkDetailView.as_view(), name="remark-detail"),
    
]
