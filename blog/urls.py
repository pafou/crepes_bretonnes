from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^accueil$', views.accueil, name='accueil'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^article/$', views.article, name='article'),
    url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)/$', views.addition),
    url(r'^article/(\d+)$', views.lire, name='lire'),
    url(r'^article/(?P<id_article>\d+)$', views.view_article, name="afficher_article"),
    url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})$', views.list_articles),
    url(r'^redirection$', views.view_redirection),
]