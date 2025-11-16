# Face Recognition Gate with OpenCV (LBPH)

This project is a simple **electronic gate prototype** using **OpenCV**
and the **LBPH Face Recognizer**, without external libraries like
`face_recognition`.

It uses: - A standard webcam - One photo per person - LBPH training
based on the folder name - A live access gate that shows: - **"Welcome,
(full name)"** → if recognized\
- **"Not recognized"** → if unknown

------------------------------------------------------------------------

## 📁 Project Structure

    project/
    │── photos/
    │   ├── John Doe_1.jpg
    │   ├── Alice Smith_1.jpg
    │── trainer.yml
    │── train.py
    │── gate.py

------------------------------------------------------------------------

## 🚀 How to Use

### **1. Add photos**

Inside **/photos**, place **one photo per person**.

Name format:

    Full Name_Number.jpg

Examples:

    John Doe_1.jpg
    Maria Silva_1.jpg

The training script automatically removes everything after the
underscore.

------------------------------------------------------------------------

## 🧠 Train the model

Run:

    python train.py

This generates:

    trainer.yml

This file contains the trained LBPH face recognition data.

------------------------------------------------------------------------

## 🚪 Run the access gate

Run:

    python gate.py

Press **Q** to quit.

------------------------------------------------------------------------

## 📝 Requirements

Install OpenCV with face module support:

    pip install opencv-contrib-python

------------------------------------------------------------------------

## 📌 Notes

-   Each user needs **only one image**, but more images improve
    accuracy.
-   Face must be frontal for best results.
-   Lighting affects recognition quality.

------------------------------------------------------------------------

## 📜 License

MIT License.

------------------------------------------------------------------------

## 👤 Author

Created by **Orcely Guedes**.
