from django.shortcuts import render
from rest_framework import filters
from rest_framework import generics
from .models import Question,Choice
from .serializers import QuestionSerializer,ChoiceSerializer
from .paginations import CustomPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])

class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    search_fields = ['question_text','author','choice__choice_text']
    filter_backends = (DynamicSearchFilter,)
    serializer_class = QuestionSerializer
    pagination_class = CustomPagination
    # permission_classes = [IsAuthenticated]

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    filter_backends = (DynamicSearchFilter,)
    serializer_class = ChoiceSerializer
    pagination_class = CustomPagination
    # permission_classes = [IsAuthenticated]

# class QuestionsAPIView(generics.ListCreateAPIView):
#     queryset = Question.objects.all()
#     search_fields = ['question_text','author','choice__choice_text']
#     filter_backends = (DynamicSearchFilter,)
#     serializer_class = QuestionSerializer
#     pagination_class = CustomPagination
#     permission_classes = [IsAuthenticated]


# class QuestionsAPIView(generics.ListCreateAPIView):
#     queryset = Question.objects.all()
#     search_fields = ['question_text','author','choice__choice_text']
#     filter_backends = (filters.SearchFilter,)
#     serializer_class = QuestionSerializer

# class QuestionsAPIView(generics.ListCreateAPIView):
#     queryset = Question.objects.filter(question_text__icontains="php")
#     search_fields = ['question_text','author','choice__choice_text']
#     filter_backends = (filters.SearchFilter,)
#     serializer_class = QuestionSerializer

# class QuestionsAPIView(generics.ListCreateAPIView):
#     queryset = Question.objects.filter(question_text__istartswith="what")
#     search_fields = ['question_text','author','choice__choice_text']
#     filter_backends = (filters.SearchFilter,)
#     serializer_class = QuestionSerializer
#     pagination_class = CustomPagination



