from rest_framework.generics import GenericAPIView ,RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
import json

from .serializers import *

# Create your views here.
class CreateQuiz(GenericAPIView):
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request):
        data = request.data
        ser = self.serializer_class(data=data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        
        return Response({'message':'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)

class ChangeQuiz(RetrieveUpdateAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]

class DeleteQuiz(GenericAPIView):
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def delete(self, request, pk):
        try:
            q = Quiz.objects.get(id = pk)
            q.delete()
            return Response({'message':'Quiz Deleted Successfully'}, status=status.HTTP_200_OK)
        except:
            return Response({'message':'No Quiz with the given ID'}, status=status.HTTP_400_BAD_REQUEST)

class GetQuiz(GenericAPIView):
    serializer_class = QuizSerializer
    permission_classes = [AllowAny]

    def get(self, request):
        result = {}
        result["live"] = []
        result["past"] = []
        result["upcoming"] = []
        today = timezone.now()
        obj = Quiz.objects.all()
        for i in obj:
            self.queryset = i
            ser = self.serializer_class(self.queryset)
            if i.status(today) == "live":
                result["live"].append(ser.data)
            if i.status(today) == "past":
                result["past"].append(ser.data)
            if i.status(today) == "upcoming":
                result["upcoming"].append(ser.data)
            
        return Response(result, status= status.HTTP_200_OK)

class AttemptQuiz(GenericAPIView):
    serializer_class = QuizResponseSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        user = request.user
        quiz = data["quiz"]
        response = str(data["response"][0])
        try:
            q = QuizResponse.objects.get(user=user, quiz_id=quiz)
            return Response({'message':'You have already attempted the quiz'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        except:
            res = QuizResponse.objects.create(quiz_id=quiz, user=user, response=response)
            ser = self.serializer_class(res)

            return Response(ser.data, status=status.HTTP_201_CREATED)

class CreateQuestion(GenericAPIView):
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request):
        data = request.data
        option = data["option"]
        opt = str(option[0])
        data["option"] = opt
        ser = self.serializer_class(data=data)
        if ser.is_valid(raise_exception=True):
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)

        return Response({'message':'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)