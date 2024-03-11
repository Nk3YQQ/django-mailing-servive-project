from django.db import models

NULLABLE = {"blank": True, "null": True}


class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    fcs = models.CharField(max_length=150, verbose_name="ФИО")
    comment = models.TextField(**NULLABLE, verbose_name="Комментарий")

    def __str__(self):
        return f"{self.fcs}:{self.email}"

    class Meta:
        verbose_name = "клиент"
        verbose_name_plural = "клиенты"


class Periodicity(models.TextChoices):
    DAILY = "daily", "Раз в день"
    WEEKLY = "weekly", "Раз в неделю"
    MONTHLY = "monthly", "Раз в месяц"
    __empty__ = 'Выберите период рассылки'


class Status(models.TextChoices):
    FINISHED = "finished", "Завершена"
    CREATED = "created", "Создана"
    STARTED = "started", "Запущена"
    __empty__ = 'Выберите тип статуса'


class Mailing(models.Model):
    mailing_time = models.DateTimeField(verbose_name="Время рассылки")
    periodicity = models.CharField(
        max_length=15, choices=Periodicity.choices, verbose_name="Периодичность"
    )
    status = models.CharField(
        max_length=15, choices=Status.choices, verbose_name="Статус"
    )

    def __str__(self):
        return f"{self.mailing_time} - {self.periodicity} - {self.status}"

    class Meta:
        verbose_name = "рассылка"
        verbose_name_plural = "рассылки"


class Letter(models.Model):
    title = models.CharField(max_length=100, verbose_name="Тема письма")
    body = models.CharField(verbose_name="Тело письма")

    def __str__(self):
        return f"{self.title} ({self.body[:30]})"

    class Meta:
        verbose_name = "письмо"
        verbose_name_plural = "письма"


class MailingLog(models.Model):
    mailing = models.ForeignKey(
        Mailing, on_delete=models.CASCADE, verbose_name="Рассылка"
    )
    last_attempt_time = models.DateTimeField(
        auto_now=True, null=True, verbose_name="Дата и время последней попытки"
    )
    status = models.CharField(
        max_length=15, choices=Status.choices, verbose_name="Статус"
    )
    server_response = models.TextField(
        **NULLABLE, verbose_name="Ответ почтового сервера"
    )

    def __str__(self):
        return f"[{self.last_attempt_time}] {self.mailing} - {self.status}: {self.server_response}"

    class Meta:
        verbose_name = "лог рассылки"
        verbose_name_plural = "логи рассылки"
