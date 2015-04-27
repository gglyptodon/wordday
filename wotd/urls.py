from django.conf.urls import include, url


urlpatterns = [
    url(r'^$','wotd.views.main', name='main'),
    url(r'^wotd/(?P<word_id>\d+)/$','wotd.views.word_detail', name='word_detail'),
]