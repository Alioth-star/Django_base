from django.apps import AppConfig


class BookConfig(AppConfig):
    name = 'book'
    # admin页面的’book‘变成'书籍管理'
    verbose_name = '书籍管理'
