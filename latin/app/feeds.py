from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Country


class LatestPostsFeed(Feed):
    title = 'Django Latin'
    link = '/app/'
    description = 'New posts of our site'

    def items(self):
        return Country.objects.all()[:3]

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        return truncatewords(item.description, 30)
