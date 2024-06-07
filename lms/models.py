from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=255, verbose_name='название')
    preview = models.ImageField(upload_to='lms/', **NULLABLE)
    description = models.TextField(max_length=250, verbose_name='описание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=255, verbose_name='название')
    description = models.TextField(max_length=250, verbose_name='описание')
    video = models.FileField(upload_to='lms/', **NULLABLE)
    preview = models.ImageField(upload_to='lms/', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='курс')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
