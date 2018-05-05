
# Imports the Google Cloud client library
from google.cloud import translate

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../Google_Translate/TravelAsia-045df89194ef.json"

# Instantiates a client
translate_client = translate.Client()

def translate(source):

    # The text to translate
    text = source
    # The target language
    target = 'en'

    # Translates some text into Russian
    translation = translate_client.translate(
        text,
        target_language=target)

    print(u'Text: {}'.format(text))
    print(u'Translation: {}'.format(translation['translatedText']))
    return translation['translatedText']