from unittest.mock import patch, Mock
import json
import pytest
from relaxq.relaxq import app as myapp
from relaxq.relaxq import get_connection, get_channel, close_rabbit


@pytest.fixture
def app():
    return myapp


@patch('relaxq.relaxq.get_channel')
@patch('relaxq.relaxq.rabbitpy.Queue')
@patch('uuid.uuid4')
def test_create_project(uuid, queue, channel, client):
    uuid.return_value = 'hash_123'
    resp = client.post('/')
    assert resp.json == {'queue': 'hash_123'}


@patch('relaxq.relaxq.get_channel')
@patch('relaxq.relaxq.rabbitpy.Message')
def test_project_put(message, channel, client):
    data = {'job': 1}
    header = {'Content-Type': 'application/json'}
    resp = client.put('/hash_321', headers=header, data=json.dumps(data))
    assert resp.status_code == 200
    assert resp.json == data


@patch('relaxq.relaxq.get_channel')
@patch('relaxq.relaxq.rabbitpy.Queue')
def test_project_get_empty(queue, channel, client):
    msg = Mock()
    msg.get.return_value = None
    queue.return_value = msg
    resp = client.get('/hash_321')
    queue.get.ack.assert_not_called()
    assert resp.status_code == 204


@patch('relaxq.relaxq.get_channel')
@patch('relaxq.relaxq.rabbitpy.Queue')
def test_project_get_data(queue, channel, client):
    data = {'job': 1}
    message_obj = Mock()
    message_obj.json.return_value = data
    msg = Mock()
    msg.get.return_value = message_obj
    queue.return_value = msg
    resp = client.get('/hash_321')
    assert resp.status_code == 200
    assert resp.json == data


@patch('relaxq.relaxq.rabbitpy.Connection')
def test_connection(Connection, client):
    con1 = get_connection()
    con2 = get_connection()
    assert con1.id == con2.id


@patch('relaxq.relaxq.rabbitpy.Connection')
def test_channel(Connection, client):
    ch1 = get_channel()
    ch2 = get_channel()
    assert ch1.id == ch2.id


@patch('relaxq.relaxq.g')
def test_teardown(g):
    close_rabbit(None)
    assert g.channel.close.call_count == 1
    assert g.connection.close.call_count == 1
