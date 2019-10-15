import sys
from helloPackage import helloHelper
app = helloHelper.app

# print(sys.path)
from HelloHelper2 import myMethod as m
m()
# import flask.GqlHelper
#from flask import HelloHelper2 as h2
# h2.myMethod()
if __name__ == '__main__':
    app.run()