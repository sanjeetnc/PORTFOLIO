from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    short_desc = models.TextField()
    long_desc = models.TextField(blank=True)
    tech_stack = models.CharField(max_length=300, blank=True)
    live_url = models.URLField(blank=True)
    repo_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Certification(models.Model):
    title = models.CharField(max_length=250)
    issuer = models.CharField(max_length=200, blank=True)
    issue_date = models.DateField(null=True, blank=True)
    credential_url = models.URLField(blank=True)
    badge_image = models.ImageField(upload_to='certs/', blank=True, null=True)
    file = models.FileField(upload_to='cert_files/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} — {self.issuer or 'Unknown'}"


class Skill(models.Model):
    HARD = 'hard'
    SOFT = 'soft'
    SKILL_TYPE_CHOICES = [
        (HARD, 'Hard Skill'),
        (SOFT, 'Soft Skill'),
    ]
    name = models.CharField(max_length=120)
    skill_type = models.CharField(max_length=10, choices=SKILL_TYPE_CHOICES)
    level = models.PositiveIntegerField(default=70, help_text="Percent proficiency: 0-100")
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.skill_type})"
