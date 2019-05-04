from django import forms
from notes.models import Note, Tag

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('label', 'body', 'tags')


    def __init__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)  # Call to ModelForm constructor
        self.fields['tags'].widget.attrs['style'] = 'height: 200px;'

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('label', )
