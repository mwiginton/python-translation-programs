import goslate

def perform_translation():
    original_text = 'Practice translating some text.'
    gs = goslate.Goslate()
    return gs.translate(original_text, 'fr')

translated_text = perform_translation()
print(translated_text)