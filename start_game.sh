#!/bin/bash
# ==============================================================================
# Historic What-If Game: One-Click Local Launcher
# Launches the FastAPI inference backend and the Client Web UI
# ==============================================================================

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "$DIR"

echo "=================================================================="
echo "      HISTORIC WHAT-IF: DYNAMIC NARRATIVE ENGINE                 "
echo "=================================================================="

# Check for Python Virtual Environment
if [ -f ".venv/bin/python" ]; then
    PYTHON=".venv/bin/python"
    UVICORN=".venv/bin/uvicorn"
elif command -v python3 &> /dev/null; then
    PYTHON="python3"
    UVICORN="uvicorn"
else
    echo "Error: Python 3 could not be found."
    exit 1
fi

echo "[1/3] Starting FastAPI Engine on http://127.0.0.1:8000..."
$UVICORN api.server:app --host 127.0.0.1 --port 8000 &
BACKEND_PID=$!

echo "[2/3] Starting Web Client UI on http://localhost:8080..."
$PYTHON -m http.server 8080 --directory client &
FRONTEND_PID=$!

# Trap Ctrl+C to stop both processes cleanly
cleanup() {
    echo -e "\nShutting down Historic What-If Engine..."
    kill $BACKEND_PID 2>/dev/null
    kill $FRONTEND_PID 2>/dev/null
    exit 0
}
trap cleanup SIGINT SIGTERM

sleep 2

echo "[3/3] Opening game in your browser..."
open "http://localhost:8080" 2>/dev/null || xdg-open "http://localhost:8080" 2>/dev/null || echo "Please navigate to http://localhost:8080 in your browser."

echo "=================================================================="
echo "  Game is running! Press Ctrl+C in this terminal to stop.        "
echo "=================================================================="

wait
