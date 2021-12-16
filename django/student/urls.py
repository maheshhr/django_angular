from django.urls import path

from student.views import StudentListView, StudentCreateView, StudentDetailView, StudentUpdateView, \
    StudentDeleteView

urlpatterns = [
    path('list/',StudentListView.as_view(),name='student_list'),
    path('create/',StudentCreateView.as_view(),name='student_create'),
    path('detail/<int:pk>',StudentDetailView.as_view(),name='student_detail'),
    path('update/<int:pk>',StudentUpdateView.as_view(),name='student_update'),
    path('delete/<int:pk>',StudentDeleteView.as_view(),name='student_delete'),
]
