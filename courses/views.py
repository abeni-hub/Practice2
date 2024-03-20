from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rest_framework import generics,permissions
from .serializers import CourseSerializer , ModuleSerializer , CourseProgressSerializer ,BankSerializer , PaymentSerializer, EnrollmentSerializer , CourseRatingSerializer, VideoRatingSerializer
from .import models
from .models import CourseProgress , Course, UserAccount , Module ,Bank , Payment, Enrollment , CourseRating , VideoRating
from rest_framework import viewsets

class ModuleList(generics.ListCreateAPIView):
    queryset = models.Module.objects.all()  
    serializer_class = ModuleSerializer  

class CourseViewList(generics.ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = CourseSerializer


class CourseProgressViewSet(viewsets.ViewSet):
    @action(detail=True, methods=['post'])
    def update_progress(self, request, pk=None):
        course = Course.objects.get(pk=pk)
        user = request.user

        progress, created = CourseProgress.objects.get_or_create(user=user, course=course)

        # Here you can update the progress based on your requirements.
        progress.completed = request.data.get('completed', progress.completed)
        progress.progress_percentage = request.data.get('progress_percentage', progress.progress_percentage)
        progress.save()

        return Response({'message': 'Progress updated successfully.'}, status=status.HTTP_200_OK)
# Create your views here.

class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class CourseRatingViewSet(viewsets.ModelViewSet):
    queryset = CourseRating.objects.all()
    serializer_class = CourseRatingSerializer

class VideoRatingViewSet(viewsets.ModelViewSet):
    queryset = VideoRating.objects.all()
    serializer_class = VideoRatingSerializer
    
from rest_framework import viewsets
from .models import SATQuestion, TOEFLQuestion, UserQuestionAttempt, UserProgress
from .serializers import SATQuestionSerializer, TOEFLQuestionSerializer, UserQuestionAttemptSerializer, UserProgressSerializer

class SATQuestionViewSet(viewsets.ModelViewSet):
    queryset = SATQuestion.objects.all()
    serializer_class = SATQuestionSerializer

class TOEFLQuestionViewSet(viewsets.ModelViewSet):
    queryset = TOEFLQuestion.objects.all()
    serializer_class = TOEFLQuestionSerializer

class UserQuestionAttemptViewSet(viewsets.ModelViewSet):
    queryset = UserQuestionAttempt.objects.all()
    serializer_class = UserQuestionAttemptSerializer

class UserProgressViewSet(viewsets.ModelViewSet):
    queryset = UserProgress.objects.all()
    serializer_class = UserProgressSerializer    