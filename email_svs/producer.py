import pika

params = pika.URLParameters('amqps://dkhxytac:NgD9bv17yv7YnpjVucX2xj39ffNcBKBJ@rabbit.lmq.cloudamqp.com/dkhxytac')
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='myqueue')

message = "Hello RabbitMQ!"
channel.basic_publish(exchange='', routing_key='myqueue', body=message)
print("📤 Sent:", message)

connection.close()
