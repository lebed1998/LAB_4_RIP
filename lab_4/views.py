from django.shortcuts import render
from django.views.generic import TemplateView

from lab_4.models import Subject, Teacher


class IndexView(TemplateView):
    def get(self, *args, **kwargs):
        data = {
            'subjects': Subject.objects.all().order_by('-semester'),
            'front_page': True
        }
        return render(self.request, 'index.html', data)


class SubjectView(TemplateView):
    def get(self, *args, **kwargs):
        data = {
            'subject': Subject.objects.filter(id=kwargs['id']).first()
        }
        return render(self.request, 'subject.html', data)


class TeacherView(TemplateView):
    def get(self, *args, **kwargs):
        data = {
            'teacher': Teacher.objects.filter(id=kwargs['id']).first()
        }
        return render(self.request, 'teacher.html', data)