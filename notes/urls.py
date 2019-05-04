from django.contrib import admin
from django.urls import path, include
from notes.views import *
from django.contrib.auth import views as authViews


app_name = 'notes'

urlpatterns = [
    path('', index_view, name='index'),
    path('addnote/', add_note, name='addnote'),
    path('addtag/', add_tag, name='addtag'),
    # path('savetag/', save_tag, name='savetag'),
    path('tags/<int:id>', tag_search, name='tagsearch'),
    path('logout/', authViews.LogoutView.as_view(template_name="exit.html"), name='logout'),
    # path('logout/', 'django.contrib.auth.logout', {'next_page': 'home'}, name='logout'),
]