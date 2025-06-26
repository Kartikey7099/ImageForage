# 🧠 ImageForge – GAN-Based Image Generator

**ImageForge** is a deep learning project that leverages **Generative Adversarial Networks (GANs)** to generate fashion item images using the **Fashion-MNIST** dataset. The model is trained in **Google Colab** using PyTorch and includes a ready-to-use **Streamlit** web application for future deployment. This project demonstrates a full ML pipeline — from data preprocessing to model training and real-time image synthesis.

---

## 🚀 Project Highlights

- ✅ GAN (Generator & Discriminator) built from scratch in PyTorch
- ✅ Trained on Fashion-MNIST dataset in Google Colab
- ✅ Modular, scalable code structure
- ✅ Reproducible training script (`train.py`)
- ✅ Ready-to-deploy Streamlit app (`app.py`)
- ✅ Sample generated outputs included


## 📷 Sample Output

| Generated Image Example |
|--------------------------|
| ![Sample](outputs/sample_epoch_30.png) |

## 📁 Project Structure

ImageForge/
├── app/ # Streamlit app code
│ └── app.py
├── models/ # Generator and Discriminator models
│ ├── generator.py
│ └── discriminator.py
├── outputs/ # Generated sample images
├── data/ # Fashion-MNIST dataset (auto-downloaded)
├── generator.pth # Trained Generator model
├── train.py # GAN training script (Colab-compatible)
├── generate.py # Image generation script
├── requirements.txt # Python dependencies
└── README.md # Project documentation


🌐 Deployment Note
The model is currently trained and tested, and can be deployed via Streamlit Cloud or Hugging Face Spaces. A ready-to-deploy app.py is included, and instructions are provided for future deployment.

🧠 Tech Stack
Python 3.8+
PyTorch
Torchvision
Matplotlib
Streamlit
Google Colab

🙋‍♂️ Author
Kartikey Sharma
🎓 B.Tech in Computer Science (Specialization: Data Science)
📫 kartikeysharmawork2222@gmail.com

