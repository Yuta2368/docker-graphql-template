import graphene
from fastapi import FastAPI, Request, Response
from starlette_graphene3 import GraphQLApp, make_graphiql_handler

# Create GraphQL schema using Grapheneを利用したGraphQLスキーマを作成する
class Query(graphene.ObjectType):
    # Create field "hello" w/ argument "name"
    hello = graphene.String(name=graphene.String(default_value="stranger"))

    # Define a query response to be returned for field "hello"
    def resolve_hello(self, info, name):
        print("resolve_hello")
        return "Hello" + name

# Create FastAPI instance
app = FastAPI()
# GraphQL endopoint
schema = graphene.Schema(query=Query)
app.mount("/graphql", GraphQLApp(schema, on_get=make_graphiql_handler()))

# for F-CS-6521547 (To add Vary header)
@app.middleware("http")
async def add_my_headers(request: Request, call_next):
    print("add_my_headers")
    response = await call_next(request)
    response.headers["Vary"] = "Origin"
    return response
