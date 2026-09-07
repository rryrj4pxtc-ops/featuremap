#!/bin/bash
# ARC Features Map dashboard — always served with caching disabled.
DIR="/Users/ahmedalghamdi/Claude/ARC/projects/features-map/dashboard"
lsof -ti :8000 | xargs kill -9 2>/dev/null
nohup python3 "$DIR/scripts/serve.py" 8000 > /tmp/arc-dashboard-server.log 2>&1 &
sleep 1
open "http://localhost:8000/index.html?v=$(date +%s)"
