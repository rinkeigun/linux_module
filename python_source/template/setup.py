from setuptools import setup, find_packages

setup(name="package",
    version="0.1",
    description="sample package",
    #long_description=readme,
    author="Huiqun Lin",
    author_email="huiqun.lin@gmail.com",
    install_requires=["numpy"],
    url="",
    license=license,
    packages=find_packages(exclude=("tests", "docs")))


# uninstall : python setup.py install --record result.txt