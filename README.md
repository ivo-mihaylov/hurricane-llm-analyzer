# 🧠 Local LLM Question Answering App
![CI](https://github.com/ivo-mihaylov/hurricane-llm-analyzer/actions/workflows/ci.yml/badge.svg)


This project is a simple but powerful Python application that lets users ask questions about a small dataset using a local Large Language Model (LLM). It loads a dataset of hurricanes, feeds it to the model, and returns intelligent, human-readable answers — all without needing internet access.

You can use the app via a **command-line interface** or through a **web browser**.

---

## ⚙️ Features
- Local LLM (Mistral via [Ollama](https://ollama.com)) for answering questions.
- Uses pandas to manage and structure the dataset.
- Flask web interface for easy access via browser.
- Clean modular code and error handling.

---

## 📁 Project Structure

```
main/
├── data.py               # The dataset (Python dictionary)
├── data_loader.py        # Loads the dataset into a pandas DataFrame
├── llm_interface.py      # Handles interaction with the LLM via HTTP API
├── app.py                # Main CLI app for asking a question via terminal
├── web_app.py            # Web app using Flask
requirements.txt          # Project dependencies
README.md                 # Project documentation
```

---

## 🚀 Usage

### 🧪 Option A: Run as CLI (terminal app)

#### 1. Start Ollama (Mistral)
```bash
ollama run mistral
```

#### 2. Run the CLI app
```bash
python app.py
```
You'll be prompted to enter a question about the dataset. Example:
```
Which hurricane caused the most damage?
```

---

### 🌐 Option B: Run as Web App (Flask)

#### 1. Start Ollama (Mistral)
```bash
ollama run mistral
```

#### 2. Run the Flask app
```bash
export FLASK_APP=web_app.py
flask run
```
🐳 Option C: Run with Docker
If you want to containerize the application and run it in an isolated environment using Docker:

1. Make sure Docker is running
You can start Docker Desktop or use the Docker daemon in your terminal.

2. Build the Docker image
From the project’s root directory, run:

bash
Copy
Edit
docker build -t llm-flask-app .
This creates a Docker image named llm-flask-app using the instructions in your Dockerfile. The . means "use the current directory".

3. Run the Docker container
bash
Copy
Edit
docker run -p 5001:5000 llm-flask-app
This tells Docker to:

Run the app inside a container based on the llm-flask-app image

Map port 5000 inside the container to port 5001 on your machine (so you can access it)

4. Open the app in your browser
Visit: http://127.0.0.1:5001
You can now interact with your app through a web interface, powered by Flask and Docker.
#### 3. Open the app in your browser
Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)  
Ask your question using the form.

---

## 📦 Requirements
Install dependencies using:
```bash
pip install -r requirements.txt
```

**Dependencies:**
- `pandas`
- `requests`
- `Flask`

---

## 🧠 How it Works
1. The dataset is loaded into a pandas DataFrame.
2. The user submits a natural language question.
3. A prompt is constructed: the dataset is embedded as text + the user's question.
4. This prompt is sent via HTTP to Ollama’s local LLM API: `http://localhost:11434/api/generate`
5. The LLM responds with an intelligent answer.
6. The app displays the response either in the terminal or web UI.

---

## 🛠️ Next Steps
This version is functional and ready to demo. To improve or deploy:
- Add Docker support to containerize the app
- Push to GitHub for sharing
- Add unit tests or logging (for production)
- Deploy to Render/Railway for a live public demo

---

## 🤖 Notes
- Ollama must be running locally with the `mistral` model pulled.
- You can replace `mistral` with another compatible model if needed.

---

## 👩‍💻 Created by
Ivo Mihaylov - a A Junior Software Automation Engineer applicant
