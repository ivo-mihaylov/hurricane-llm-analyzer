#!/bin/bash
set -e  # Exit if any command fails

# Start Ollama in the background
ollama serve &

# Wait for Ollama to be ready
until curl -s http://localhost:11434 > /dev/null; do
    echo "Waiting for Ollama to start..."
    sleep 2
done

# Check if the Mistral model exists in the model folder
if [ ! -d "/root/.ollama/models/mistral" ]; then
    echo "Mistral model not found, pulling the model..."
    
    retries=5
    count=0
    success=false
    
    while [ $count -lt $retries ]; do
        if ollama pull mistral:7b; then
            success=true
            ollama run mistral:7b
            break
        fi
        count=$((count+1))
        echo "Retry $count/$retries failed, trying again..."
        sleep 10
    done
    
    if ! $success; then
        echo "Failed to pull the Mistral model after $retries attempts"
        exit 1
    fi
else
    echo "Mistral model already exists, skipping pull."
fi

# Keep the container running (since the server was started in the background)
wait
