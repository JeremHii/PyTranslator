# Translator

Easy to use library, allow you to translate content using YAML files.

## Installing

**Python 3.8 or higher is required**<br /><br />
To install the library, please run the following command:
```sh
pip install git+https://github.com/JeremHii/PyTranslator
```

## Example

- First you have to create a `translations` folder.
- In this folder you need to create YAML files depending on the languages you will use. For example, if you want to be able to translate your content in french and in english you will to create two files: `fr_FR.yaml` and `en_EN.yaml` inside the `translations` folder. <br />

#### `translations/fr_FR.yaml` file
```yaml
hello: "Bonjour"
hello_user: "Bonjour %user%"
one:
    two: "Comment allez-vous ?"
```
<br />

#### `translations/en_EN.yaml` file
```yaml
hello: "Hello"
hello_user: "Hello %user%"
one:
    two: "How are you ?"
```
<br />

#### `main.py` file
```py
from translator import Translator

#Create a Translator object and set two languages available to "fr_FR" and "en_EN"
#The second param set the default language used
translator: Translator = Translator(["fr_FR", "en_EN"], "en_EN")

#Automatic translation based on user's system language
#Without placeholder
print(translator.auto_translate("hello"))
#This will print "Bonjour" or "Hello"

#With placeholder
print(translator.auto_translate("hello_user", {"user": "Jerem"}))
#This will print "Bonjour Jerem" or "Hello Jerem"

#If you dont want to auto_translate you can use the 'translate' method
#But you will have to specify the language you want to translate to 
print(translator.translate("fr_FR", "hello"))
#This will print "Bonjour"

#It is also possible to access longer paths, you just have to put a . between each part of the path
print(translator.auto_translate("one.two"))
#This will print "Comment allez-vous" or "How are you"

#Finally, if you want to print the locale of the user you can simply do:
print(translator.get_locale())
```
