from django.db import models
# ------------------------------------ 用户相关 ------------------------------------ #
class UserModel(models.Model):
  username = models.CharField(max_length = 10, verbose_name = '用户名')
  age = models.IntegerField(verbose_name = '年龄')
  gender = models.BooleanField(default = True, verbose_name = '性别')
  status = models.IntegerField(default = True, verbose_name = '账号状态')
  create_time = models.DateTimeField(auto_now_add = True, verbose_name = '创建时间')
  last_login_time = models.DateTimeField(auto_now = True, verbose_name = '最后登录时间')
  is_del = models.BooleanField(default = False, verbose_name = '删除标识')

  def to_json(self):
    return {
      'id': self.id,
      'username': self.username,
      'age': self.age,
      'gender': self.gender,
      'status': self.status,
      'create_time': self.create_time,
      'last_login_time': self.last_login_time
    }

  class Meta:
    db_table = 'user'
# ------------------------------------ 用户相关 end ------------------------------------ #

# ------------------------------------ 文章相关 ------------------------------------ #
''' 文章分类 '''
class ArticleCategoryModle(models.Model):
  category_name = models.CharField(max_length = 50, verbose_name = '分类名称')
  status = models.BooleanField(default = True, verbose_name = '显示状态')
  sort = models.IntegerField(default = 0, verbose_name = '排序')
  create_time = models.DateTimeField(auto_now_add = True, verbose_name = '创建时间')
  update_time = models.DateTimeField(auto_now = True, verbose_name = '更新时间')
  is_del = models.BooleanField(default = False, verbose_name = '删除标识')

  def to_json(self):
    return {
      'id': self.id,
      'category_name': self.category_name,
      'sort': self.sort,
      'status': self.status,
      'create_time': self.create_time,
      'update_time': self.update_time
    }

  class Meta:
    db_table = 'article_category'

''' 文章详情 '''
class ArticleModle(models.Model):
  title = models.CharField(max_length = 50, verbose_name = '文章标题')
  category_id = models.IntegerField()
  description = models.CharField(max_length = 50, verbose_name = '文章简介')
  views = models.IntegerField(default = 0, verbose_name = '阅读量')
  likes = models.IntegerField(default = 0, verbose_name = '点赞数')
  collections = models.IntegerField(default = 0, verbose_name = '收藏数')
  status = models.BooleanField(default = True, verbose_name = '显示状态')
  is_stick = models.BooleanField(default = False, verbose_name = '是否置顶')
  is_del = models.BooleanField(default = False, verbose_name = '删除标识')

  def to_json(self):
    return {
      'id': self.id,
      'title': self.title,
      'description': self.description,
      'views': self.views,
      'likes': self.likes,
      'collections': self.collections,
      'status': self.status
    }

  class Meta:
    db_table = 'article'
# ------------------------------------ 文章相关 end ------------------------------------ #