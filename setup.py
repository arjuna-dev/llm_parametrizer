from setuptools import setup, find_packages

setup(
    name='llm_parametrizer',
    version='0.1',
    author ="Alejandro Camus",
    description="A library to parametrize multiple API calls for LLMs",
    packages=['llm_parametrizer'],
    install_requires=[
        'openai',
        'python-dotenv',
    ],
)