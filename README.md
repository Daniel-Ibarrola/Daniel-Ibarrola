#  👋 Hi, I’m Daniel
[![Linkedin: Daniel-Ibarrola](https://img.shields.io/badge/-DanielIbarrola-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/d-ibarrola/)](https://www.linkedin.com/in/d-ibarrola/)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)

```Python
class Daniel(SoftwareEngineer):

    def __init__(self):
        super().__init__(
            seniority="Senior", name="Daniel Ibarrola", location="CDMX, Mexico"
        )

    def describe(self) -> str:
        return (
            f"I'm {self.name}, a senior engineer who designs and builds cloud-native systems "
            "using Python, AWS, and modern DevOps practices. I specialize in backend architecture, "
            "infrastructure as code, and scalable full-stack applications."
        )

    @property
    def stack(self) -> set[str]:
        return {
            "Python",
            "TypeScript",
            "React",
            "FastAPI",
            "Terraform",
            "Docker",
            "GitHub Actions",
            "Bitbucket Pipelines",
            "AWS",
            "PostgreSQL",
            "DynamoDB",
        }

    @staticmethod
    def experience() -> list[Experience]:
        return [
            Experience(
                company="Inter-Con Security Systems",
                position="Senior Software Engineer",
                responsibilities=(
                    "Designing cloud-native architectures with AWS and Terraform, "
                    "developing full-stack applications in Python and React, and mentoring junior developers."
                ),
            ),
            Experience(
                company="Centro de Instrumentación y Registro Sísmico",
                position="Software Engineer",
                responsibilities=(
                    "Built real-time seismic data systems and automated AWS infrastructure with Terraform."
                ),
            ),
            Experience(
                company="Hospital Infantil de México Federico Gómez",
                position="Software Engineer",
                responsibilities=(
                    "Led the development of an open-source pharmacophore modeling library for drug discovery."
                ),
            ),
        ]
```