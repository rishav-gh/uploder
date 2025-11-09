📨 **Django + RabbitMQ File Processing System**

This project demonstrates how to use RabbitMQ as a message broker in a Django application — to send and receive asynchronous tasks using pika.
It includes a simple file upload feature (producer) and a separate consumer script that processes uploaded files in the background.

🚀 Features

Upload files via Django web interface

Store uploaded files in the uploads/ directory

Send file paths as messages to RabbitMQ

Consume and process messages asynchronously

Move processed files to a processed/ folder

Environment variables used for secure RabbitMQ credentials

🛠️ Tech Stack

Backend: Django (Python)

Message Broker: RabbitMQ (CloudAMQP)

Messaging Library: pika

Environment Management: python-decouple
