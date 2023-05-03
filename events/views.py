from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from django.utils import timezone
from config.permissions import ReadOnly, ReadOnlyIfAuthenticated
from .models import *
from .serializers import *

# ViewSets

class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
    permission_classes = [ReadOnly | IsAdminUser, ]
    
    event_registration_serializer_class = EventRegistrationsSerializer
    event_registration_model = EventRegistrations
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    @action(detail=True, methods=['post'], serializer_class=None, permission_classes=[IsAuthenticated, ])
    def registration(self, request, pk=None):
        """ Зарегестрироваться на конкретное мероприятие пользователю или группе пользователей """
        current_user = request.user
        serializer = self.event_registration_serializer_class(data={"event_id": pk, "user_id": current_user.id})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    @registration.mapping.delete
    def delete_registration(self, request, pk=None):
        """ Удалить регистрацию на конкретное мероприятие пользователю или группе пользователей """
        current_user = request.user
        event_registration = get_object_or_404(self.event_registration_model, event_id=pk, user_id=current_user.id)
        event_registration.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['post'], permission_classes=[IsAdminUser, ])
    def invite(self, request, pk=None):
        """ Отправить приглашение на конкретное мероприятие пользователю или группе пользователей """
        return Response({})
    
    @action(detail=True, methods=['get'])
    def invitations(self, request, pk=None):
        """ Получить список приглашений на конкретное мероприятие """
        return Response({})
        
    @action(detail=True, methods=['get'])
    def guestlist(self, request, pk=None):
        """ Получить список пользователей, принявших приглашение на конкретное мероприятие """
        event = self.get_object()
        return Response(event.visitors_list, status=status.HTTP_200_OK)
    

class PrivateEventsViewSet(EventsViewSet):
    queryset = PrivateEvents.objects.all()
    serializer_class = PrivateEventsSerializer
    permission_classes = [ReadOnlyIfAuthenticated | IsAdminUser, ]
    
    event_registration_serializer_class = PrivateEventRegistrationsSerializer
    event_registration_model = PrivateEventRegistrations
    
    
class EventsRegistrationsViewSet(viewsets.ModelViewSet):
    queryset = EventRegistrations.objects.all()
    serializer_class = EventRegistrationsSerializer
    permission_classes = [ReadOnly | IsAuthenticated, ]
    

class PrivateEventsRegistrationsViewSet(viewsets.ModelViewSet):
    queryset = PrivateEventRegistrations.objects.all()
    serializer_class = PrivateEventRegistrationsSerializer
    permission_classes = [ReadOnly | IsAdminUser, ]
        

class EventVenuesViewSet(viewsets.ModelViewSet):
    queryset = EventVenues.objects.all()
    serializer_class = EventVenuesSerializer
    permission_classes = [ReadOnly | IsAdminUser, ]


class EventTypesViewSet(viewsets.ModelViewSet):
    queryset = EventTypes.objects.all()
    serializer_class = EventTypesSerializer
    permission_classes = [ReadOnly | IsAdminUser, ]