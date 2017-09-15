from google.cloud import translate

def translate_text(text, target='en'):
    client = translate.Client()
    result = client.translate(text, target_language=target)

    print 'Source: {}'.format(result['detectedSourceLanguage'])
    print 'Input: {}'.format(result['input'])
    print 'Result: {}'.format(result['translatedText'])


text = """la liga, el classico"""

translate_text(text)
