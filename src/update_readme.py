

def get_code() -> list[str]:
    """ Get the code from the file me.py
    """
    code = [
        "```Python\n",
    ]

    add_line = False
    with open("me.py", "r") as fp:
        for line in fp.readlines():
            if line.startswith("class Daniel"):
                add_line = True
            if line.startswith("me = Daniel()"):
                add_line = False

            if add_line:
                code.append(line)

    code.append("```")
    return code


def main() -> None:
    """ Creates or updates the readme file."""
    
    header = [
        "#  👋 Hi, I’m Daniel\n",
        "[![Linkedin: Daniel-Ibarrola](https://img.shields.io/badge/-DanielIbarrola-blue?style=flat-square&logo"
        "=Linkedin&logoColor=white&link=https://www.linkedin.com/in/d-ibarrola/)]("
        "https://www.linkedin.com/in/d-ibarrola/)\n",
        "[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)]("
        "https://github.com/ellerbrock/open-source-badge/)\n",
    ]

    code = get_code()
    with open("../README.md", "w") as fp:
        fp.writelines(header)
        fp.writelines(code)

    print("DONE")


if __name__ == "__main__":
    main()
