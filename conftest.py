# YaNews conftest.py
import pytest
from django.urls import reverse
from news.models import News
# from notes.models import Note


@pytest.fixture
def author(django_user_model):  
    return django_user_model.objects.create(username='Автор')


@pytest.fixture
def author_client(author, client):
    client.force_login(author)
    return client

@pytest.fixture()
def news():
    news = News.objects.create(
        title='Заголовок',
        text='Текст',
    )
    return news

@pytest.fixture
def news_detail_url(news):
    return reverse('news:detail', args=(news.pk,))

# @pytest.fixture
# def note(author):
#     note = Note.objects.create(
#         title='Заголовок',
#         text='Текст заметки',
#         slug='note-slug',
#         author=author,
#     )
#     return note


# @pytest.fixture
# def slug_for_args(note):  
#     return note.slug,


# @pytest.fixture
# def form_data():
#     return {
#         'title': 'Новый заголовок',
#         'text': 'Новый текст',
#         'slug': 'new-slug'
#     }
