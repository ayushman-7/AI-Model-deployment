import tensorflow as tf
import numpy as np
from fastapi import FastAPI, HTTPException
import requests
import os

# Azure Blob Storage Model URL
AZURE_MODEL_URL = "https://aomodelstorage.blob.core.windows.net/models/model.h5"
MODEL_PATH = "model.h5"

# Download model from Azure Blob Storage if not available locally
if not os.path.exists(MODEL_PATH):
    print("Downloading model from Azure Blob Storage...")
    try:
        response = requests.get(AZURE_MODEL_URL)
        response.raise_for_status()  # Raise an error for bad status codes
        with open(MODEL_PATH, "wb") as file:
            file.write(response.content)
        print("Model downloaded successfully.")
    except Exception as e:
        print(f"Failed to download model: {e}")
        raise

# Load the model
try:
    model = tf.keras.models.load_model(MODEL_PATH)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Failed to load model: {e}")
    raise

# Create FastAPI app
app = FastAPI()

@app.post("/predict")
def predict(data: dict):
    try:
        # Ensure input_data is provided
        if "input_data" not in data:
            raise HTTPException(status_code=400, detail="input_data is required")

        # Reshape input data for the model
        input_data = np.array(data["input_data"]).reshape(-1, 28, 28)

        # Make predictions
        predictions = model.predict(input_data)

        # Return predictions
        return {"predictions": predictions.tolist()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run: uvicorn app:app --host 0.0.0.0 --port 8000