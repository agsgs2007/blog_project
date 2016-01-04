# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.conf import settings

#在此次创建日志器，根据设定输出错误信息
import logging
logger = logging.getLogger('blog.views')


# 用于模板的全局配置信息,该函数作为模板的上下文处理器
# 模板中可以直接使用下面的字典名

def global_settings(request):
    return {'SITE_NAME':settings.SITE_NAME,
            'SITE_DESC':settings.SITE_DESC}


def index(request):

    # 不存在的文件，输出错误日志
    try:
        file = open('sss.txt', 'r')
    except Exception as e:
        logger.error(e)

    return render(request, 'index.html', locals())
