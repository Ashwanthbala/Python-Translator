from translate import Translator

translator = Translator(to_lang="es")

with open("genai.txt","r") as file:
    text = file.read()
    translation = translator.translate(text)
    print(translation)
    with open("esgenai.txt","w") as file1:
        file1.write(translation)