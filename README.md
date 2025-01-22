# ** Description ** 
This project demonstrates how to handle large file transfers using Apache Kafka. It splits a large file into chunks, sends them to a Kafka topic with a producer, and reassembles the file on the consumer side.

# ** Key Features **
*File Chunking*: Splits large files into smaller chunks (e.g., 1 MB) for easier transmission. <br>
*Producer-Consumer Model*: The producer sends chunks to Kafka, and the consumer reassembles them into the original file.<br>
*Fault Tolerance*: Ensures reliable delivery and handling of file chunks.<br>

# ** Usage **
*Producer*: Splits the file into chunks and sends them to a Kafka topic.<br>
*Consumer*: Reads chunks from the Kafka topic and writes them back into a new file, reassembling the original.<br>

# **Prerequisites**
Apache Kafka set up on your machine or a remote server.<br>
Python 3.x with ```confluent-kafka``` library installed.
