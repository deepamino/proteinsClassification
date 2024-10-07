<h1 align="center">DeepAmino: Protein Classification</h1>

<br>

<hr>
<h1 align="center">Study case 2: Architecture</h1>

## 1. Introduction

<p align="justify">
The human being needs proteins to survive all the time.  These are obtained from our body's DNA which goes through a process to synthesise amino acids to build the necessary proteins. As data scientist, the classification of this protein according to its amino acid chain was not known from the outset and so, in collaboration with the team of biologists from the University of Las Palmas de Gran Canaria, an application has been made that will be a language model that you give the amino acid chain and it will tell you what protein it is or even what protein it is close to.
</p>

## 2. Architecture

<p align="justify">
DeepAmino, the aforementioned model, is a PLM that is able to predict protein characteristics given its amino acid sequence. To deploy such a tool so that clients all around the world are able to make use of it, we introduce the following architecture. As can be seen in <b>Diagram 1</b>, the whole infrastructure is deployed on Amazon Web Services (AWS) to leverage the cloud's scalability, availability, and cost-effectiveness. AWS allows us to take advantage of economies of scale by paying only for the resources used (OpEx), rather than investing in upfront infrastructure (CapEx).
</p>

<p align="center">
<img src="images/diagram.png" width="600">
</p>

### Key Components:

#### **Amazon S3** 
- **Purpose:** Data Storage and Model Management  
- Amazon S3 is used to store two main types of data:
    1. **Training Data:** The large datasets of amino acid sequences and protein data needed for training the machine learning model. The **training data bucket** will store incoming data from various sources, including the National Center for Biotechnology Information (NCBI), facilitating further processing.
    2. **Model Outputs:** The trained models are stored and accessed via another S3 bucket, encouraging seamless versioning and updating. It will be useful to deploy real-time applications in which AI models are all the time training in batches. Once a model has been trained by the **SageMaker Trainer** service, it is uploaded to the bucket, creating an event which triggers the SageMaker Trainer service for the output model parameters

#### **Amazon SageMaker**
Training and Prediction. Amazon SageMaker is a **fully managed machine learning service** that allows developers and data scientists to build, train, and deploy machine learning models quickly and easily. It removes the heavy lifting associated with the infrastructure, so you can focus on developing the model. 

With SageMaker, you can:
1. **Train**: It simplifies training by providing pre-configured environments and optimized infrastructure for distributed training, which allows for efficient use of resources when working with large datasets.
2. **Deploy**: Once the model is trained, SageMaker allows for seamless deployment in production, providing a scalable inference endpoint. The endpoint can handle a high volume of requests, making it ideal for real-time prediction tasks.
3. **Manage**: SageMaker provides tools to monitor model performance and automatically scale resources to handle varying workloads.

We will have two SageMaker services that accomplish the following tasks.
- **SageMaker Trainer:** Used for building, training, and fine-tuning the protein classification models.
- **SageMaker Predictor:** Deployed to serve inference requests once the model has been trained and validated, allowing predictions based on amino acid sequences provided by the users.
    
#### **Amazon DynamoDB**
- **Purpose:** Database for protein sequences. Each protein amino acid sequence obtained from the **ncbi API** has been also saved into a DynamoDB Table, **Protein-sequences**, which stores the name-sequence pairs. This doesn't exactly lead to redundancy, despite the fact that the same sequences, including some other relevant metadata, have been loaded to the Amazon S3 already. Indeed

- A highly scalable NoSQL database used to store metadata or results from previous predictions, facilitating quick lookups and responses to users’ queries.

#### **Amazon EC2**
- **Purpose:** Computing Resources  
- EC2 instances are utilized to run general-purpose computation tasks, such as pre-processing the data received from the National Center for Biotechnology Information and orchestrating requests between services.
  
#### **Amazon API Gateway**
- **Purpose:** Interface for Clients  
- API Gateway serves as the interface between users and the backend system. It accepts HTTP requests, authenticates them using Amazon Cognito, and routes them to the appropriate services, such as SageMaker Predictor or EC2 instances.

#### **Amazon Cognito**
- **Purpose:** User Authentication  
- Cognito handles authentication and user management for secure access. Users are authenticated via Cognito before being allowed to interact with the system, ensuring secure access to sensitive bioinformatics data.

#### **Classic Load Balancer**
- **Purpose:** Traffic Distribution  
- The Classic Load Balancer is used to distribute incoming requests evenly across multiple EC2 instances and SageMaker endpoints, ensuring that the system remains responsive even under high load.

#### **Virtual Private Cloud (VPC)**
- **Purpose:** Network Security  
- A VPC is used to securely isolate the DeepAmino architecture. Sensitive operations, such as training and storage, are housed in the **private subnet**, while public-facing services like API Gateway and Cognito are housed in the **public subnet**.
  
#### **Integration with National Center for Biotechnology Information (NCBI)**
- **Purpose:** Data Source  
- The model can pull datasets directly from NCBI, keeping the training data up-to-date with the latest biological information.

## 3. Workflow

1. **User Request**: A client submits an amino acid sequence via a user interface or API.
2. **API Gateway**: The request is routed through API Gateway, which authenticates the user through Amazon Cognito.
3. **Processing & Prediction**: The authenticated request is forwarded to Amazon SageMaker's inference endpoint via EC2, where the trained model predicts the protein classification based on the input sequence.
4. **Storage & Response**: Results are stored in DynamoDB for future reference and returned to the client through API Gateway.

---

### Credits

- Susana Suárez Mendoza
- Ricardo Cárdenes Pérez
---
