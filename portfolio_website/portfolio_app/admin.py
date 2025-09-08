from django.contrib import admin
from .models import Project, Certification, Skill

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'tech_stack', 'priority', 'created_at')
    search_fields = ('title', 'tech_stack')

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuer', 'issue_date')
    search_fields = ('title', 'issuer')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'skill_type', 'level', 'order')
    list_filter = ('skill_type',)
