## **Description:** 
This project demonstrates how to handle large file transfers using Apache Kafka. It splits a large file into chunks, sends them to a Kafka topic with a producer, and reassembles the file on the consumer side.

### **Key Features**
- **File Chunking**: Splits large files into smaller chunks (e.g., 1 MB) for easier transmission. <br>
- **Producer-Consumer Model**: The producer sends chunks to Kafka, and the consumer reassembles them into the original file.<br>
- **Fault Tolerance**: Ensures reliable delivery and handling of file chunks.<br>

## Technologies Used:
- **Kafka**: For streamlining the real-time data flow between the producer and consumer.
- **Python**: Programming language for implementing Kafka Producers, Consumers.
- **Confluent Kafka Python**: To interact with Kafka's messaging system.
  
## Prerequisites:
### 1. **Install Apache Kafka:**
   Apache Kafka is a distributed event streaming platform. Before starting, ensure that you have Kafka installed on your local machine or on a server. Follow these steps:

   - **Download Kafka**: Go to the [official Kafka website](https://kafka.apache.org/downloads) and download the appropriate version.
   - **Extract Kafka**: Unzip the downloaded file and move it to your desired directory.
   - **Install Java**: Kafka requires Java to run. If Java is not installed, download and install it from [Oracle's website](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html)

### 2.   **Start Zookeeper and Kafka:**
   Kafka requires **Zookeeper** for coordination. You need to start Zookeeper and then Kafka:
   - Open a terminal and navigate to the Kafka directory.
   - **Start Zookeeper** (in one terminal window):
     ```bash
     bin/zookeeper-server-start.sh config/zookeeper.properties
     ```
   - **Start Kafka** (in another terminal window):
     ```bash
     bin/kafka-server-start.sh config/server.properties
     ```

### 3. **Create a Kafka Topic:**
   After starting Kafka, create a Kafka topic to which the producer will send chunks:
   ```bash
   bin/kafka-topics.sh --create --topic file-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
 ```

### 4.Running the Application:

- **Running the Kafka Producer (p.py):**
This script splits the file into chunks and sends them to a Kafka topic
```bash
python p.py
```
- **Running the Kafka Consumer (c.py):**
The Kafka consumer script reads chunks from the Kafka topic and writes them back into a new file, reassembling the original.
```bash
python c.py
```
## Requirements:
Install the following Python libraries to run the application:
```
pip install confluent_kafka 
```
