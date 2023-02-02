from django.contrib.sitemps import Sitemp
from .models import Post

class PostSitemap(Sitemp):
    chagefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.published.all()
    
    def lastmod(self, obj):
        return obj.updated
    

    