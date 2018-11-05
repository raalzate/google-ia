import io
from google.cloud import vision_v1p3beta1 as vision
from google.cloud.vision_v1p3beta1 import types as vision_type
from google.cloud import language
from google.cloud.language import types as language_type
from google.cloud.language import enums


def get_image_to_text(img):
    client_vision = vision.ImageAnnotatorClient()
    with io.open(img, 'rb') as image_file:
        content = image_file.read()

    image = vision_type.Image(content=content)

    image_context = vision_type.ImageContext(
        language_hints=['mul-latin-t-i0-handwrit']
    )

    response_vision = client_vision.document_text_detection(
        image=image,
        image_context=image_context
    )

    return response_vision.full_text_annotation.text


def check_sentiment(text):
    client = language.LanguageServiceClient()
    document = language_type.Document(
        type=enums.Document.Type.PLAIN_TEXT,
        content=text
    )
    response = client.analyze_sentiment(document=document)

    return response.document_sentiment


print(check_sentiment(get_image_to_text("sentiment.jpg")))

