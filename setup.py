from setuptools import setup, find_packages
import pathlib


here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")
setup(
    name="catsordogs",
    version="0.0.5",
    description="Tells you if the given image is that of a cat or a dog.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jun6000/cats-or-dogs",
    author="Arjun Vishanth",
    author_email="arjunvishanth@gmail.com",
    keywords="cats, dogs, CNN, tensorflow, cats-or-dogs, model",
    package_dir={"catsordogs": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7, <4",
    install_requires=["tensorflow", "numpy", "opencv-python"],
    # Entry points. The following would provide a command called `sample` which
    # executes the function `main` from this package when invoked:
    # entry_points={  # Optional
    #     "console_scripts": [
    #         "sample=sample:main",
    #     ],
    # },
    project_urls={
        "Source": "https://github.com/jun6000/cats-or-dogs/",
    },
)
