# AgriTech

## General Description
This repository contains the implementation of the AgriTech project. AgriTech aims to provide traceability in an agricultural environment using blockchain technology with Directed Acyclic Graphs (DAGs). The project uses a Proof of Authority (PoA) consensus algorithm and includes three different setups: using an IPFS server, a traditional server, or no server at all.

## Authors 
This activity is part of the project R&D&I Laboratory on Cybersecurity, Privacy, and Secure Communications (TRUST Lab) financed by European Union NextGeneration-EU, the Recovery Plan, Transformation and Resilience, through INCIBE.
<div align="center">                                                    
    <img src="https://github.com/AVVillafranca/Pruebas/assets/168525862/fc1201ae-7be1-4980-a14e-ba08ab940c18" alt="TrustLab Logo">
</div>


## Project Overview

The project involves three types of devices:

- **IoT Devices**: These devices collect data, generate transactions, and send them to an active master node.

- **Master Devices**: These nodes synchronize with other master nodes and listen to MQTT topics for incoming data from IoT devices. They can either add the transaction to the DAG if they are the authority or forward it to the authoritative node.

- **Servers**: Depending on the setup, transactions can be sent to either an IPFS server or a traditional server, which returns a hash to be stored in the DAG.

## Setup

### IoT Device Configuration
In the *IoT_Device.py* script, change the device_id to ensure each IoT device has a unique ID:

> 'device_id': "IoT_1"  # Change this to a unique ID for each device

### Master Device Configuration
In the Master_Device.py script, configure the node_id and topic_temperature to indicate the node's ID and the topic it listens to:

> node_id = "node_001"  # Change this to a unique ID for each master node
> topic_temperature = "temperature1"  # Change this to the topic the node listens to

## Execution

### No Server Setup
- Run as many master devices and IoT devices as needed with Python 3:
>python3 Master_Device.py
>python3 IoT_Device.py

### Traditional Server Setup
- Run the server script:
>python3 Server.py

- Run as many master devices and IoT devices as needed:
>python3 Master_Device.py
>python3 IoT_Device.py

### IPFS Server Setup
To set up the IPFS server, follow these steps to download, install, and run an IPFS client on Ubuntu:

- Download and Install IPFS
> wget https://dist.ipfs.io/go-ipfs/v0.18.1/go-ipfs_v0.18.1_linux-amd64.tar.gz

- Extract the downloaded tar file:
> tar -xvzf go-ipfs_v0.18.1_linux-amd64.tar.gz

- Navigate to the extracted directory and install IPFS:
> cd go-ipfs
> sudo bash install.sh

- Initialize the IPFS node by running: This will start the IPFS node, making it ready to interact with other nodes in the IPFS network.
> ipfs daemon

- Run as many master devices and IoT devices as needed:
> python3 Master_Device.py
> python3 IoT_Device.py

## Results

- **Live Graph**: A real-time graph showing all master nodes and highlighting the authority:

    ![image](https://github.com/AVVillafranca/Pruebas/assets/168525862/99bc1340-1dd2-4d78-885f-9b5304a99359)

- **DAG Visualization**: A temporary image of the DAG graph with the last 100 transactions interconnected.:

    ![image](https://github.com/AVVillafranca/Pruebas/assets/168525862/665323af-e998-450e-b5c3-066419af47fc)

- **Transaction Data**: 
- *Traditional Server*: A JSON file containing all transaction data:

    ![image](https://github.com/AVVillafranca/Pruebas/assets/168525862/d5414343-f4ad-41f8-beeb-6095b850a9f7)

- *IPFS Server*:  The hash returned by the IPFS server stored in the DAG.

## Log Files

- *Master Log*: Each master device generates a log file upon execution, recording all changes in the network.

- *IoT Log*: Each IoT device generates a log file with the transactions it creates and indicates which master node it sends each transaction to.

### Afitional Scripts

- *process_log_master.py*: This script generates a graph from the master log to visualize the network's evolution, including node activation times and reputation growth, as well as identifying the authoritative node at any given time.

- *process_log_IoT_sends*: This script creates a graph from the IoT logs to show the distribution of transactions generated by the IoT devices and which master node each transaction was sent to.

- *process_log_IoT_transactions*: This script produces a graph from the IoT logs to display the number of transactions each IoT device has sent.

These scripts provide detailed insights into the system's performance and behavior, aiding in the analysis and understanding of the AgriTech project's operation.

## Server Query
Each server setup includes a *Server_Query.py* script. Run this script and input the hash of the transaction to retrieve its data.

Example Usage:
> python3 Server_Query.py

Enter the hash when prompted to get the transaction data.

## Detailed Explanation

### IoT Devices
IoT devices are responsible for:

1. Collecting data.
2. Generating a transaction.
3. Signing the transaction.
4. Sending the transaction to an active master node.

### Master Devices
Master devices handle:

1. Synchronizing with other master nodes.
2. Listening to MQTT topics for incoming data.
3. Acting as the authority to add transactions to the DAG or forwarding them to the current authoritative node.

### Servers
#### IPFS Server
- Transactions are sent to the IPFS server.
- The server returns a hash, which is stored in the DAG.

#### Traditional Server
- Transactions are sent to the server.
- The server returns a SHA256 hash, which is stored in the DAG.

# Conclusion
AgriTech provides a robust solution for traceability in agricultural environments using DAG-based blockchain technology. With flexible setups (IPFS server, traditional server, or no server), it ensures data integrity and synchronization across multiple devices.

For further details and code implementation, please refer to the individual scripts within each folder.

# Funding

This study was funded by the grant PID2020-114410RB-I00 MCIN/AEI/10.13039/501100011033, formed part of the AGROALNEXT programme, and was supported by MICIU with funding from European Union NextGenerationEU(PRTR-C17.I1) and by Fundación Séneca with funding from ComunidadAutónoma Región de Murcia (CARM).
