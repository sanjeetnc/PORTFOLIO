from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from .models import Project, Certification, Skill
from .forms import CertificationForm

def home_view(request):
    featured = Project.objects.all().order_by('-priority')[:4]
    return render(request, 'home.html', {'featured': featured})

def skills_view(request, type=None):
    # type can be 'hard' or 'soft' — if None, show both grouped
    hard = Skill.objects.filter(skill_type=Skill.HARD).order_by('order')
    soft = Skill.objects.filter(skill_type=Skill.SOFT).order_by('order')
    if request.GET.get('type') == 'hard' or type == 'hard':
        hard = hard
        return render(request, 'skills_list.html', {'skills': hard, 'kind': 'Hard Skills'})
    if request.GET.get('type') == 'soft' or type == 'soft':
        soft = soft
        return render(request, 'skills_list.html', {'skills': soft, 'kind': 'Soft Skills'})
    return render(request, 'skills.html', {'hard': hard, 'soft': soft})

def projects_view(request):
    projects = Project.objects.all().order_by('-priority')
    return render(request, 'projects.html', {'projects': projects})

def certifications_view(request):
    certs = Certification.objects.all().order_by('-issue_date')
    return render(request, 'certifications.html', {'certs': certs})

@staff_member_required
def upload_certification(request):
    """
    Only admin/staff can upload via this page. You can also use Django admin /admin/.
    """
    if request.method == 'POST':
        form = CertificationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Certification uploaded.")
            return redirect('certifications')
    else:
        form = CertificationForm()
    return render(request, 'cert_upload.html', {'form': form})
