# -*- coding: utf-8 -*-
"""
Project Serializers
"""

from __future__ import unicode_literals

from tasking.models import Project

from tasking.serializers.base import GenericForeignKeySerializer


class ProjectSerializer(GenericForeignKeySerializer):
    """
    Project serializer class
    """
    # pylint: disable=too-few-public-methods
    class Meta(object):
        """
        Meta options for ProjectSerializer
        """
        model = Project
        fields = [
            'id',
            'name',
            'tasks',
            'created',
            'modified',
            'target_content_type',
            'target_id',
        ]
