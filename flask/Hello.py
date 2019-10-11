from flask import Flask
import graphene
from flask_graphql import GraphQLView

app = Flask(__name__)

class Query(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(self, args):
        return 'Hello World'

schema = graphene.Schema(query=Query)

@app.route('/')
def hello_world():
    return 'Hello World1'

app.add_url_rule('/graphql', view_func=GraphQLView.as_view(
    'graphql',
    schema=schema,
    graphiql=True
))
    
if __name__ == '__main__':
    app.run()