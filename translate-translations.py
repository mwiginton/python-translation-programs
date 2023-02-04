from translate import Translator

def perform_translation():
    original_text = 'What is your favorite book?'
    translator = Translator(from_lang='english', to_lang='german')
    return translator.translate(original_text)

translated_text = (perform_translation())
print(translated_text)

