from google.cloud import language

from google.cloud.language import types
from google.cloud.language import enums

client = language.LanguageServiceClient()


text = 'This is very bad'

document = types.Document(
    type=enums.Document.Type.PLAIN_TEXT,
    content=text
)

reponse = client.analyze_sentiment(document=document)

print(text)
print(reponse.document_sentiment)