import uuid
import rabbitpy
from flask import Flask, request, jsonify, g

app = Flask(__name__)

CONNECT_STRING = 'amqp://guest:guest@rabbitmq:5672/%2f'


def get_connection():
    connection = getattr(g, 'connection', None)
    if connection is None:
        connection = g._connection = rabbitpy.Connection(CONNECT_STRING)
    return connection


def get_channel():
    channel = getattr(g, 'channel', None)
    if channel is None:
        channel = g.channel = get_connection().channel()
    return channel


@app.teardown_appcontext
def close_rabbit(error):
    if hasattr(g, 'channel'):
        g.channel.close()
    if hasattr(g, 'connection'):
        g.connection.close()


@app.route("/", methods=['POST'])
def create_queue():
    if request.method == 'POST':
        channel = get_channel()
        name = uuid.uuid4()
        queue = rabbitpy.Queue(channel, str(name))
        queue.declare()
    return jsonify(queue=str(name))


@app.route("/<project>", methods=['GET', 'PUT'])
def putget(project):
    channel = get_channel()
    if request.method == 'PUT':
        job = request.get_json()
        message = rabbitpy.Message(channel, job)
        message.publish('', project)
        data = job

    if request.method == 'GET':
        queue = rabbitpy.Queue(channel, project)
        message = queue.get()
        if message is not None:
            data = message.json()
            message.ack()
        else:
            return jsonify({}), 204
    return jsonify(data)
