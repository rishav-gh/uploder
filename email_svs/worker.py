from decouple import config
import pika

# Step 1: Define the callback (what to do when a message arrives)
def callback(ch, method, properties, body):
    print("📩 Received message:", body.decode())
    # You can process data here
    # Example: parse JSON, process file, etc.

# Step 2: Connect to RabbitMQ (only once)
params = pika.URLParameters(config('RABBITMQ_URL'))
connection = pika.BlockingConnection(params)
channel = connection.channel()

# Step 3: Declare queue (make sure it exists)
channel.queue_declare(queue='myqueue')

# Step 4: Start consuming messages
channel.basic_consume(queue='myqueue', on_message_callback=callback, auto_ack=True)

print("✅ Consumer is ready and waiting for messages...")
channel.start_consuming()
