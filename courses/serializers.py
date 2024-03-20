from rest_framework import serializers
from .import models
from .models import CourseProgress ,Bank , Payment , Enrollment , CourseRating , VideoRating
class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Module
        fields=['module_id', 'module_name']
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ['id' ,'featured_img','course_name','title','features','price','module']        
class CourseProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseProgress
        fields = ['id', 'user', 'course', 'completed', 'progress_percentage'] 
        
class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ['id', 'name', 'logo']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['payment_id', 'user', 'bank', 'transaction_id', 'timestamp']

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['id', 'user', 'course', 'payment']
class CourseRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseRating
        fields = ['id', 'user', 'course', 'rating']

class VideoRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoRating
        fields = ['id', 'user', 'video', 'rating']   
        
from rest_framework import serializers
from .models import SATQuestion, TOEFLQuestion, UserQuestionAttempt, UserProgress

class SATQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SATQuestion
        fields = 'all'

class TOEFLQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TOEFLQuestion
        fields = 'all'

class UserQuestionAttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserQuestionAttempt
        fields = 'all'

class UserProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProgress
        fields = 'all'                            