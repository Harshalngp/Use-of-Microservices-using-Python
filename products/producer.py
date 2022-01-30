
import pika, json

params = pika.URLParameters('amqps://otgjokqx:QWDg3rQONAe5dDy5T5euI6JC4uyWpKUJ@hummingbird.rmq.cloudamqp.com/otgjokqx')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)