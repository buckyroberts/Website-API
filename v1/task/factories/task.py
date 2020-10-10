# -*- coding: utf-8 -*-
import factory
from factory.django import DjangoModelFactory

from ..models import Task


class TaskFactory(DjangoModelFactory):
    title = factory.Faker('pystr', max_chars=250)
    contributor = factory.SubFactory('v1.team.factories.ContributorFactory')
    repository = factory.Faker('pystr', max_chars=250)
    amount = factory.Faker('pyint')

    class Meta:
        model = Task
