from django.core.mail import EmailMessage

from django_extensions.db.models import TimeStampedModel
from django.db import models

import uuid


class DeletableManager(models.manager):
    pass


class Datation(TimeStampedModel):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    deleted = models.BooleanField(default=False)
    objects = DeletableManager()
    h_objects = models.Manager()


class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data['email_subject'], 
            body=data['email_body'],
            to=[data['to_email']]
        )
        email.send()