import io
from google.cloud import vision_v1p3beta1 as vision
from google.cloud.vision_v1p3beta1 import types


clientVision = vision.ImageAnnotatorClient()
with io.open('vision.jpeg', 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

image_context = types.ImageContext(
    language_hints=['mul-latin-t-i0-handwrit']
)

responseVision = clientVision.document_text_detection(
    image=image,
    image_context=image_context
)

print(responseVision.full_text_annotation.text)