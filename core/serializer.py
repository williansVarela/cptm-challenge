from rest_framework import routers, serializers
from core.models import Line, Station
from django.db.models import Prefetch


class LineSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(LineSerializer, self).__init__(*args, **kwargs)
        request = self.context.get("request")
        if request and request.query_params.get('fields'):
            fields = request.query_params.get('fields')
            if fields:
                fields = fields.split(',')
                allowed = set(fields)
                existing = set(self.fields.keys())
                for field_name in existing - allowed:
                    self.fields.pop(field_name)

    class Meta:
        model = Line
        fields = ('pk', 'name', 'humanized_name', 'number', 'author')


class StationSerializer(serializers.ModelSerializer):
    line = LineSerializer(read_only=True)
    line_id = serializers.IntegerField(write_only=True)

    def __init__(self, *args, **kwargs):
        super(StationSerializer, self).__init__(*args, **kwargs)
        request = self.context.get("request")
        if request and request.query_params.get('fields'):
            fields = request.query_params.get('fields')
            if fields:
                fields = fields.split(',')
                allowed = set(fields)
                existing = set(self.fields.keys())
                for field_name in existing - allowed:
                    self.fields.pop(field_name)

    class Meta:
        model = Station
        fields = ('pk', 'name', 'line', 'line_id')
