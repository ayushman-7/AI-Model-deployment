# 🚀 Deploying a Machine Learning Model on Azure with MLOps

## 📌 Overview
This project demonstrates **MLOps on Azure** by deploying a trained AI model using **Azure Blob Storage, FastAPI, Docker, and Azure Kubernetes Service (AKS)**. The model is stored in **Azure Blob Storage**, served using **FastAPI**, containerized with **Docker**, and deployed on **AKS** for scalability and high availability.

## 🛠️ Tech Stack
- **Cloud**: Azure
- **Model Storage**: Azure Blob Storage
- **API Framework**: FastAPI
- **Containerization**: Docker
- **Orchestration**: Kubernetes (Azure Kubernetes Service - AKS)
- **Registry**: Azure Container Registry (ACR)

---

## 🔹 Step 1: Store the Model in Azure Blob Storage

1. **Create a Storage Account:**
   - Go to **Azure Portal** → Create a **Storage Account**
   - Choose a **Blob Container** to store the model file

2. **Upload Model File:**
   - Upload your trained model (`.h5` or `.pkl`) to Azure Blob Storage
   - Note down the **storage URL** and **access credentials** for fetching the model dynamically

---

## 🔹 Step 2: Serve the Model with FastAPI

1. **Develop FastAPI Application:**
   - The API downloads the model from Azure Blob Storage at startup
   - Accepts input data via POST requests, processes it, and returns predictions
   
2. **Ensure Efficient Model Loading:**
   - Load model only once when the API starts to optimize performance
   - Handle multiple requests asynchronously for efficiency

---

## 🔹 Step 3: Containerize with Docker

1. **Write a Dockerfile:**
   - Base image: `python:3.9`
   - Install dependencies (FastAPI, TensorFlow/PyTorch, Azure SDKs)
   - Copy FastAPI app into the container and expose required ports

2. **Build and Push Image to Azure Container Registry (ACR):**
   ```sh
   az acr login --name <your-acr-name>
   docker build -t <your-acr-name>.azurecr.io/ml-model-api:latest .
   docker push <your-acr-name>.azurecr.io/ml-model-api:latest
   ```

---

## 🔹 Step 4: Deploy on Azure Kubernetes Service (AKS)

1. **Create an AKS Cluster:**
   ```sh
   az aks create --resource-group <your-resource-group> --name <your-cluster-name> --node-count 2 --enable-managed-identity --generate-ssh-keys
   ```

2. **Deploy Application on AKS:**
   - Create a Kubernetes deployment and service YAML file
   - Deploy using `kubectl apply -f deployment.yaml`
   - Expose the service via LoadBalancer to make it accessible

3. **Check Deployment:**
   ```sh
   kubectl get pods
   kubectl get services
   ```

---

## 🔹 Step 5: Testing & Optimization

- **Send test requests** to the deployed API using Postman or cURL
- **Monitor logs and performance** to ensure scalability
- **Optimize auto-scaling policies** in AKS to balance cost and efficiency

---

## 📌 Key Takeaways
✅ **Azure Blob Storage** efficiently manages large ML models  
✅ **FastAPI** is lightweight and ideal for serving AI models  
✅ **Docker** ensures portability and reproducibility  
✅ **Azure Kubernetes Service (AKS)** provides automated scaling and resilience  
✅ Transitioning from AWS to Azure broadens cloud expertise  

---

