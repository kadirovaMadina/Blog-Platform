from django.db import models


class Comment(models.Model):

    text = models.TextField("Комментарий")
    user = models.ForeignKey("users.user", on_delete=models.CASCADE)
    post = models.ForeignKey("posts.post", on_delete=models.CASCADE)
    date = models.DateTimeField("Дата создания")

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return f"{self.text}"