import streamlit as st
import torch
import torch.nn as nn
import matplotlib.pyplot as plt

class Generator(nn.Module):
    def __init__(self, noise_dim=100):
        super(Generator, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(noise_dim, 256),
            nn.LeakyReLU(0.2),
            nn.Linear(256, 512),
            nn.LeakyReLU(0.2),
            nn.Linear(512, 1024),
            nn.LeakyReLU(0.2),
            nn.Linear(1024, 28*28),
            nn.Tanh()
        )

    def forward(self, x):
        return self.net(x).view(-1, 1, 28, 28)

# Load model
device = 'cpu'
model = Generator()
model.load_state_dict(torch.load('generator.pth', map_location=device))
model.eval()

st.title("🧠 ImageForge - GAN Image Generator")
st.write("Click below to generate a new Fashion-MNIST image.")

if st.button("Generate Image"):
    noise = torch.randn(1, 100)
    with torch.no_grad():
        generated = model(noise).squeeze()
    fig, ax = plt.subplots()
    ax.imshow(generated, cmap='gray')
    ax.axis('off')
    st.pyplot(fig)
