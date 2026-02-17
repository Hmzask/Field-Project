# Field Project - Object Detection & Image Captioning

## 📋 Project Description

Field Project is a secure web application that combines advanced AI technologies for object detection and image captioning. Users can create an account, log in, and upload images to automatically detect objects and generate descriptive captions. The application stores all results in a local SQLite database for easy access and management.

## 📁 Project Structure

```
Field-Project/
├── app.py                 # Main Streamlit application
├── database.py            # Database operations (user management, results storage)
├── requirements.txt       # Python dependencies
└── README.md             # Project documentation
```

## ✨ Key Features

- 🔐 **Secure Authentication**: User registration and login with encrypted passwords
- 🎯 **Accurate Object Detection**: YOLOv8 nano model for real-time object detection
- 📝 **Smart Image Captioning**: BLIP model generates contextual image descriptions
- 💾 **Database Storage**: Automatic saving of results for each user session
- 🖥️ **Interactive Web Interface**: Clean and user-friendly Streamlit UI
- 📱 **Multiple Image Formats**: Support for JPG and PNG images

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

## 📦 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/Hmzask/Field-Project.git
cd Field-Project
```

### Step 2: Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
```

Activate the virtual environment:
- **On Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **On macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install all required packages:
- streamlit
- ultralytics
- transformers
- torch
- pillow
- opencv-python
- sqlitebrowser

### Step 4: Run the Application

```bash
streamlit run app.py
```

The application will start and you can access it in your browser at `http://localhost:8501`

## 🎮 How to Use

1. **Register a New Account**:
   - Select "Register" from the Login/Register menu
   - Enter your desired username and password
   - Click the "Register" button

2. **Login**:
   - Select "Login" from the menu
   - Enter your credentials
   - Click the "Login" button

3. **Upload and Analyze an Image**:
   - Once logged in, click "Upload Image" button
   - Select a JPG or PNG image from your device
   - The app will:
     - Display the original image
     - Show detected objects with bounding boxes
     - Generate and display a caption describing the image
     - Save the results to the database

## 🔧 Commands Reference

| Command | Description |
|---------|-------------|
| `git clone https://github.com/Hmzask/Field-Project.git` | Clone the repository |
| `cd Field-Project` | Navigate to project directory |
| `python -m venv venv` | Create virtual environment |
| `source venv/bin/activate` (Mac/Linux) or `venv\Scripts\activate` (Windows) | Activate virtual environment |
| `pip install -r requirements.txt` | Install all dependencies |
| `streamlit run app.py` | Run the Streamlit application |

## 📋 Requirements

All dependencies are listed in `requirements.txt` and will be installed automatically when you run:
```bash
pip install -r requirements.txt
```

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs by opening an issue
- Suggest enhancements
- Submit pull requests with improvements

## 📝 License

This project is open source and available under the MIT License.

## 🆘 Troubleshooting

### Port Already in Use
If port 8501 is already in use, run:
```bash
streamlit run app.py --server.port 8502
```

### Model Download Issues
On first run, the application will download YOLOv8 and BLIP models. This may take a few minutes depending on your internet connection.

### GPU Support
If you have a CUDA-capable GPU, PyTorch will automatically use it. For CPU-only systems, the application will work but be slower.

## 📞 Contact & Support

For questions or support, please open an issue on the GitHub repository.

---

  **---Hamza**
