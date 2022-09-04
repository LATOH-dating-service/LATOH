import graphene
from meet.schema import Query as MeetQuery
from chat.schema import (
    Query as ChatQuery,
    Mutation as ChatMutation
)

class Query(
    MeetQuery,
    ChatQuery,
    graphene.ObjectType
    ):
    pass

class Mutation(
    ChatMutation,
    graphene.ObjectType
    ):
    pass

schema = graphene.Schema(query=Query,mutation=Mutation)