
import random

from googletrans import Translator

def translate_text(text, source_lang, target_lang):
    translator = Translator()
    translation = translator.translate(text, src=source_lang, dest=target_lang)
    return translation.text

# Example usage
source_text = 'thank you'
translated_text = translate_text(source_text, 'en', 'fr')
print(translated_text)
