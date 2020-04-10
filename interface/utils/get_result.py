# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""


class GetResult:

    @staticmethod
    def get_result_except(res, except_desc, except_content):
        print(except_desc, except_content)
        if except_desc == 'contains':
            if except_content in res:
                return True
            print("result", type(res), except_content, except_content in res)
        if except_desc == 'equal':
            if except_content == res:
                return True
        if except_desc == 'notcontains':
            if except_content not in res:
                return True

        if except_desc == 'notequal':
            if not except_content == res:
                return True
        print("error false")
        return False

