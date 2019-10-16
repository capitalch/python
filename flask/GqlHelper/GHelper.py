from flask import Flask
from graphene import ObjectType, String, Int, Float, Field, Schema, List
from flask_graphql import GraphQLView
import requests
import simplejson as json
import psycopg2
from psycopg2.extras import RealDictCursor


app = Flask(__name__)

url = 'http://chisel.cloudjiffy.net/contacts/short'

with open('config.json') as json_file:
    cfg = json.load(json_file)

sql = '''
set search_path to test; 
with RECURSIVE cte 
    as ( select m."id", m."accCode", m."parentId", t."amount" from "AccTran" t 
        join "AccM" m on t."accCode" = m."accCode" 
    union select a.id,a."accCode", a."parentId"
        , ( cte."amount") as "amount" from "AccM" a join cte on cte."parentId" = a.id ) 
select id, "accCode", "parentId", sum(amount) as amount
    from cte 
        group by id, "accCode", "parentId" order by cte.id
'''

try:
    connection = psycopg2.connect(user=cfg['trackTest']['user'], password=cfg['trackTest']['password'], host=cfg['trackTest']['host'], port=cfg['trackTest']['port'], database=cfg['trackTest']['database'])
    # cursor = connection.cursor(cursor_factory=RealDictCursor)
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
    
class PersonType(ObjectType):
    firstName = String()
    lastName = String()
    age = Int()

class AccountType(ObjectType):
    id = Int()
    accCode = String()
    parentId = Int()
    amount = Float()

class Query(ObjectType):
    hello = String()
    person = Field(PersonType)
    people = List(PersonType)
    contacts = String()
    accounts = List(AccountType)
    personById =  Field(PersonType, id=Int(required=True)) #List(AccountType, id=Int(required=True))

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
    
    def resolve_accounts(self, args):
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute(sql)
        rows = cursor.fetchall()
        j = json.dumps(rows, indent=2)
        list = json.loads(j)
        cursor.close()
        return(list)
    
    def resolve_personById(self, args, id):
        return {'firstName':'Ujjal', 'lastName':'Saha', 'age':50}

schema = Schema(query=Query)

@app.route('/')
def hello_world():
    r = requests.get(url)
    return (r.text)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view(
    'graphql',
    schema=schema,
    graphiql=True
))