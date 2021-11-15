import json
import requests

from repository import NodeData

class ApiClient:

    def request_status(self, ip):
        url = "http://" + ip + ":8080/nodes"
        try:
            response = requests.get(url)
        except requests.exceptions.RequestException as re:
            print(re)
            pass
        return response

    def request_nodes(self, seed):
        url = "http://" + seed + ":8080/nodes"
        try:
            response = requests.get(url)
        except requests.exceptions.RequestException as re:
            print(re)
            pass
        return response

    def join_cluster(self, seed, hostIP):
        url = "http://" + seed + ":8080/nodes"
        data = {'ip': hostIP}
        try:
            response = requests.post(url, json=data)
            if response.status_code == 200:
                nodes = response.json()
                NodeData.setNodes(nodes)
        except requests.exceptions.RequestException as re:
            print(re)
            pass

    def broadcast_change(self, ignore):
        for ip in list(NodeData.nodes):
            if ip in ignore:
                continue
            url = "http://" + ip + ":8080/update"
            data = NodeData.nodes
            try:
                response = requests.post(url, json=data)
            except requests.exceptions.RequestException as re:
                print(re)
                pass

if __name__ == "__main__":
    pass
