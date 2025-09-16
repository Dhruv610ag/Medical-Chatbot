# MedicoAI 🩺

**MedicoAI** is an AI-powered medical chatbot that helps users with health-related queries, symptom insights, and wellness guidance.  
It makes healthcare information more accessible and user-friendly while acting as a smart companion for reliable medical support.  

> ⚠️ **Disclaimer:** MedicoAI is **not** a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of a qualified healthcare provider for medical concerns.

---

## 🚀 How to Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Dhruv610ag/MedicoAI.git
cd MedicoAI
```

---

### 2️⃣Create a Conda Environment

```bash
conda create -n medibot python=3.10 -y
conda activate medibot
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Set Up Environment Variables

Create a .env file in the root directory and add your Pinecone & OpenAI credentials:

```bash
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
OPENAI_API_KEY   = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

---

### 5️⃣ Store Embeddings in Pinecone

```bash
python store_index.py
```

---

### 6️⃣ Run the Application

```bash
python app.py
```

Now open your browser and navigate to:

```bash
http://localhost:5000
```

---

# 🛠️ Tech Stack

- Python
- LangChain
- Flask
- GROQ
- PINECONE

---

# Pinecone

☁️ AWS CI/CD Deployment with GitHub Actions

1. Login to AWS Console
2. Create IAM User for Deployment
Grant the following permissions:
    - EC2 → Virtual machine hosting
    - ECR → Elastic Container Registry for Docker images

Policies Required:
    - AmazonEC2ContainerRegistryFullAccess
    - AmazonEC2FullAccess

3. Create an ECR Repository

Save the URI (example):

```bash
666802049678.dkr.ecr.us-east-1.amazonaws.com/medical-chatbot
```

4. Launch an EC2 Instance (Ubuntu)

5. Install Docker on EC2

```bash
sudo apt-get update -y
sudo apt-get upgrade -y
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```

6. Configure EC2 as a Self-Hosted GitHub Runner

- Go to your repo: Settings > Actions > Runners > New self-hosted runner

- Choose OS, then copy & run the provided commands on EC2

7. Setup GitHub Secrets
Add the following secrets in your repo settings (Settings > Secrets > Actions):

- AWS_ACCESS_KEY_ID

- AWS_SECRET_ACCESS_KEY

- AWS_DEFAULT_REGION

- ECR_REPO

- PINECONE_API_KEY

- OPENAI_API_KEY

---

## 📌 Roadmap

- Add user-friendly frontend (React/Next.js)

- Integrate more medical knowledge sources

- Enhance deployment with monitoring/logging

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repo and submit a PR.

---

## 📜 License

This project is licensed under the Apache-2.0 license.

---

This version is:  
✔ Clean & professional  
✔ Proper headings with emojis for readability  
✔ Clearly separated **local run** vs **AWS CI/CD deployment** steps  
✔ Added disclaimer, roadmap, contributing, and license sections  

Would you like me to also create a **GitHub Actions workflow file (`.github/workflows/deploy.yml`)** so that your README aligns with actual CI/CD automation?
