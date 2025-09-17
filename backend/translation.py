import deepl

auth_key = "API-KEY"
translator = deepl.Translator(auth_key)

def translate(text, target_lang):
    result = translator.translate_text(text, target_lang=target_lang)
    return result.text