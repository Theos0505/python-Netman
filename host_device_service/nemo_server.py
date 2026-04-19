from flask import Flask, request
# from flask_cors import CORS


nemo_app = Flask(__name__)
# CORS(nemo_app)


# READ THIS: Don't do this. By that I mean, don't use global variables in a flask application.
#            The reason: flask is by nature, multi-threaded. Each REST request will operate on
#            it's own thread. So you could have multiple threads attempting to write global data.
#            That's a bad, bad idea.
#            In the next lessons, we'll be replacing this data with an SQL database. And reads
#            and writes to the database are safe.

# DON'T DO THIS # DON'T DO THIS # DON'T DO THIS !!!
global_hosts = dict()
global_devices = dict()
global_services = dict()


@nemo_app.route("/hosts", methods=["GET", "POST", "PUT", "DELETE"])
def hosts():
    global global_hosts
    if request.method == 'GET':
        return global_hosts
    elif request.method == 'POST':
        global_hosts = request.get_json()
        return {}, 204
    elif request.method == 'PUT':
        hostname = request.args.get('hostname')
        if not hostname:
            return "must provide hostname on PUT", 400
        host = request.get_json()
        global_hosts[hostname] = host
        return {}, 204
    elif request.method == 'DELETE':
        hostname = request.args.get('hostname')
        if not hostname:
            return "must provide hostname on PUT", 400
        del global_hosts[hostname]
        return {}, 204


@nemo_app.route("/devices", methods=["GET", "POST", "PUT", "DELETE"])
def devices():
    global global_devices
    if request.method == "GET":
        return global_devices
    elif request.method == 'POST':
        global_devices = request.get_json()
        return {}, 204
    elif request.method == 'PUT':
        hostname = request.args.get('name')
        if not hostname:
            return "must provide hostname on PUT", 400
        host = request.get_json()
        global_devices[hostname] = host
        return {}, 204
    elif request.method == 'DELETE':
        hostname = request.args.get('name')
        if not hostname:
            return "must provide hostname on PUT", 400
        del global_devices[hostname]
        return {}, 204


@nemo_app.route("/services", methods=["GET", "POST", "PUT", "DELETE"])
def services():
    global global_services
    if request.method == "GET":
        return global_services
    elif request.method == 'POST':
        global_services = request.get_json()
        return {}, 204
    elif request.method == 'PUT':
        hostname = request.args.get('name')
        if not hostname:
            return "must provide hostname on PUT", 400
        host = request.get_json()
        global_services[hostname] = host
        return {}, 204
    elif request.method == 'DELETE':
        hostname = request.args.get('name')
        if not hostname:
            return "must provide hostname on PUT", 400
        del global_services[hostname]
        return {}, 204
