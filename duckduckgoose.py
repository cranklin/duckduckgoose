from bottle import Bottle
import ipaddress
import threading

from client import ApiClient
from repository import NodeData
from routes import app

class DuckDuckGoose:

    def __init__(self, hostIP, seedIP):
        self.app = Bottle()
        self.app.merge(app)
        NodeData.myIP = hostIP

        if seedIP is None:
            NodeData.setRole("goose")
            NodeData.setNodes({hostIP : NodeData.role})
        else:
            NodeData.setRole("duck")
            apiClient = ApiClient()
            apiClient.join_cluster(seedIP, hostIP)
        self.app.run(host = hostIP, port = 8080)

    def pick_goose(self):
        ips = [ipaddress.ip_address(ip) for ip in NodeData.nodes.keys()].sort()
        print(ips[0])
        return ips

    def ping_nodes(self):
        #TODO: spin up thread to ping nodes in cluster
        pass

if __name__ == "__main__":
    pass
