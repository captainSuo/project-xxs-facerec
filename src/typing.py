"""
用于类型提示
请养成良好的写类型提示的习惯
"""

from cv2.typing import NumPyArrayNumeric, MatLike
from typing import Literal, TypeAlias


Emotion: TypeAlias = Literal[
    "anger", "disgust", "fear", "happy", "neutral", "sad", "suprise"
]
Image = MatLike | NumPyArrayNumeric

__all__ = [
    "Emotion",
    "Image",
]
