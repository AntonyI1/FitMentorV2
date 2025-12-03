#!/usr/bin/env python3
"""Start FitMentor backend and frontend servers."""

import subprocess
import sys
import os
import time
import signal

ROOT = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.join(ROOT, "src", "backend")
FRONTEND_DIR = os.path.join(ROOT, "src", "frontend")

processes = []

def cleanup(sig=None, frame=None):
    for p in processes:
        p.terminate()
    sys.exit(0)

signal.signal(signal.SIGINT, cleanup)
signal.signal(signal.SIGTERM, cleanup)

print("Starting FitMentor...")
print("  Backend:  http://localhost:5000")
print("  Frontend: http://localhost:8000")
print("\nPress Ctrl+C to stop\n")

# Start backend
backend = subprocess.Popen(
    [sys.executable, "-c",
     f"import sys; sys.path.insert(0, '{BACKEND_DIR}'); from app import app; app.run(port=5000)"],
)
processes.append(backend)

# Start frontend
frontend = subprocess.Popen(
    [sys.executable, "-m", "http.server", "8000", "--directory", FRONTEND_DIR],
)

time.sleep(1)
print("Ready! Open http://localhost:8000")

# Wait for processes
try:
    while all(p.poll() is None for p in processes):
        time.sleep(1)
except KeyboardInterrupt:
    pass

cleanup()
