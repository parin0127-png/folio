from deep_translator import GoogleTranslator
LANGUAGES = GoogleTranslator().get_supported_languages(as_dict = True)

def translate_text(text: str, target_language: str):
    """translate any text or sentence from one language to another target language"""
    target = LANGUAGES.get(target_language.lower(), target_language.lower())
    result = GoogleTranslator(source = "auto", target = target).translate(text)
    return result

