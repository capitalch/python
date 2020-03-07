from mydata.bsData import data1
import copy
# print(data)

def getNodeDict():
    nodeDict = {}
    for item in data1:
        nodeDict[item['id']] = {
            'key': item['id'],
            'data': {
                'name': item['accCode'],
                'amount': item['amount']
            },
            'children': item['children']
        }
    return nodeDict

def getNode(id):
    return copy.deepcopy(nodeDict[id])

def setDeepChild(id):
    item = nodeDict[id]
    temp = []
    if item['children']:
        for it in item['children']:
            temp.append(getNode(it))
    item['temp'] = temp

nodeDict = getNodeDict()
for id in nodeDict:
    setDeepChild(id)
print(nodeDict)