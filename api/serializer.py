from rest_framework import routers, serializers
from django.db.models import Prefetch
from core.models import User
from core.serializer import LineSerializer, StationSerializer
from core import models


class RailsSerializer(serializers.ModelSerializer):
	line = LineSerializer(read_only=True)
	line_id = serializers.IntegerField(write_only=True)
	station = StationSerializer(read_only=True)
	station_id = serializers.IntegerField(write_only=True)

	def __init__(self, *args, **kwargs):
		super(RailsSerializer, self).__init__(*args, **kwargs)
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
		model = models.Rails
		fields = ('pk', 'temperature', 'station', 'station_id', 'line', 'line_id')


class ElectricalNetworkSerializer(serializers.ModelSerializer):
	line = LineSerializer(read_only=True)
	line_id = serializers.IntegerField(write_only=True)
	station = StationSerializer(read_only=True)
	station_id = serializers.IntegerField(write_only=True)

	def __init__(self, *args, **kwargs):
		super(ElectricalNetworkSerializer, self).__init__(*args, **kwargs)
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
		model = models.ElectricalNetwork
		fields = ('pk', 'temperature', 'station', 'station_id', 'line', 'line_id')

