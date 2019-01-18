import xadmin
from .models import *

# 文章类别
class CategoryAdmin(object):
    list_display = ("id", "name")


xadmin.site.register(Category, CategoryAdmin)


# 文章标签
class TagAdmin(object):
    list_display = ("id","name")


xadmin.site.register(Tag, TagAdmin)


# 文章
class ArticleAdmin(object):
    list_display = ('id', 'title', 'category', 'pub_time','auther')


xadmin.site.register(Article, ArticleAdmin)


# 评论
class CommentAdmin(object):
    list_display = ('name', 'email', 'content', 'publish')


xadmin.site.register(Comment, CommentAdmin)
