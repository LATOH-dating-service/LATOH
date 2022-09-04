import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.rest_framework.mutation import SerializerMutation
from chat.models import Conversation
from chat.serializers import ConversationSerializer
from django.contrib.auth.models import User

class UserType(DjangoObjectType):
    class Meta:
        model=User

class ConversationType(DjangoObjectType):
    class Meta:
        model=Conversation
        interfaces=(relay.Node,)
        fields=('id','name','code','online')

class ConversationConnection(relay.Connection):
    class Meta:
        node=ConversationType
        
class ConversationCreateMutation(graphene.Mutation):
    class Arguments:
        name=graphene.String(required=True)
        public=graphene.Boolean(required=True)
    
    conversation = graphene.Field(ConversationType)
    
    @classmethod
    def mutate(cls,root,info,name,public):
        conversation=Conversation.objects.create(name=name,public=public)
        return ConversationCreateMutation(conversation=conversation)

class Query(graphene.ObjectType):
    conversations=relay.ConnectionField(ConversationConnection)

    def resolve_conversations(self,info,**kwargs):
        return Conversation.objects.all()

class Mutation(graphene.ObjectType):
    create_conversation=ConversationCreateMutation.Field()