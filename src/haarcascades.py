"""
调用 opencv 自带的 haarcascades 模型进行人脸检测
"""

import cv2
from .typing import Image


def detect_faces(image: Image) -> Image:
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades  # pyright: ignore
        + "haarcascade_frontalface_default.xml"
    )
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 灰度图
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
    )

    for x, y, w, h in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return image
