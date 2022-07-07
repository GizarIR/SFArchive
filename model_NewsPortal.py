from django.db import models

guest = 'GU'
user = 'US'
admin = 'AD'
author = 'AU'

USER_STATUS = [
    (guest, 'Гость'), #Гость может только читать
    (user, 'Читатель'), #для пользователя будет рассылка и можно оставлять комментарии
    (admin, 'Администратор'), #Полные права
    (author, 'Автор'), #Может все что и читатель плюс публиковать статьи
]

draft = 'DR'
published = 'PU'

ARTICLE_STATUS = [
    (draft, 'Черновик'),
    (published, 'Опубликовано'),
    (modifyed, 'Изменено')
]

# class Product(models.Model):
#     name = models.CharField(max_lenght = 255)
#     price = models.FloatField(default = 0.0)
#     composition = models.TextField(default = "Состав не указан")
#     time_in = models.DateTimeField(auto_now_add=True)
#     time_out = models.DateTimeField(null=True)
#         position = CharField(max_lenght=2,
#                              choices=POSITIONS,
#                              default=cashier)



# Класс для работы Пользователями
class User (models.Model):
    personal_email = models.EmailField()
    pwd = models.CharFields(max_lenght = 50)
    full_name = models.CharFields(max_lenght = 255)
    data_reg_u = models.DateTimeField(auto_now_add = True)
    data_reg_a = models.DateTimeField(null = True)
    u_status = CharField(max_lenght = 2,
                         choices = USER_STATUS,
                         default = user)


# Класс для работы со Статьями
class Article (models.Model):
    header = models.CharFields(max_lenght = 255)
    short_news = models.CharFields(max_lenght = 255)
    article_text = models.TextField()
    date_create = models.DateTimeField(auto_now_add = True)
    date_publish = models.DateTimeField(null = True)
    date_modify = models.DateTimeField(auto_now = True)
    a_status = CharField(max_lenght = 2,
                         choices = ARTICLE_STATUS,
                         default = draft)
    users = models.ManyToManyField(User, through='ArticleUser')

# Класс для работы с комментариями
class Comment (models.Model):
    comment_text = models.TextField()
    date_create = models.DateTimeField(auto_now_add = True)
    article = models.ForeignKey(User, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)




# Класс для обеспечения связи Многие-многие - таблица новостей
class ArticleUser (models.Model):
    arcticle = models.ForeignKey(Article, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)


