from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

# <HINT> Register QuestionInline and ChoiceInline classes here

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 5


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 4


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Register your models here.
# class QuestionAdmin(admin.ModelAdmin):
#     inlines = [QuestionInline]
#     list_display = ('text', 'grade')

# class ChoiceAdmin(admin.ModelAdmin):
#     inclines = [ChoiceInline]
#     list_display = ('text', 'is_correct')

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline, QuestionInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['text']

# class ChoiceAdmin(admin.ModelAdmin):
#     list_display = ['text']


# <HINT> Register Question and Choice models here

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Choice)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Submission)
