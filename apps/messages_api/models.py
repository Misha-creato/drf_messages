from django.db import models


class Message(models.Model):
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=256,
    )
    text = models.TextField(
        verbose_name='Текст',
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = [
            '-created_at',
        ]
        db_table = 'messages'
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
