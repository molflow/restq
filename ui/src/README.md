# Restq
Restq is a multipurpose FIFO-queue for JSON-objects served with on Rest API. Limited use is free of charge. The maximum size of a queue is 1,000 kbytes. Queues are removed after 7 days of inactivity.

# Usage
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

# Example implementations
## Batch processing system
The user sends JSON-objects to a queue. One or many worker clients pulls the queue and receive sufficient data to process a job.

    {
      input: https://www.example.com/dataset/1
      output: https://www.exaple.com/result/1
    }

The worker client get the input data from the input url, processes the information and posts back the result to the output url.

## Peer-to-peer Chat client
A communication channel is set up by sharing the peers queues. Peer A posts a message to Peer B on Peer B's queue and vice versa.
