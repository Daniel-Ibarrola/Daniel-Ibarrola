

class SoftwareDeveloper:
    pass


class Daniel(SoftwareDeveloper):

    def __init__(self):
        self.name = "Daniel"

    def describe(self):
        return f"Hi! I'm {self.name}, a software engineer whose speciality is python " \
               "programming. I have worked in different areas such as " \
               "scientific computing, web development and data science."

    @property
    def knowledge(self):
        return {
            "Python",
            "C++",
            "SQL",
            "HTML",
            "Git",
            "Docker",
            "Linux",
        }

    def list_interests(self):
        return [
            "Algorithms",
            "Data Science",
            "Machine Learning",
            "Drug Design",
        ]

    def currently_working_on(self):
        return "Open Pharmacophore: a tool for finding molecules with drug-like properties " \
               "https://github.com/uibcdf/OpenPharmacophore"


me = Daniel()
print(me.describe())
print(me.knowledge)
print(me.list_interests())
print(me.currently_working_on())
