from confluent_kafka import Consumer, KafkaException, KafkaError

# Configuration du consommateur Kafka
conf = {
    'bootstrap.servers': 'localhost:9092',  # Serveur Kafka
    'group.id': 'file-consumer-group',  # Identifiant du groupe
    'auto.offset.reset': 'earliest',  # Commencer à lire depuis le début du topic
}

consumer = Consumer(conf)
topic = 'G-topic'

# Souscrire au topic
consumer.subscribe([topic])

# Fichier de sortie
output_file_path = "c.txt"

with open(output_file_path, 'wb') as f:
    try:
        while True:
            # Lire les messages du topic
            msg = consumer.poll(timeout=1.0)  # Attendre 1 seconde pour un message
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    print(f"Fin de partition atteint: {msg.partition()} @ {msg.offset()}")
                else:
                    raise KafkaException(msg.error())
            else:
                # Écrire le message dans le fichier de sortie
                f.write(msg.value())
                print(f"Réception de {len(msg.value())} octets")
    except KeyboardInterrupt:
        print("Consommation arrêtée manuellement")
    finally:
        # Fermer le consommateur
        consumer.close()
