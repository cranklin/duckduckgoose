import threading

class NodeData:
    myIP = ""
    role = ""
    nodes = {}
    lock = threading.Lock()

    @classmethod
    def setNodes(cls, nodes):
        with cls.lock:
            cls.nodes = nodes

    @classmethod
    def addNode(cls, node):
        with cls.lock:
            cls.nodes[node['ip']] = node['role']

    @classmethod
    def setRole(cls, role):
        with cls.lock:
            cls.role = role

    @classmethod
    def removeNode(cls, node):
        with cls.lock:
            cls.nodes.pop(node['ip'])
