from django.db import models
from pytils.translit import slugify
from ckeditor_uploader.fields import RichTextUploadingField

class ImageTag(models.Model):
    name = models.CharField(max_length=50, blank=False)

    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        super(ImageTag, self).save(*args, **kwargs)

class Image(models.Model):
    image = models.ImageField('Изображение', upload_to='upload_img/', blank=False)
    tag = models.ForeignKey(ImageTag, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Тэг')
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
    icon = models.CharField('Иконка', max_length=50, blank=True, null=True)
    short_description = models.CharField('Короткое описание ',max_length=255, blank=True, null=True)
    full_description = RichTextUploadingField ('Полное описание ', blank=True, null=True)