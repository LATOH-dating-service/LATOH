import graphene
from meet.schema import Query as MeetQuery

class Query(
    MeetQuery,
    graphene.ObjectType
    ):
    hello = graphene.String(default_value="Hi!")

schema = graphene.Schema(query=Query)