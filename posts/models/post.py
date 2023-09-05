from django.db import models


class Post(models.Model):

    title = models.CharField("Название", max_length=50)
    description = models.TextField("Описание")
    photo = models.ImageField("Фото", upload_to='images/')
    user = models.ForeignKey("users.user", on_delete=models.CASCADE)
    date = models.DateTimeField("Дата создания")

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return f"{self.title}"