

class SoftwareDeveloper:
    pass


class Daniel(SoftwareDeveloper):

    def __init__(self):
        self.name = "Daniel Ibarrola"

    def about(self):
        return "I'm a graduate student in Chemistry. " \
                "My main focus is cheminformatics and drug design."

    @property
    def knowledge(self):
        return [
            "Python",
            "C++",
            "SQL",
            "HTML",
        ]

    def currently_working_on(self):
        return "Open Pharmacophore: a tool for finding drug-like molecules: " \
               "https://github.com/uibcdf/OpenPharmacophore"

    def currently_learning(self):
        return {
            "Algorithms": "https://github.com/Daniel-Ibarrola/Algorithms-Cpp",
            "Test-Driven Development": "https://github.com/Daniel-Ibarrola/ToDoList",
        }


me = Daniel()
print(me.about())
print(me.knowledge)
print(me.currently_working_on())
print(me.currently_learning())
