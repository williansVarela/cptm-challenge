import requests
from datetime import datetime, timedelta
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework import renderers
from rest_framework.permissions import AllowAny, BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from core.models import Rails, ElectricalNetwork, Line, Station
from django.db.models import Sum, Max, Q, Min, Avg
from api.serializer import RailsSerializer, ElectricalNetworkSerializer


class RailsViewSet(viewsets.ModelViewSet):
    model = Rails
    queryset = model.objects.all()
    serializer_class = RailsSerializer
    pagination_class = None
    http_method_names = ['get', 'post']

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer], methods=['post'])
    def image(self, request, *args, **kwargs):
        return Response({'Imagem processada com sucesso': 'Imagem Processada Com Sucesso'}, status=HTTP_200_OK)


class ElectricalNetworkViewSet(viewsets.ModelViewSet):
    model = ElectricalNetwork
    queryset = model.objects.all()
    serializer_class = ElectricalNetworkSerializer
    pagination_class = None
    http_method_names = ['get', 'post']

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer], methods=['post'])
    def image(self, request, *args, **kwargs):
        return Response({'Imagem processada com sucesso': 'Imagem Processada Com Sucesso'}, status=HTTP_200_OK)
