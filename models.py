from distutils.command.upload import upload
from email.policy import default
from django.db import models

AUDIO_CHOICES = (
            ('Select Caption', "Select Caption"),
            ('ENGLISH' , "English"),
            ('Español', "Español"),
            ('Português', "Português"),
            ('Italiano',"Italiano"),
            ('Français', "Français"),
            ('Polski', "Polski"),
            ('Deutsch', "Deutsch"),
            ('Bahasa Indonesia',"Bahasa Indonesia"),
            ('ภาษาไทย', "ภาษาไทย"),
            ('हिन्दी',"हिन्दी"),
            ('Tamil',"Tamil"),
            ('मराठी',"मराठी"),
            ('Telugu',"Telugu"),
        )
LEVEL_CHOICES = (
    ('Select Level',"Select Level"),
    ('Beginner',"Beginner"),
    ('Intermediate',"Intermediate"),
    ('Expert',"Expert"),
)
VIDEO_CHOICES = (
    ('HTML5(mp4)',"HTML5(mp4)"),
    ('External Url',"External Url"),
    ('Youtube',"Youtube"),
    ('Vimeo',"Vimeo"),
    ('embedded',"embedded"),
)
QUESTION_CHOICES = (
    ('Single Choice',"Single Choice"),
    ('Multiple Choice',"Multiple Choice"),
    ('Single Line Text',"Single Line Text"),
    ('Multi Line Text',"Multi Line Text"),
)
class Destination(models.Model):
    City =  models.CharField(max_length=100)
    img = models.ImageField(upload_to ='pics')  
    Description =  models.TextField()
    Arrival =  models.IntegerField()
    Budjet =  models.IntegerField()
class Basic_Information(models.Model):
    Course_title = models.CharField(max_length=60)
    Short_Description = models.TextField()
    Course_Description = models.TextField()
    What_will_students_learn_in_your_course = models.TextField()
    Requirements = models.TextField()
    Course_level = models.CharField(
            max_length= 30,
            choices= LEVEL_CHOICES,
            default = 'Select Level'
        )
    Close_Caption = models.CharField(
            max_length= 30,
            choices= AUDIO_CHOICES,
            default = 'Select Caption'
        )
    Audio_Language = models.CharField(
            max_length= 30,
            choices= AUDIO_CHOICES,
            default = 'Select Caption'
        )
    Course_Category = models.TextChoices
class Curriculum(models.Model):
    class Add_Lecture(models.Model):
            class basic_lecture(models.Model):
                Lecture_title = models.CharField(max_length=30)
                Description = models.TextField()
            class Video_Runtime(models.Model):
                    Runtime = models.TimeField('%H:%M:%S')
            class Attachments(models.Model):
                upload_ID12 = models.FileField(upload_to='pics/')
                upload_ID13 = models.FileField(upload_to='pics/')
                upload_ID14 = models.FileField(upload_to='pics/')
    class Add_Quiz(models.Model):
        class Add_Quiz_Basic(models.Model):
            Quiz_title = models.CharField(max_length=60)
            Description = models.TextField()
        class Questions(models.Model):
             class Add_Quiz_Question(models.Model):
                Question_Type = models.CharField(
                    max_length=60,
                    choices= QUESTION_CHOICES,
                    default = 'Select Caption'
                )
             class question_image(models.Model):
                Image = models.ImageField(upload_to ='pics/')
                question_title = models.TextField()
                score = models.TextField()
        class Setting(models.Model):
            Time_Limit = models.TextField()
            Passing_Score = models.TextField()
            Questions_Limit = models.TextField()
class MEDIA(models.Model):
    class Introduction_Video(models.Model):
        Video_Type = models.CharField(
                    max_length=60,
                    choices= VIDEO_CHOICES
                )
    class Course_thumbnail(models.Model):
        course_thumbnail = models.ImageField(upload_to='pics', height_field=590, width_field=300, max_length=100)
