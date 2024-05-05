import deepl

auth_key = "3bd9ca42-0a30-4f90-a6d1-185d0b942c67:fx"
translator = deepl.Translator(auth_key)

def translate(text, target_lang):
    result = translator.translate_text(text, target_lang=target_lang)
    return result.text