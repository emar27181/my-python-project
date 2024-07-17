from translate import Translator

translator = Translator(from_lang = "ja", to_lang = "en")
result = translator.translate("こんにちは私はベイマックスです")

print(result)