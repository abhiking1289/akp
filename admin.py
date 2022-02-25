from msilib.schema import Media
from django.contrib import admin
from .models import Destination
from .models import Basic_Information
from .models import Curriculum
from .models import MEDIA

admin.site.register(Destination)
admin.site.register(Basic_Information)
admin.site.register(Curriculum.Add_Lecture.basic_lecture)
admin.site.register(Curriculum.Add_Lecture.Video_Runtime)
admin.site.register(Curriculum.Add_Lecture.Attachments)
admin.site.register(MEDIA)
admin.site.register(Curriculum.Add_Quiz.Add_Quiz_Basic)
admin.site.register(Curriculum.Add_Quiz.Questions)
admin.site.register(Curriculum.Add_Quiz.Questions.Add_Quiz_Question)
admin.site.register(Curriculum.Add_Quiz.Questions.question_image)
admin.site.register(Curriculum.Add_Quiz.Setting)
# Register your models here.
