from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import uuid

from django.contrib.auth.models import PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, email, firstname, lastname, phone, password=None):
        user = self.model(
            email=self.normalize_email(email),
            firstname=firstname,
            lastname=lastname,
            phone=phone,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, firstname, lastname, phone, password=None):
        user = self.create_user(
            email=email,
            password=password,
            firstname=firstname,
            lastname=lastname,
            phone=phone,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser,PermissionsMixin):
    id = models.CharField(max_length=200, default=uuid.uuid4, unique=True, primary_key=True)
    email = models.EmailField(null=False, max_length=100, unique=True)
    firstname = models.CharField(null=False, max_length=100)
    image = models.ImageField(verbose_name='аватарка', upload_to='user_images/', blank=True, null=True)
    lastname = models.CharField(null=False, max_length=100)
    phone = models.IntegerField(null=False, unique=True)
    date_joined = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname', 'phone']

    objects = UserManager()

    def __str__(self):
        return self.email + ", " + self.firstname

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

class Comment(models.Model):
    
    class Meta:
        verbose_name = 'коммент'
        verbose_name_plural = 'комменты'
        
    user = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name='user id')
    text = models.TextField(verbose_name='контент')
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.user} - {self.date}'
        
class Documentation(models.Model):
    class Meta:
        verbose_name = 'документ'
        verbose_name_plural = 'документы'

    name = models.CharField(max_length=100, verbose_name='имя')
    # tema = models.ForeignKey('Topics_Documentation',  on_delete=models.PROTECT )
    tema = models.CharField(max_length=100, verbose_name='тема')
    description = models.TextField(verbose_name='описание')
    zadacha = models.TextField(verbose_name='задача', blank=True, null=True)
    image = models.ImageField(verbose_name='изображение', upload_to='documents_images/', blank=True, null=True)
    link_youtube = models.CharField(max_length=200, verbose_name='ссылка от ютуба на видео')
    reshenie = models.TextField(verbose_name='решение задачи')
    

    def __str__(self):
        return f'{self.name} - {self.tema}'


class Topics_Documentation(models.Model):
    class Meta:
        verbose_name = 'подтема'
        verbose_name_plural = 'подтемы'

    name = models.CharField(max_length=100, verbose_name='имя подтемы')
    document = models.ManyToManyField('Documentation', related_name='topics', verbose_name='документы')

    def __str__(self):
        return f'{self.name}'


class All_Topics_Documentation(models.Model):
    class Meta:
        verbose_name = 'сборник'
        verbose_name_plural = 'сборники'

    name = models.CharField(max_length=100, verbose_name='имя сборника')
    document = models.ManyToManyField('Topics_Documentation', related_name='all_topics', verbose_name='подтемы')

    def __str__(self):
        return f'{self.name}'


class Test(models.Model):
    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'

    title = models.CharField(max_length=100, blank=True, null=True, verbose_name='имя вопроса')
    question = models.TextField(verbose_name='вопрос')
    var1 = models.TextField(verbose_name='вариант1')
    var2 = models.TextField(verbose_name='вариант2')
    var3 = models.TextField(verbose_name='вариант3')
    answer = models.TextField(verbose_name='правильный ответ')
    level = models.CharField(max_length=100, verbose_name='уровень')

    def __str__(self):
        return f'{self.title} - {self.level}'


class Topics_Test(models.Model):
    class Meta:
        verbose_name = 'тест'
        verbose_name_plural = 'тесты'

    name = models.CharField(max_length=100, verbose_name='имя теста')
    test = models.ManyToManyField('Test', related_name='tests', verbose_name='тесты')
    level = models.CharField(max_length=100, verbose_name='уровень')

    def __str__(self):
        return f'{self.name}'


class AboutUs(models.Model):
    class Meta:
        verbose_name = 'программист'
        verbose_name_plural = 'программисты'

    name = models.CharField(max_length=100, verbose_name='имя программиста')
    image = models.ImageField(verbose_name='изображение', upload_to='developer_images/', blank=True, null=True)
    email = models.EmailField(verbose_name='почта')
    instagram = models.TimeField(verbose_name='instagram')
    description = models.CharField(max_length=300, verbose_name='описание')
    status = models.CharField(max_length=100, verbose_name='статус')

    def __str__(self):
        return f'{self.name} - {self.status}'
