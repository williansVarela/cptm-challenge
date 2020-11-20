import requests, json, os, gc
import pandas as pd
from datetime import datetime, timedelta
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, detail_route
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import renderers
from rest_framework.permissions import AllowAny, BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from core.helpers import process_brand, process_line, process_applicator, csv_in_memory, send_mail
from core.models import Rails, ElectricalNetwork, Line, Station
from django.db.models import Sum, Max, Q, Min, Avg
from api import serializer


class RailsViewSet(viewsets.ModelViewSet):
	permission_classes = (IsAuthenticated,)
	model = Rails
	queryset = model.objects.all()
	serializer_class = serializer.RailsSerializer
	pagination_class = None
	http_method_names = ['post']

	@detail_route(renderer_classes=[renderers.StaticHTMLRenderer], methods=['post'])
	def image(self, request, *args, **kwargs):
		line_name = self.request.query_params.get('line', None)
		station_name = self.request.query_params.get('station', None)

		return Response({'Imagem processada com sucesso': 'Imagem Processada Com Sucesso'}, status=HTTP_200_OK)



class ElectricalNetworkViewSet(viewsets.ModelViewSet):
	permission_classes = (IsAuthenticated,)
	model = ElectricalNetwork
	queryset = model.objects.all()
	serializer_class = serializer.ElectricalNetworkSerializer
	pagination_class = None
	http_method_names = ['post']

	@detail_route(renderer_classes=[renderers.StaticHTMLRenderer], methods=['post'])
	def image(self, request, *args, **kwargs):
		line_name = self.request.query_params.get('line', None)
		station_name = self.request.query_params.get('station', None)

		line = Line.objects.get(name=line_name)
		station = Station.objects.get(name=station_name)

		return Response({'Imagem processada com sucesso': 'Imagem Processada Com Sucesso'}, status=HTTP_200_OK)
