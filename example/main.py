from translator import Translator

#Create a new translator with the following languages: fr_FR, en_EN
#The default language is en_EN
#By default, the path of translations files is ./translations/
t: Translator = Translator(["fr_FR", "en_EN"], "en_EN")

#Translate the following string with the auto_translate method
#This method automatically detects the language of the user's system
print(t.auto_translate("hello", {"user": "Jerem"}))