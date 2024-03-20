from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# Create your models here.
from django.core.validators import MinValueValidator , MaxValueValidator
class Module(models.Model):
    module_id = models.AutoField(primary_key=True , default= 1)
    module_name = models.CharField(max_length=100)  # 
    
class  UserAccount(AbstractUser):
    phone_number = models.CharField(max_length = 15)
    
    
class Course(models.Model):
    featured_img = models.ImageField(upload_to= 'courses_img', null=True)
    course_name = models.CharField(max_length = 100)#
    title = models.TextField()
    features = models.CharField(max_length = 150)
    price = models.DecimalField(max_digits = 10 , decimal_places = 2 , default = 0)
    module = models.ForeignKey(Module , on_delete = models.CASCADE , related_name='courses')
    
    def enrolled_users_count(self):
        return Enrollment.objects.filter(course = self).count()
    
class Bank(models.Model):
    name = models.CharField(max_length = 100)
    logo = models.ImageField(upload_to='bank_logos/')
class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserAccount ,on_delete=models.CASCADE)
    bank = models.ForeignKey(Bank ,on_delete =models.CASCADE)
    transaction_id =models.CharField(max_length = 100)
    timestamp = models.DateTimeField(auto_now_add = True) 
    
    class Meta:
        ordering = ['-timestamp']   
            
class Enrollment(models.Model):
    user = models.ForeignKey(UserAccount , on_delete = models.CASCADE)
    course = models.ForeignKey(Course , on_delete = models.CASCADE)
    payment = models.ForeignKey(Payment , on_delete=models.CASCADE)
    
    


    
# Assume like there is a user Model which register for taking the course

class CourseProgress(models.Model):
    user = models.ForeignKey(UserAccount , on_delete = models.CASCADE)
    course = models.ForeignKey(Course, on_delete =models.CASCADE)
    completed = models.BooleanField(default = False)
    progress_precentage = models.IntegerField(default = 0)
    
    class Meta:
        unique_together  =('user','course')
        
class Video(models.Model):
    title = models.CharField(max_length = 100)        
        
class Quiz(models.Model):
    title = models.CharField(max_length = 10)
    description = models.TextField()   
         
class QuizAttempt(models.Model):
    user = models.ForeignKey(UserAccount , on_delete =models.CASCADE)
    quiz = models.ForeignKey(Quiz , on_delete = models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add =True)
    score = models.IntegerField()
    
    class Meta:
        unique_together = ('user' , 'quiz') 
        
class CourseRating(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

class VideoRating(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])                


class SATQuestion(models.Model):
    question_text = models.TextField()
    answer_choices = models.JSONField()
    correct_answer = models.CharField(max_length=50)
    explanation = models.TextField()
    paragraph = models.TextField(blank=True, null=True)
    diagram = models.ImageField(upload_to='sat_diagrams/', blank=True, null=True)

class TOEFLQuestion(models.Model):
    question_text = models.TextField()
    answer_choices = models.JSONField()
    correct_answer = models.CharField(max_length=50)
    explanation = models.TextField()
    paragraph = models.TextField(blank=True, null=True)
    diagram = models.ImageField(upload_to='toefl_diagrams/', blank=True, null=True)

class UserQuestionAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sat_question = models.ForeignKey(SATQuestion, on_delete=models.CASCADE, blank=True, null=True)
    toefl_question = models.ForeignKey(TOEFLQuestion, on_delete=models.CASCADE, blank=True, null=True)
    correct = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)

class UserProgress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sat_progress = models.FloatField(default=0)
    toefl_progress = models.FloatField(default=0)    
    