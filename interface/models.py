# coding=utf-8
from django.db import models

# Create your models here.


class interfaceData(models.Model):
    # EXCEPT_CHOICE = (
    #     (u'M', u'contains'),
    #     (u'F', u'Female'),
    # )
    id = models.AutoField(auto_created=True, primary_key=True, db_column='id')
    # 接口名称
    name = models.CharField(max_length=30, db_column='name', null=False)
    # case描述
    describe = models.CharField(max_length=50, db_column='describe', null=False)
    # url
    url = models.TextField(db_column='url', null=False)
    # 请求方式
    method = models.CharField(max_length=10, db_column='method', null=False)
    # 请求数据
    request_data = models.TextField(db_column='request_data', null=True)
    # 期望
    except_desc = models.CharField(max_length=20, db_column='except_desc', null=False)
    # 期望内容
    except_content = models.TextField(db_column='except_content', null=False)
    # 添加时间
    add_time = models.DateTimeField(db_column='add_time', auto_now=True)
    # 是否删除
    is_delete = models.BooleanField(db_column='is_delete', default=False)
    # 删除时间
    delete_time = models.DateTimeField(db_column='delete_time', null=True)

    def __unicode__(self):
        return self.name + self.url

    class Meta:
        # 竞品数据对比主表
        db_table = 'interface_data'
        ordering = ['id']
