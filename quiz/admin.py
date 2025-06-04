from django.contrib import admin
from .models import  *

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    #list_display = ["user__username","level__pseudo"]
    list_filter = ["level__name"]
    
    
@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ["name","pseudo"]
    
    
@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ["Question","good_answer"]
    list_filter = ["categories"]
    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
    
    
@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    pass
