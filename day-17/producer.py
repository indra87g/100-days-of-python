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


def send(message):
    conn = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    ch = conn.channel()

    ch.queue_declare(queue="notification_queue")

    ch.basic_publish(exchange="", routing_key="notification_queue", body=message)
    print(f"Sent '{message}'")
    conn.close()


if __name__ == "__main__":
    while True:
        message = input("Enter your message: ")
        send(message)
