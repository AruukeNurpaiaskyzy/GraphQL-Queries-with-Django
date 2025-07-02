import graphene
from graphene_django import DjangoObjectType
from quiz.models import Quizzes, Category, Question, Answer

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name")

class QuizzesType(DjangoObjectType):  # Исправлено имя
    class Meta:
        model = Quizzes
        fields = ("id", "title", "category", "date_created")

class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("title", "quiz")

class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ("question", "answer_text")

class Query(graphene.ObjectType):
    quiz = graphene.String()

    def resolve_quiz(self, info):  # Добавлены аргументы
        return "this is the first question"

schema = graphene.Schema(query=Query)
