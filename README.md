#  👋 Hi, I’m Daniel
[![Linkedin: Daniel-Ibarrola](https://img.shields.io/badge/-DanielIbarrola-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/d-ibarrola/)](https://www.linkedin.com/in/d-ibarrola/)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)
```Python
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


```