from django.db import models


class Collection(models.Model):
    collection_name = models.CharField('Название коллекции', max_length=50)
    collection_description = models.TextField('Описание коллекции')
    collection_picture = models.ImageField('Путь к изображению', upload_to='images/', null=True)
    collection_views = models.IntegerField('Количество просмотров', default=0)

    def __str__(self):
        return f'{self.collection_name[:10]}...'

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'


class Exhibition(models.Model):
    exhibition_name = models.CharField('Название выставки', max_length=50)
    date = models.DateTimeField('Дата выставки')
    duration = models.DateTimeField('Дата окончания')
    coverage = models.IntegerField('Количество человек')

    def __str__(self):
        return f'{self.exhibition_name[:10]}...'

    class Meta:
        verbose_name = 'Выставка'
        verbose_name_plural = 'Выставки'


class Work(models.Model):
    work_name = models.CharField('Название работы', max_length=50)
    work_description = models.TextField('Описание работы')
    work_artist = models.CharField('Художник', max_length=50)
    work_views = models.IntegerField('Количество просмотров', default=0)
    post_date = models.DateField('Дата создания', auto_now=True)

    collection = models.ForeignKey(Collection, blank=True, null=True, on_delete=models.CASCADE)
    exhibition = models.ForeignKey(Exhibition, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.work_name[:10]}...'

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'


class WorkPicture(models.Model):
    picture_source = models.ImageField('Путь к изображению', upload_to='images/')
    is_main = models.BooleanField(default=False)
    work = models.ForeignKey(Work, on_delete=models.CASCADE, related_name='work_pictures')

    class Meta:
        verbose_name = 'Изображение работы'
        verbose_name_plural = 'Изображения работ'
