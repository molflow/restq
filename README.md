[![Build Status](https://travis-ci.org/molflow/restq.svg?branch=master)](https://travis-ci.org/molflow/restq)
[![Coverage Status](https://coveralls.io/repos/github/molflow/restq/badge.svg)](https://coveralls.io/github/molflow/restq)

# restQ
A restful and persistent service for queuing JSON-objects.

## Hosted solution

A hosted service is running at http://restq.io. Feel free to use it for your applications. Usage is free for queues smaller than 1 Mb. Queues inactive for longer than 7 days will be removed.

### Usage
To create a queue:

    curl -X POST http://restq.io/rest_api/
    {
        "queue": "8919fdd4-4363-4d9e-84b4-5deb078561f3"
    }
The "queue" field contains your newly created queue

Post data into the queue:

    curl -H "Content-Type: application/json" \
        -X PUT \
        -d '{"any_key": "any_data"}' \
        http://restq.io/rest_api/8919fdd4-4363-4d9e-84b4-5deb078561f3

Retrieve data from the queue:

    curl http://restq.io/rest_api/8919fdd4-4363-4d9e-84b4-5deb078561f3
    {
        "any_key": "any_data"
        "message_id": "8de52879-90c6-488d-a6df-90696807afa3"
    }


The queue will return http-code 204 if there are no more objects in the queue.

## Simple service setup
To run an instance in your own network. Simply use the docker-compose.yml file at the top of the repository.

    docker-compose up

## Example implementations

### Batch processing system
The user sends JSON-objects to a queue. One or many worker clients pulls the queue and receive sufficient data to process a job.

    {
      input: https://www.example.com/dataset/1
      output: https://www.exaple.com/result/1
    }

The worker client get the input data from the input url, processes the information and posts back the result to the output url.

### Peer-to-peer Chat client
A communication channel is set up by sharing the peers queues. Peer A posts a message to Peer B on Peer B's queue and vice versa.
