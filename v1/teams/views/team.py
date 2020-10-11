# -*- coding: utf-8 -*-
from rest_framework import viewsets

from v1.third_party.rest_framework.permissions import IsStaffOrReadOnly
from ..models import Team
from ..serializers import TeamSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects \
        .prefetch_related('teamcontributor_set') \
        .order_by('created_date') \
        .all()
    serializer_class = TeamSerializer
    pagination_class = None
    permission_classes = [IsStaffOrReadOnly]
