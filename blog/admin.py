# -*- coding:utf-8 -*-

from django.contrib import admin

from .models import *


# 自定义管理页面显示的内容
class AdAdmin(admin.ModelAdmin):

    fields = ('title', 'description',)
    list_display = ('title', 'description',)  #列表显示内容

# 使用默认的方法在admin模块中注册模型，然后可以登录admin网页，需要
# 提前manage.py createsuperuser创建超级用户

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Ad, AdAdmin)
admin.site.register(Article)
admin.site.register(Links)
admin.site.register(Tag)
admin.site.register(Comment)