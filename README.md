**Ergonomic Posture Detection with YOLOv5**


**Project Description**

This project tackles the crucial task of ergonomic posture detection using the state-of-the-art YOLO deep learning model. It aims to promote healthy workplace habits by identifying and flagging potentially harmful postures that could lead to musculoskeletal disorders (MSDs).

The program is designed to analyze the user's sitting posture in real-time and provide feedback on whether the posture is good or bad based on predefined criteria

**What It Does**

* Analyzes real-time video or images to detect human figures.
* Provides visual feedback, such as neck,torso, elbow,and knee angle,and also plot the line of each part of body

**Why It Matters**

* MSDs are a leading cause of workplace discomfort and lost productivity.
* Early detection and correction of poor posture can significantly improve employee well-being and reduce healthcare costs.

**How It Works**

1. **YOLOv5 Model**: The core of the project is a pre-trained YOLO nas pose detection. This model is capable of identifying human body keypoints.
2. **Real-Time Detection**: The project leverages computer vision libraries to capture live video or process images. It then feeds frames to the YOLO model to detect and classify keypoints in real-time.
3. **Angle_calculation** : using the **[Law of Cosines](https://www.varsitytutors.com/hotmath/hotmath_help/topics/law-of-cosines)** for calculating the angle of each joints

4. **Visualization**: Detected keypoinys  are visually represented by lines that ploted with opencv and at each keypoints it show the angle of each joints of body .

**Installation and Running**

**Prerequisites:**

* Python 3.x 
* SuperGradients: free, open-source library for training PyTorch-based computer vision models. 
* OpenCV 

**Instructions:**

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/<Milad0310>/ergonomic-posture-detection
   ```
2. **Install Dependencies:**
   https://www.supergradients.com/

**Contributing**

We welcome contributions to this project! Please refer to the CONTRIBUTING.md file for guidelines on how to submit pull requests.

**License**
This project is licensed under the MIT License.

**Output**

