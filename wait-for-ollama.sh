#!/bin/sh
set -e

IP="ollama"  

echo "Waiting for Ollama to be ready..."
until curl -s http://$IP:11434/api/tags | grep -q "mistral"; do
  sleep 5
done

echo "Ollama is ready. Sending test request..."
response=$(curl -s -X GET http://$IP:11434 -H "Content-Type: application/json")

echo "Response from Ollama: $response"

echo "Starting Flask..."
exec python -m flask run --host=0.0.0.0
