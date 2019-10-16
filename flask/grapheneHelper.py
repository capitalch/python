from flask import Flask
from graphene import ObjectType, String, Int, Float, Field, Schema, List
from graphene import types
from flask_graphql import GraphQLView
import requests
import simplejson as json
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)


class PersonType(ObjectType):
    firstName = String()
    lastName = String()
    helloName = String()
    
    def resolve_helloName(parent, info):
        print(parent)
        return 'x'

class Query(ObjectType):
    hello = String()
    helloWithParam = String(name = String())
    person = Field(PersonType)
   

    def resolve_hello(parent, info):
        return 'Hello world'
    def resolve_helloWithParam(parent, info, name):
        return f'Hello {name}'
    def resolve_person(parent, info):
        return {'firstName':'a', 'lastName':'b'}
    

schema = Schema(query = Query)
app.add_url_rule('/graphql', view_func=GraphQLView.as_view(
    'graphql',
    schema=schema,
    graphiql=True
))

@app.route('/')
def hello_world():
    r = requests.get('http://chisel.cloudjiffy.net/contacts/short')
    return (r.text)

# app.add_url_rule('/graphql', view_func=GraphQLView.as_view(
#     'graphql',
#     schema=schema,
#     graphiql=True
# ))