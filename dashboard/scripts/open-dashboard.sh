#!/bin/bash
# Serve the dashboard with caching disabled, then open it.
DIR="/Users/ahmedalghamdi/Claude/ARC/projects/features-map/dashboard"
# Always restart: a plain http.server left running would keep serving cached JSON.
lsof -ti :8000 | xargs kill -9 2>/dev/null
nohup python3 "$DIR/scripts/serve.py" 8000 > /tmp/arc-dashboard-server.log 2>&1 &
sleep 1
open "http://localhost:8000/index.html?v=$(date +%s)"
