# 🧠 Local LLM Question Answering App
![CI](https://github.com/ivo-mihaylov/hurricane-llm-analyzer/actions/workflows/ci.yml/badge.svg)

# Hurricane LLM Analyzer

This project is a simple, containerized, local LLM-powered web application that allows you to query a hurricane dataset in natural language. It uses:

- A **Flask** web interface
- The **Mistral** large language model
- Hosted locally via **Ollama**
- Dockerized for easy testing and sharing

---

## 🔗 Final URL for Testing
Access the app at:
```
http://127.0.0.1:5001
```
> **Note:** Even though Flask internally runs on port `5000`, it is mapped to host port `5001` in Docker. Trying `http://127.0.0.1:5000` will result in **access denied**.

---

## 🚀 How to Run the App

This project is fully containerized using Docker, meaning **you do NOT need to install Python, Ollama, or any dependencies manually**.

### ✅ Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running on your machine.
- At least **8–10 GB of free disk space** for model pulling.
- Internet connection (required to download the base Docker images and the Mistral model on first run).

### 🧭 Steps to Run

1. **Clone the project (if not already):**

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Run the containers using Docker Compose:**

   ```bash
   docker compose up --build
   ```

   > This will:
   > - Start the **Flask** application
   > - Spin up **Ollama** in a separate container
   > - Automatically download and launch the **Mistral** language model
   > - Wait for Ollama to be ready before starting the app

3. **Open your browser and go to:**

   👉 [http://127.0.0.1:5001](http://127.0.0.1:5001)

   > ⚠️ **Note:** Do **NOT** use `http://127.0.0.1:5000` even if the logs suggest it — the app is exposed on **port 5001**, as defined in `docker-compose.yml`.

---

## 📁 Project Structure & Purpose

```bash
LLM/
├── app.py                      # Legacy entry point (not used in container setup)
├── docker-compose.yml         # Spins up Flask and Ollama containers
├── Dockerfile                 # For Flask app container
├── Dockerfile.ollama          # Custom Ollama container with Mistral pre-installed
├── entrypoint.sh              # Waits for Ollama before starting Flask
├── wait-for-ollama.sh         # Ensures Ollama is healthy before Flask launches
├── requirements.txt           # Flask + dependencies
├── README.md                  # Project documentation
├── web_app.py                 # Main Flask application
├── .env                       # Environment variables (optional)
├── main/
│   ├── data.py                # Hurricane dataset
│   ├── data_loader.py         # Loads dataset
│   └── llm_interface.py       # Handles query-to-LLM communication
└── tests/
    └── test_web_app.py        # Sample test case
```

---

## ⚙️ How It Works – Execution Flow

1. **User** opens `http://127.0.0.1:5001` in browser
2. **Flask** (`web_app.py`) captures natural language query
3. It forwards the query to **Ollama's Mistral API** (running at `http://ollama:11434`)
4. **Mistral** returns an answer, which is displayed back in the browser

---

## 🧩 How the Pieces Work Together

### 📄 `web_app.py`
- Renders UI and handles HTTP requests
- Sends queries to `llm_interface.py`

### ⚙️ `llm_interface.py`
- Sends the user prompt to Mistral via Ollama API
- Receives and returns the model's response

### 📊 `data_loader.py`
- Loads the hurricane CSV file into pandas for future enhancement

### 📦 `Dockerfile`
- Builds the Flask container using Python 3.12

### 🧠 `Dockerfile.ollama`
- Builds a custom Ollama image that already includes Mistral model

### 🕒 `entrypoint.sh` / `wait-for-ollama.sh`
- Ensures Flask only starts once Ollama is ready and healthy

---

## 🛠️ Changes Made (Compared to Initial Version)

### ✅ Containerized Ollama
- **Why:** Originally, testers needed to install Ollama locally. Docker now handles this.

### ✅ Switched to Docker Compose with 2 Services
- **Why:** Needed Flask and Ollama to run together in sync.

### ✅ Added Health Checks & Entrypoint Wait Script
- **Why:** Flask was crashing when Ollama wasn't ready. The wait script solves this.

### ✅ Flask port changed to 5001 on host
- **Why:** Port 5000 was often in use and caused collisions. 5001 avoids this.

### ✅ Pre-installed Mistral inside Dockerfile.ollama
- **Why:** So users don’t wait 15+ mins on first run, or need internet.

### ✅ CI/CD setup (in `.github/workflows/`)
- **Why:** Ensures automated testing and clean GitHub pushes

---

## 🧪 Issue Faced: Missing Ollama Locally

### ❌ Initial Error
```bash
ConnectionError: Failed to establish new connection: [Errno 111] Connection refused
```
- **Cause:** User’s machine didn’t have Ollama installed
- **Fix:** Added a dedicated Ollama container via Docker with pre-pulled Mistral model

---

## 🔁 Final Docker Flow

1. `docker-compose up --build`
2. Spins up:
    - `ollama` container (w/ Mistral pre-installed)
    - `flask_app` container
3. You can now visit `http://127.0.0.1:5001` and chat with the model!

---

## 📊 Visual Diagram
(See attached image below for visual representation of file interactions and flow)

> Separate PNG file: `llm_project_architecture.png`



## 👩‍💻 Created by
Ivo Mihaylov - a A Junior Software Automation Engineer applicant
