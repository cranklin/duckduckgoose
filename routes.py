from bottle import Bottle, response, request
import ipaddress
import json

from client import ApiClient
from repository import NodeData

app = Bottle()

@app.route('/')
def default():
    return json.dumps({'role': NodeData.role})

@app.route('/nodes')
def get_nodes():
    return json.dumps({'nodes': NodeData.nodes})

@app.route('/nodes', method='POST')
def post_node():
    try:
        try:
            data = request.json
        except:
            raise ValueError

        if data is None:
            raise ValueError
        try:
            newNode = ipaddress.ip_address(data['ip'])
        except (TypeError, KeyError):
            raise ValueError

    except ValueError:
        response.status = 400
        return

    newNodeStr = format(newNode)
    NodeData.addNode({'ip': newNodeStr, 'role': "duck"})
    response.headers['Content-Type'] = 'application/json'
    apiClient = ApiClient()
    apiClient.broadcast_change([NodeData.myIP, newNodeStr])
    return json.dumps(NodeData.nodes)

@app.route('/update', method='POST')
def update():
    try:
        try:
            data = request.json
        except:
            raise ValueError

        if data is None:
            raise ValueError

    except ValueError:
        response.status = 400
        return

    NodeData.setNodes(data)
    response.headers['Content-Type'] = 'application/json'
    return json.dumps(NodeData.nodes)

@app.route('/check/<ip>')
def gossip(ip):
    ipToCheck = ip
    if ipToCheck in NodeData.nodes:
        apiClient = ApiClient()
        response = apiClient.request_status(ipToCheck)
        response.status = response.status_code
        return
    else:
        response.status = 404
        return
