import json
import os

def save_candidate_data(data, path="saved_data/candidate_data.json"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    try:
        with open(path, "r") as f:
            all_data = json.load(f)
    except FileNotFoundError:
        all_data = []

    all_data.append(data)

    with open(path, "w") as f:
        json.dump(all_data, f, indent=2)

def log_interaction(log, path="logs/conversations.log"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a") as f:
        f.write(log + "\n")
