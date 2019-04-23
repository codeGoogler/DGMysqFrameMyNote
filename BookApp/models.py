from django.db import models


# Create your models here.

#
# class BookInfo(models.Model):
#     btitle = models.CharField(max_length=20)
#     bpub_date = models.DateTimeField(db_column='pub_date')
#     breadnum = models.IntegerField(default=0)
#     bcomment = models.IntegerField(null=False)
#     isDelete = models.BooleanField(default=False)
#
#     class Meta:
#         db_table = 'djbookinfo'
#
#     bookManager = models.Manager()
#
#     # 模型类的创建方法
#     @classmethod  # 不能用于普通的方法，因为还没哟创建这个对象
#     def create(self, btitle, bpub_date):
#         b = BookInfo()
#         b.btitle = btitle
#         b.bpub_date = bpub_date
#         b.bcomment = 0
#         b.breadnum = 0
#         b.isDelete = 0
#         return b
#
#
# class HeroInfo(models.Model):
#     hname = models.CharField(max_length=10)
#     hgender = models.BooleanField(default=False)
#     hcontent = models.CharField(max_length=1000)
#     isDelete = models.BooleanField(default=False)
#     book = models.ForeignKey(BookInfo, "on_delete=models.CASCADE()")
#
#     class Meta:
#         db_table = 'djheroinfo'
#
#     def showName(self):
#         return self.hname
