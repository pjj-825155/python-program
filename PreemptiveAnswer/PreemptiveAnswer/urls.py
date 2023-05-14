from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^host-login/$', views.host_login),
    url(r'^player-login/$', views.player_login),
    url(r'^host-logining/$', views.host_logining),
    url(r'^player-logining/$', views.player_logining),
    url(r'^change-score/$', views.change_score),
    url(r'^start/$', views.start),
    url(r'^answer/$', views.answer),
    url(r'^player-answer/(.+)/$', views.player_answer),
    url(r'^stop/$', views.stop),
    url(r'^host/$', views.host),
    url(r'^player/(.+)/$', views.player),
]