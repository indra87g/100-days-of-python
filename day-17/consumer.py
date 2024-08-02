"""
Day 17 - RabbitMQ Notification Queue

Getting Started:
* Install the latest version of RabbitMQ Server. On Windows: 'scoop install rabbitmq'
* Install pika by running 'pip install pika'
* Run producer by running 'python producer.py'
* Run consumer by running 'python consumer.py'
* Send some message from producer, and receive it from consumer
"""

import pika


def callback(ch, method, properties, body):
    print(f" [X] Producer: {body.decode()}")


def consume():
    conn = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    ch = conn.channel()

    ch.queue_declare(queue="notification_queue")

    ch.basic_consume(
        queue="notification_queue", on_message_callback=callback, auto_ack=True
    )

    print(f" [*] Waiting for messages from producer. press CTRL+C to exit.")
    ch.start_consuming()


if __name__ == "__main__":
    while True:
        consume()
