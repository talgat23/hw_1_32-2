from django.shortcuts import render
from .models import ProgramLang


def program_lang_view(request):
    lang = ProgramLang.objects.all()
    return render(request, 'library.html', {'lang_key': lang})
