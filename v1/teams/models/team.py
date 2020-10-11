# -*- coding: utf-8 -*-
import uuid

from django.db import models
from thenewboston.models.created_modified import CreatedModified

from v1.contributors.models import Contributor


class Team(CreatedModified):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    contributors = models.ManyToManyField(Contributor, through='TeamContributor')

    title = models.CharField(max_length=250)

    def __str__(self):
        return f'#{self.pk}: {self.title}'


class TeamContributor(CreatedModified):
    team = models.ForeignKey('Team', on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)

    is_lead = models.BooleanField(default=False)
    pay_per_day = models.PositiveIntegerField()

    class Meta:
        unique_together = (
            ('team', 'contributor'),
        )