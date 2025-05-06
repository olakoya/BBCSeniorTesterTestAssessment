# check_feature_file.py
import os

path = os.path.join(os.path.dirname(__file__), "features/schedule_api_steps.feature")
print(f"Looking for: {path}")

with open(path) as f:
    print("Contents:")
    print(f.read())
