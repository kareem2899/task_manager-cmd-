from setuptools import setup

setup(
    name='taskaty',
    version='0.1.0',
    description='simple command-line task-app written in python',
    author='Karim Mamdouh',
    install_requires=['tabulate'],
    entry_points={
        'console_scripts':['taskaty= taskaty:main']
    }

)