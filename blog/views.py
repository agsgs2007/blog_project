# -*- coding:utf-8 -*-

from django.shortcuts import render

#在此次创建日志器，根据设定输出错误信息
import logging
logger = logging.getLogger('blog.views')


def index(request):

    # 不存在的文件，输出错误日志
    try:
        file = open('sss.txt', 'r')
    except Exception as e:
        logger.error(e)

    return render(request, 'index.html', locals())
