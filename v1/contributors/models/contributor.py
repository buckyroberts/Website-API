# -*- coding: utf-8 -*-
import uuid

from django.db import models
from thenewboston.models.created_modified import CreatedModified


class Contributor(CreatedModified):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    display_name = models.CharField(max_length=250)
    github_username = models.CharField(blank=True, max_length=250)
    profile_image = models.FileField(blank=True)
    slack_username = models.CharField(blank=True, max_length=250)

    def __str__(self):
        return f'#{self.pk}: {self.display_name}'
