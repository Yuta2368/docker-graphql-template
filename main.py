import graphene
from fastapi import FastAPI, Request, Response
#from starlette.graphql import GraphQLApp
from starlette_graphene3 import GraphQLApp, make_graphiql_handler

# Grapheneを利用したGraphQLスキーマを作成する
class Query(graphene.ObjectType):
    # 引数nameを持つフィールドhelloを作成
    hello = graphene.String(name=graphene.String(default_value="stranger"))

    # フィールドhelloに対するユーザへ返すクエリレスポンスを定義
    def resolve_hello(self, info, name):
        print("resolve_hello")
        return "Hello" + name

# FastAPIを利用するためのインスタンスを作成
app = FastAPI()
# GraphQLのエンドポイント
schema = graphene.Schema(query=Query)
app.mount("/graphql", GraphQLApp(schema, on_get=make_graphiql_handler()))

# for F-CS-6521547 (To add Vary header)
@app.middleware("http")
async def add_my_headers(request: Request, call_next):
    print("add_my_headers")
    response = await call_next(request)
    response.headers["Vary"] = "Origin"
    return response
