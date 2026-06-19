from utils.road_inference import predict_image
from flask import Flask, request
import os
import uuid
from flask_cors import CORS

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

UPLOAD_FOLDER = os.path.join(
    BASE_DIR, 
    "uploads"
)

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)

app = Flask(__name__)
CORS(app)
@app.route("/")
def home():
    return {
        "message": "Road Classification API running"
    }


@app.route("/predict", methods=["POST"])
def predict():

    file = request.files["image"]
    
    extension = file.filename.split(".")[-1]

    unique_filename = (
        f"{uuid.uuid4()}.{extension}"
    )

    save_path = os.path.join(
        UPLOAD_FOLDER,
        unique_filename
    )

    file.save(save_path)
    try:
        result = predict_image(save_path)
    
    finally:
        if os.path.exists(save_path):
            os.remove(save_path)

    return result
if __name__ == "__main__":
    app.run(debug=True)