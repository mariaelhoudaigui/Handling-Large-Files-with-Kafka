from confluent_kafka import Producer

# Configuration du producteur Kafka
conf = {
    'bootstrap.servers': 'localhost:9092',  # Serveur Kafka
}

producer = Producer(conf)

# Nom du fichier et topic Kafka
file_path = "p.txt"
topic = 'G-topic'

# Taille du morceau (1 Mo ici, vous pouvez l'ajuster)
chunk_size = 1024 * 1024  # 1 Mo

def delivery_report(err, msg):
    if err is not None:
        print(f"Message échoué: {err}")
    else:
        print(f"Message envoyé à {msg.topic()} partition [{msg.partition()}] @ {msg.offset()}")

with open(file_path, 'rb') as f:
    while True:
        # Lire un morceau du fichier
        chunk = f.read(chunk_size)
        if not chunk:
            break
        # Envoyer le morceau au topic Kafka
        producer.produce(topic, chunk, callback=delivery_report)
        print(f"Envoyé un morceau de {len(chunk)} octets")

# Attendre la confirmation de l'envoi de tous les messages
producer.flush()
