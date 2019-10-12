from flask import Flask
from graphene import ObjectType, String, Int, Field, Schema, List
from flask_graphql import GraphQLView
import requests
import json

app = Flask(__name__)
url = 'http://chisel.cloudjiffy.net/contacts/short'

with open('config.json') as json_file:
    cfg = json.load(json_file)
    
class PersonType(ObjectType):
    firstName = String()
    lastName = String()
    age = Int()

class Query(ObjectType):
    hello = String()
    person = Field(PersonType)
    people = List(PersonType)
    contacts = String()

    def resolve_hello(self, args):
        return 'Hello World'

    def resolve_person(self,args):
        return {'firstName':'Sushant', 'lastName':'Agrawal', 'age':56}

    def resolve_people(self, args):
        return [
            {'firstName':'Sushant', 'lastName':'Agrawal', 'age':56},
            {'firstName':'Sushant1', 'lastName':'Agrawal1', 'age':57}
        ]
    
    def resolve_contacts(self,args):
        r = requests.get(url)
        return r.text


schema = Schema(query=Query)

@app.route('/')
def hello_world():
    r = requests.get(url)
    return r.text

app.add_url_rule('/graphql', view_func=GraphQLView.as_view(
    'graphql',
    schema=schema,
    graphiql=True
))
    
if __name__ == '__main__':
    app.run()

