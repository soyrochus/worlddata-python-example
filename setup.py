import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="worlddata-python-example",
    version="0.0.1",
    author="Iwan van der Kleijn",
    author_email="iwanvanderkleijn@gmail.com",
    description="A Python package demonstrating the usage with large data sets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/soyrochus/worlddata-python-example",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)