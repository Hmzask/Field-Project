import streamlit as st
import bcrypt
from database import *
from ultralytics import YOLO
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

init_db()

# -----------------------
# Authentication
# -----------------------

st.sidebar.title("Login / Register")

menu = st.sidebar.selectbox("Menu", ["Login", "Register"])

if menu == "Register":
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Register"):
        hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        try:
            add_user(username, hashed_pw)
            st.success("Account created!")
        except:
            st.error("Username already exists")

elif menu == "Login":
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Login"):
        user = get_user(username)

        if user and bcrypt.checkpw(password.encode(), user[2]):
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.success("Logged in successfully")
        else:
            st.error("Invalid credentials")

# -----------------------
# Main App After Login
# -----------------------

if st.session_state.get("logged_in"):

    st.title("Object Detection + Captioning")

    yolo_model = YOLO("yolov8n.pt")

    processor = BlipProcessor.from_pretrained(
        "Salesforce/blip-image-captioning-base"
    )
    model = BlipForConditionalGeneration.from_pretrained(
        "Salesforce/blip-image-captioning-base"
    )

    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png"])

    if uploaded_file:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image)

        # YOLO
        results = yolo_model(image)
        annotated = results[0].plot()
        st.image(annotated)

        detected_objects = []
        for box in results[0].boxes:
            name = yolo_model.names[int(box.cls)]
            detected_objects.append(name)

        # BLIP
        inputs = processor(image, return_tensors="pt")
        with torch.no_grad():
            output = model.generate(**inputs)

        caption = processor.decode(output[0], skip_special_tokens=True)

        st.subheader("Caption")
        st.write(caption)

        # Save to DB
        save_result(
            st.session_state["username"],
            uploaded_file.name,
            caption,
            ", ".join(detected_objects).upper()
        )

    # Show History
    # history = get_user_results(st.session_state["username"])

    # for record in history:
    #     st.write("Objects:", record[2])
    #     st.write("---")
