
import cv2
import os
import numpy as np

# Path to photos
photos_path = "photos"

# LBPH recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

faces = []
names = []
label_map = {}

current_label = 0

# Load images
for filename in os.listdir(photos_path):
    if filename.lower().endswith((".jpg", ".png", ".jpeg")):
        path = os.path.join(photos_path, filename)

        # Get name before underscore
        name = filename.split("_")[0]

        # Assign label
        if name not in label_map:
            label_map[name] = current_label
            current_label += 1

        label = label_map[name]

        # Read image
        img = cv2.imread(path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces.append(gray)
        names.append(label)

# Train model
recognizer.train(faces, np.array(names))

# Save training data
recognizer.write("trainer.yml")

# Save label map
with open("labels.txt", "w") as f:
    for name, label in label_map.items():
        f.write(f"{label}:{name}\n")

print("Training completed.")
