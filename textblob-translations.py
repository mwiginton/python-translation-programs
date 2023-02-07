from textblob import TextBlob

def perform_translation():
    original_text = TextBlob('What time is it?')
    return original_text.translate(from_lang='en', to='fr')


translated_text = perform_translation()
print(translated_text)