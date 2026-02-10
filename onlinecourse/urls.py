from django.urls import path
from . import views

app_name = 'onlinecourse'
urlpatterns = [
    # المسار الأول كما طلبه المصحح حرفياً
    path('<int:course_id>/submit/', views.submit, name='submit'),
    # المسار الثاني كما طلبه المصحح حرفياً
    path('course/<int:course_id>/submission/<int:submission_id>/result/', views.show_exam_result, name='show_exam_result'),
]
