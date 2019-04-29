from django.db import models

# Create your models here.


class UserInfo(models.Model):
    userName = models.CharField(max_length=10)
    userPassword= models.CharField(max_length=40)
    idDelete = models.BooleanField()

    # userManager = models.Manager()

class Page:
    def __init__(self, current_page, total_count, base_url, per_page=10, max_page_num=11):
        """
        :param current_page:当前页
        :param total_count: 总数量
        :param base_url: 请求url
        :param per_page: 每页数量
        :param max_page_num:每页最大页码数
        """

        # 当前页
        try:
            self.current_page = int(current_page)
        except Exception as e:
            self.current_page = 1
        # 每页数量
        self.per_page = per_page
        # 总页数
        total_page, more = divmod(total_count, per_page)
        if more:
            total_page += 1
        self.total_page = total_page
        # 最大页码数
        self.max_page_num = max_page_num
        self.half_page_num = max_page_num // 2
        self.base_url = base_url

    @property
    def start(self):
        return (self.current_page - 1) * self.per_page

    @property
    def end(self):
        return self.current_page * self.per_page

    def page_html(self):
        if self.total_page <= self.max_page_num:
            # 总页码数小于最大页码数
            start_page = 1
            end_page = self.total_page
        elif self.current_page + self.half_page_num >= self.total_page:
            # 右边越界
            end_page = self.total_page
            start_page = self.total_page - self.max_page_num
        elif self.current_page - self.half_page_num <= 1:
            # 左边越界
            start_page = 1
            end_page = self.max_page_num
        else:
            # 正常
            start_page = self.current_page - self.half_page_num
            end_page = self.current_page + self.half_page_num

        # 生成页码html
        page_html_list = []

        # 添加首页页码
        first_li = '<li><a href="{}?page=1">首页</a></li>'.format(self.base_url)
        page_html_list.append(first_li)

        # 添加上一页
        if self.current_page == 1:
            prev_li = '<li class="disabled"><a href="#"><span aria-hidden="true">&laquo;</span></a></li>'
        else:
            prev_li = '<li><a href="{}?page={}"><span aria-hidden="true">&laquo;</span></a></li>'.format(
                self.base_url, self.current_page - 1)
        page_html_list.append(prev_li)

        # 添加中间页码
        for i in range(start_page, end_page + 1):
            if i == self.current_page:
                li = '<li class="active"><a href="{0}?page={1}">{1}</a></li>'.format(self.base_url, i)
            else:
                li = '<li ><a href="{0}?page={1}">{1}</a></li>'.format(self.base_url, i)
            page_html_list.append(li)

        # 添加下一页
        if self.current_page == self.total_page:
            next_li = '<li class="disabled"><a href="#"><span aria-hidden="true">&raquo;</span></a></li>'
        else:
            next_li = '<li><a href="{}?page={}"><span aria-hidden="true">&raquo;</span></a></li>'.format(
                self.base_url, self.current_page + 1)
        page_html_list.append(next_li)

        # 添加尾页
        end_li = '<li><a href="{}?page={}">尾页</a></li>'.format(self.base_url, self.total_page)
        page_html_list.append(end_li)

        return ''.join(page_html_list)
