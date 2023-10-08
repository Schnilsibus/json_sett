import setuptools

with open("README.md", "r") as fp:
    long_description = fp.read()

setuptools.setup(
    name="json-sett",
    version="0.0.0",
    author="Nils Urbach",
    author_email="ndu01u@gmail.com",
    description="load and save settings from/ to a json file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    keywords=[
        "json",
        "settings"
    ],
    url="https://github.com/Schnilsibus/json_sett.git",
    package_dir={"": "_core"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Programming Language :: Python"
    ],
    test_suite="tests",
    install_requires=[
        "json-convenience",
    ]
)
