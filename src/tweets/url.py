from django.conf.urls import url
# from .views import tweet_detail_view, tweet_list_view
from .views import TweetListView, TweetDetailView


urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    #url(r'^$', tweet_list_view, name='list'),
    url(r'^$', TweetListView.as_view(), name='list'),
    #url(r'^1/$', tweet_detail_view, name='detail'),
    url(r'^1/$', TweetDetailView.as_view(), name='detail'),
]

 