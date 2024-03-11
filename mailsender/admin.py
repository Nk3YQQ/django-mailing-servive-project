from django.contrib import admin

from mailsender.models import Client, Mailing, Letter, MailingLog


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("email", "fcs", "comment")
    list_filter = ("email", "fcs")


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ("mailing_time", "periodicity", "status")
    list_filter = ("periodicity", "status")


@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
    list_display = ("title", "body")


@admin.register(MailingLog)
class MailingLogAdmin(admin.ModelAdmin):
    list_display = ("mailing", "status", "server_response")
    list_filter = ("mailing", "status")
