from setuptools import setup, find_packages

setup(
    name="pymidi",
    version="2.0.0",
    packages=find_packages(),
    install_requires=[
        'pyserial',
    ],
    author="Nathan Adkins",
    author_email="nathanpadkins@gmail.com",
    description="Making my own midi interface for keyboard",
    license="MIT",
    keywords="actuator robotics",
    url="https://github.com/nate-adkins/pymidi",   # project homepage
)