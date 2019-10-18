from flask import Flask
from graphene import ObjectType, String, Int, Float, Field, Schema, List, Mutation, Boolean
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

class Person(ObjectType):
    name = String()

class CreatePerson(ObjectType): #Mutation
    class Arguments:
        name = String()

    ok = Boolean()
    person = Field(lambda: Person)

    def mutate(root, info, name):
        person = Person(name=name)
        ok = True
        return CreatePerson(person=person, ok=ok)
    
class Idea(ObjectType):
    mname= String()


class MyMutations(ObjectType):
    createPerson = Field(CreatePerson) #CreatePerson.Field()
    createIdea = Field(Idea)

    def resolve_createIdea(parent, info):
        return "This is the idea"

schema = Schema(query = Query, mutation = MyMutations)
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