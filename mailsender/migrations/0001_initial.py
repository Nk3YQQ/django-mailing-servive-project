# Generated by Django 5.0.3 on 2024-03-11 12:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="Электронная почта"
                    ),
                ),
                ("fcs", models.CharField(max_length=150, verbose_name="ФИО")),
                (
                    "comment",
                    models.TextField(blank=True, null=True, verbose_name="Комментарий"),
                ),
            ],
            options={
                "verbose_name": "клиент",
                "verbose_name_plural": "клиенты",
            },
        ),
        migrations.CreateModel(
            name="Letter",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100, verbose_name="Тема письма")),
                ("body", models.CharField(verbose_name="Тело письма")),
            ],
            options={
                "verbose_name": "письмо",
                "verbose_name_plural": "письма",
            },
        ),
        migrations.CreateModel(
            name="Mailing",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("mailing_time", models.DateTimeField(verbose_name="Время рассылки")),
                (
                    "periodicity",
                    models.CharField(
                        choices=[
                            ("daily", "Раз в день"),
                            ("weekly", "Раз в неделю"),
                            ("monthly", "Раз в месяц"),
                        ],
                        max_length=15,
                        verbose_name="Периодичность",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("finished", "Завершена"),
                            ("created", "Создана"),
                            ("started", "Запущена"),
                        ],
                        max_length=15,
                        verbose_name="Статус",
                    ),
                ),
            ],
            options={
                "verbose_name": "рассылка",
                "verbose_name_plural": "рассылки",
            },
        ),
        migrations.CreateModel(
            name="MailingLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "last_attempt_time",
                    models.DateTimeField(
                        auto_now=True,
                        null=True,
                        verbose_name="Дата и время последней попытки",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("finished", "Завершена"),
                            ("created", "Создана"),
                            ("started", "Запущена"),
                        ],
                        max_length=15,
                        verbose_name="Статус",
                    ),
                ),
                (
                    "server_response",
                    models.TextField(
                        blank=True, null=True, verbose_name="Ответ почтового сервера"
                    ),
                ),
                (
                    "mailing",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mailsender.mailing",
                        verbose_name="Рассылка",
                    ),
                ),
            ],
            options={
                "verbose_name": "лог рассылки",
                "verbose_name_plural": "логи рассылки",
            },
        ),
    ]
