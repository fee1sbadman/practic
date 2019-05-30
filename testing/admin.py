from django.contrib import admin
from .models import Test,Question,Choice
# Register your models here.

class TestAdmin(admin.ModelAdmin):
    list_display = ('name', 'info')

admin.site.register(Test, TestAdmin)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3 


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Date information', {'fields': ['right_choice']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)