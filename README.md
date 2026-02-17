# Field Project - Object Detection & Image Captioning

## 📋 Project Description

Field Project is a secure web application that combines advanced AI technologies for object detection and image captioning. Users can create an account, log in, and upload images to automatically detect objects and generate descriptive captions. The application stores all results in a local SQLite database for easy access and management.

## 🚀 What Does This Project Do?

The application performs the following tasks:

1. **User Authentication**: Secure user registration and login system with bcrypt password hashing
2. **Object Detection**: Uses YOLOv8 (nano model) to detect objects in uploaded images
3. **Image Captioning**: Generates natural language descriptions of images using Salesforce BLIP model
4. **Data Persistence**: Saves detection results and captions to SQLite database for each user
5. **User-Friendly Interface**: Built with Streamlit for an intuitive and interactive web experience

## 🛠️ Technology Stack

### Core Technologies:
- **Python 3.x** - Primary programming language
- **Streamlit** - Web application framework for building the UI
- **YOLOv8** (Ultralytics) - State-of-the-art object detection model
- **BLIP** (Salesforce) - Vision-language model for image captioning
- **PyTorch** - Deep learning framework for running ML models
- **Bcrypt** - Secure password hashing for authentication
- **SQLite** - Lightweight database for storing user data and results
- **Pillow (PIL)** - Image processing library
- **OpenCV** - Computer vision library for image operations

## 📁 Project Structure
