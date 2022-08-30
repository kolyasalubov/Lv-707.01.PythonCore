class Human:
    _type = 'Homosapiens'

    def __init__(self, name):
        self.name = name

    def __setattr__(self, key, value):
        if key == 'name':
            object = super().__setattr__(key, value)

            print(f"Hello human - {value}")
            self.info_Homosapiens()
            self.info_about_Homosapiens()
            return object

    @classmethod
    def info_Homosapiens(cls):
        print(f"I have good news - you are {cls._type}")

    @staticmethod
    def info_about_Homosapiens():
        print("Homosapiens are terms used to distinguish Homo sapiens (the only extant Hominina species) that are anatomically "
              "consistent with the range of phenotypes seen in contemporary humans from extinct archaic human "
              "species.\n")

human = Human('Alex')
#change name
human.name = 'Stiven'