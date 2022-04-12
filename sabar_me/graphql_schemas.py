import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from .models import Article as ArticleModel

class Article(SQLAlchemyObjectType):
    class Meta:
        model = ArticleModel

class Query(graphene.ObjectType):
    ping = graphene.String()

    article = graphene.Field(Article)
    articles = graphene.List(Article)

    def resolve_articles(self, info):
        query = Article.get_query(info)
        return query.all()

    def resolve_ping(self, info):
        return "Sora"

# class Mutation(graphene.ObjectType):
#     pass

schema = graphene.Schema(
    query=Query#, mutation=Mutation
)
