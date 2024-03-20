
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CourseViewSet, VideoViewSet, WorkbookViewSet, QuizViewSet, CourseProgressViewSet,UserQuestionAttemptViewSet, BankViewSet, PaymentViewSet, EnrollmentViewSet , CourseRatingViewSet, VideoRatingViewSet ,SATQuestionViewSet,TOEFLQuestionViewSet,UserQuestionAttempt,UserProgressViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'videos', VideoViewSet)
router.register(r'workbooks', WorkbookViewSet)
router.register(r'quizzes', QuizViewSet)
router.register(r'course-progress', CourseProgressViewSet)
router.register(r'banks', BankViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'course-ratings', CourseRatingViewSet)
router.register(r'video-ratings', VideoRatingViewSet)
router.register(r'sat-questions', SATQuestionViewSet)
router.register(r'toefl-questions', TOEFLQuestionViewSet)
router.register(r'user-question-attempts', UserQuestionAttemptViewSet)
router.register(r'user-progress', UserProgressViewSet)

urlpatterns = [
    path('', include(router.urls)),
]