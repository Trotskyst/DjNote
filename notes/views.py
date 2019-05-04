from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from notes.models import Note, Tag
from notes.forms import NoteForm, TagForm
from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator
from django.forms.utils import ErrorList


class DivErrorList(ErrorList):
     def __str__(self):              # __unicode__ on Python 2
         return self.as_divs()
     def as_divs(self):
         if not self: return ''
         return '<div class="errorlist">%s</div>' % ''.join(['<div class="error">%s</div>' % e for e in self])


def authuser_only(user):
    return (user.is_authenticated)


@user_passes_test(authuser_only, login_url="/")
def add_note(request):
    id = request.GET.get('id', None)
    if id is not None:
        note = get_object_or_404(Note, id=id)
    else:
        note = None

    if request.method == 'POST':
        if request.POST.get('control') == 'delete':
            note.delete()
            messages.add_message(request, messages.INFO, 'Заметка удалена!')
            return HttpResponseRedirect(reverse('notes:index'))

        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Заметка добавлена!')
            return HttpResponseRedirect(reverse('notes:index'))

    else:
        form = NoteForm(instance=note)

    return render(request, 'notes/addnote.html', {'form': form, 'note': note})


def add_tag(request):
    id = request.GET.get('id', None)
    if id is not None:
        tag = get_object_or_404(Tag, id=id)
    else:
        tag = None

    if request.method == 'POST':

        #временно убираю возможность удаления тега. Не придумал, куда прикрутить
        # if request.POST.get('control') == 'delete':
        #     tag.delete()
        #     messages.add_message(request, messages.INFO, 'Тег удалён!')
        #     return HttpResponseRedirect(reverse('notes:index'))

        form = TagForm(request.POST, instance=tag, error_class=DivErrorList)

        if form.is_valid():
            t = form.save(commit=False)
            t.save()
            messages.add_message(request, messages.INFO, 'Тег добавлен!')
        else:
            messages.add_message(request, messages.INFO, 'Ошибка! Тег уже существует!')
            print(form.errors)
        return HttpResponseRedirect(reverse('notes:addnote'))

    else:
        form = TagForm(instance=tag)

    return render(request, 'notes/newtag.html', {'form': form, 'tag': tag})

@user_passes_test(authuser_only, login_url="/")
def tag_search(request, **kwargs):
    id = kwargs['id']
    tag = get_object_or_404(Tag, id=id)
    notes_all = tag.notes.all()
    paginator = Paginator(notes_all, 2)
    page = request.GET.get('page')
    notes = paginator.get_page(page)
    data = {
        'notes': notes,
        'tag': tag,
        'title': 'Заметки по тегу "'+ tag.label + '"'
    }
    return render(request, 'notes/tagsearch.html', data)


@user_passes_test(authuser_only, login_url="/")
def index_view(request):
    notes_all =  Note.objects.all().order_by('-timestamp')
    paginator = Paginator(notes_all, 5)
    page = request.GET.get('page')
    notes = paginator.get_page(page)
    data = {
        'notes': notes,
        'tags': Tag.objects.all().order_by('label'),
        'title': 'DjNote. Заметки'
    }
    return render(request, 'notes/index.html', data)
