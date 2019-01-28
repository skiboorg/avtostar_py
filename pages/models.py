from django.db import models
from pytils.translit import slugify
from ckeditor_uploader.fields import RichTextUploadingField





class Image(models.Model):
    image = models.ImageField('Изображение', upload_to='upload_img/', blank=False)
    big_text = models.CharField('Большой текст', max_length=255, blank=False, null=True)
    small_text = models.CharField('Малый текст', max_length=255, blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return 'Изображение '

    class Meta:
        verbose_name = "Изображение "
        verbose_name_plural = "Изображения "

class Service(models.Model):
    name = models.CharField('Название сервиса', max_length=255, blank=False, null=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField('Изображение сервиса для главной', upload_to='upload_img/', blank=False)
    head_image = models.ImageField('Изображение сервиса для шапки страницы', upload_to='upload_img/', blank=False)
    head_description = models.CharField('Короткое описание в шапке страницв ', max_length=255, blank=True, null=True, default='')
    icon = models.CharField('Иконка', max_length=50, blank=True, null=True)
    short_description = models.CharField('Короткое описание ',max_length=255, blank=True, null=True)
    full_description = RichTextUploadingField ('Полное описание ', blank=True, null=True)
    is_main_service = models.BooleanField('Основной сервис?', default=True)
    show_at_home = models.BooleanField('Отображать на главной?', default=False)

    def __str__(self):
        return 'Услуга : %s ' % self.name

    class Meta:
        verbose_name = "Услуга "
        verbose_name_plural = "Услуги "

    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        super(Service, self).save(*args, **kwargs)


class Post(models.Model):
    name = models.CharField('Название поста', max_length=255, blank=False, null=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField('Изображение для страницы', upload_to='upload_img/', blank=True)
    head_image = models.ImageField('Изображение  для шапки страницы', upload_to='upload_img/', blank=False)
    head_description = models.CharField('Короткое описание в шапке страницв ', max_length=255, blank=True, null=True)
    full_description = RichTextUploadingField ('Полное описание ', blank=True, null=True)

class Banner(models.Model):
    order = models.IntegerField('Порядок отображения', default=1)
    post = models.ForeignKey(Post, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Относится к посту')
    image = models.ImageField('Изображение для банера', upload_to='upload_img/', blank=False)
    small_text = models.CharField('Маленький текст', max_length=255, blank=True, null=True)
    big_text = models.CharField('Большой текст', max_length=255, blank=False, null=True)
    description = models.CharField('Описание', max_length=255, blank=True, null=True)
    url = models.CharField('Ссылка', max_length=255, blank=True, null=True,default='')
    is_active = models.BooleanField('Активен?', default=True)