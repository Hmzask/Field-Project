import streamlit as st
from ultralytics import YOLO
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch
import cv2


# -----------------------
# Page Config
# -----------------------
st.set_page_config(page_title="Object Detection & Captioning", layout="centered")

st.title("🧠 Object Detection + Image Captioning")
st.write("Upload an image to detect objects and generate caption.")

# -----------------------
# Load Models (Cached)
# -----------------------
@st.cache_resource
def load_models():
    yolo_model = YOLO("yolov8n.pt")

    processor = BlipProcessor.from_pretrained(
        "Salesforce/blip-image-captioning-base"
    )

    model = BlipForConditionalGeneration.from_pretrained(
        "Salesforce/blip-image-captioning-base"
    )

    return yolo_model, processor, model

yolo_model, processor, blip_model = load_models()

device = "cpu"
blip_model.to(device)

# -----------------------
# Upload Image
# -----------------------
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")

    st.image(image, caption="Uploaded Image", use_column_width=True)

    # -----------------------
    # YOLO Detection
    # -----------------------
    results = yolo_model(image)

    annotated_image = results[0].plot()

    annotated_image = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)

    st.image(annotated_image, caption="Detected Objects", use_column_width=True)

    # -----------------------
    # BLIP Caption
    # -----------------------
    inputs = processor(image, return_tensors="pt").to(device)

    with torch.no_grad():
        output = blip_model.generate(**inputs, max_new_tokens=50)

    caption = processor.decode(output[0], skip_special_tokens=True)

    st.subheader("Caption \n")
    st.subheader(caption)

