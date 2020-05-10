import math
from django.db import connection


class SqlPaginator(object):
    """实现分页"""
    def __init__(self, sql, params, page_size):
        super().__init__()
        self.sql = sql
        self.params = params
        self.page_size = page_size

    def page(self, now_page):
        cursor = connection.cursor()
        sql = self.sql + ' LIMIT %s,%s'
        offset = (now_page - 1)*self.page_size
        self.params.extend([offset, self.page_size])
        cursor.execute(sql, self.params)
        result = cursor.fetchall()
        return result

    def count(self):
        cursor = connection.cursor()
        if len(self.params) == 2:
            cursor.execute(self.sql)
        else:
            cursor.execute(self.sql, self.params)
        result = cursor.fetchall()
        return len(result)

    def total(self):
        return math.ceil(self.count()/self.page_size)