# -*- coding: utf-8 -*-
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from ..models.opening import Opening


class OpeningSerializer(ModelSerializer):
    reports_to = SerializerMethodField()

    class Meta:
        fields = (
            'active',
            'created_date',
            'description',
            'eligible_for_task_points',
            'modified_date',
            'pay_per_day',
            'pk',
            'reports_to',
            'responsibilities',
            'skills',
            'team',
            'title',
        )
        model = Opening
        read_only_fields = 'created_date', 'modified_date'

    @staticmethod
    def get_reports_to(opening):
        return [team_member.pk for team_member in opening.team.team_members.all()]
