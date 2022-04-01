from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")


def read_requirements() -> list[str]:
    with open("requirements.txt") as f:
        return f.read().splitlines()


setup(
    name="type-validators",
    version="0.1.0",
    description="Utility package to validate values based on type annotations",
    url="https://github.com/stijndcl/type-validators",
    author="stijndcl",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
    keywords="python, type, annotations, validators, value, utility, utilities",
    packages=find_packages(include=["type_validators"]),
    python_requires=">=3.9",
    install_requires=read_requirements(),
    project_urls={
        "Bug Reports": "https://github.com/stijndcl/type-validators/issues",
        "Source": "https://github.com/stijndcl/type-validators",
    },
)
