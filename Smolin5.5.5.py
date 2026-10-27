class ProgrammingLanguage:
    def __init__(self, name, paradigm):
        self.name = name
        self.paradigm = paradigm

    def say_hello(self):
        return f"Мова програмування {self.name} вітає світ!"


class Python(ProgrammingLanguage):
    def __init__(self, name, paradigm, version):
        super().__init__(name, paradigm)
        self.version = version

    def say_hello(self):
        return f"Привіт від Python (версія {self.version})!"

    def write_script(self):
        return f"{self.name} виконує скрипт автоматизації."


class JavaScript(ProgrammingLanguage):
    def __init__(self, name, paradigm, environment):
        super().__init__(name, paradigm)
        self.environment = environment

    def say_hello(self):
        return f"Привіт від JavaScript у середовищі {self.environment}!"

    def run_in_browser(self):
        return f"{self.name} працює у веб-браузері."


if __name__ == "__main__":
    python_lang = Python("Python", "Мультипарадигмова", "3.11")
    js_lang = JavaScript("JavaScript", "Події та прототипи", "Node.js / Browser")

    print(f"Мова: {python_lang.name}, Парадигма: {python_lang.paradigm}")
    print(python_lang.say_hello())
    print(python_lang.write_script())

    print("-" * 30)

    print(f"Мова: {js_lang.name}, Парадигма: {js_lang.paradigm}")
    print(js_lang.say_hello())
    print(js_lang.run_in_browser())