import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from daos.image_2d import Image2DDao

image2DDao = Image2DDao()

image = image2DDao.generate_image(
    "A cat holding a sign that says hello world", "", steps=28
)

image.save("test_text-2-image.png")
