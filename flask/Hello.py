import sys
from helloPackage import helloHelper
app = helloHelper.app

# print(sys.path)
from HelloHelper2 import myMethod as m
m()
if __name__ == '__main__':
    app.run()