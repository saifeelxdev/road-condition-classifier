import torch
import torch.nn as nn
import os
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "..",
    "models",
    "best_road_classifier.pth"
)
from torchvision.models import (
    efficientnet_b0,
    EfficientNet_B0_Weights
)

device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

weights = EfficientNet_B0_Weights.DEFAULT
transform = weights.transforms()

model = efficientnet_b0(weights=None)
model.classifier[1] = nn.Linear(
    model.classifier[1].in_features,
    2
)
print("Loading model")
model.load_state_dict(
    torch.load(
        MODEL_PATH,
        map_location=device
    )
)
print("Model Loaded")

model.to(device)

model.eval()

idx_to_class = {
    0: "Road issues detected",
    1: "Road Appears Safe"
}

def predict_image(images_path):

    img = Image.open(images_path)

    img = img.convert("RGB")

    img = transform(img)

    img = img.unsqueeze(0)

    img = img.to(device)

    with torch.no_grad():
        
        outputs = model(img)

        pred = torch.argmax(
            outputs,
            dim=1
        ).item()

        probs = torch.softmax(
            outputs, 
            dim=1
        )

        confidence = round(
            probs.max().item(),
            2
        )

        return {
            "confidence": confidence,
            "pred": idx_to_class[pred]
        }


