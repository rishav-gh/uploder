from django.shortcuts import render
from django.http import HttpResponse
from decouple import config
import pika, json
import os

def upload_file(request):
    if request.method == "POST":
        file = request.FILES['file']
        file_path = os.path.join('uploads', file.name)

        os.makedirs('uploads', exist_ok=True)
        with open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        # connect to RabbitMQ
        connection = pika.BlockingConnection(pika.URLParameters(config('RABBITMQ_URL')))
        channel = connection.channel()

        channel.queue_declare(queue='file_tasks')

        # message to send
        message = json.dumps({'file_path': file_path})
        channel.basic_publish(exchange='', routing_key='file_tasks', body=message)
        connection.close()

        return HttpResponse("File uploaded and task queued!")

    return render(request, 'index.html')
