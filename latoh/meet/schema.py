import graphene
from graphene_django import DjangoObjectType

from .models import Meet

class MeetType(DjangoObjectType):
    class Meta:
        model = Meet
        fields = "__all__" #("id", "question_text")

class Query(graphene.ObjectType):
    meets = graphene.List(MeetType)
    meet_by_id = graphene.Field(MeetType, id=graphene.String())

    def resolve_meets(root, info, **kwargs):
        # Querying a list
        return Meet.objects.all()

    def resolve_meet_by_id(root, info, id):
        # Querying a single question
        return Meet.objects.get(pk=id)