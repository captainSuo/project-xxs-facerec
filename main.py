"""
这是一个示范代码
调用了 opencv 自带的人脸检测器
具体请查看 src/haarcascades.py
"""

import cv2
import matplotlib.pyplot as plt
from .src.haarcascades import detect_faces
from .src.typing import Image

image: Image | None = cv2.imread("image.png")
assert image is not None
detect_faces(image)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
