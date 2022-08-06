from ctypes import Array, windll
import locale, yaml

class Translator:
    def __init__(self, langs: Array, default_lang: str, base_path: str = "translations/") -> None:
        self.langs: Array = langs
        self.default_lang: str = default_lang
        self.base_path: str = base_path
        self.windll = windll.kernel32

        if self.base_path[-1] != "/":
            self.base_path += "/"

    def translate(self, lang: str, id: str, placeholders: dict = {}) -> str:
        if lang not in self.langs:
            lang = self.default_lang
        result: str = self.read_yaml(lang, id)
        if result == None:
            result = self.read_yaml(self.default_lang, id)
            if result == None:
                return id

        for placeholder in placeholders:
            result = result.replace(f"%{placeholder}%", placeholders[placeholder])

        return result

    def auto_translate(self, id: str, placeholders: dict = {}) -> str:
        return self.translate(self.get_locale(), id, placeholders)

    def read_yaml(self, lang: str, id: str):
        try:
            with open(f"{self.base_path}{lang}.yaml", "r+") as f:
                translations = yaml.load(f, Loader=yaml.FullLoader)
                for part in id.split("."):
                    translations = translations[part]
                return translations
        except Exception as e:
            return None

    def get_locale(self):
        return locale.windows_locale[self.windll.GetUserDefaultUILanguage()]