from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='llm_parametrizer',
    version='0.1.2',
    author ="Alejandro Camus",
    description="A library to parametrize multiple API calls for LLMs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['llm_parametrizer'],
    url="https://github.com/arjuna-dev/llm_parametrizer",
    install_requires=[
        'openai',
        'python-dotenv'
    ],
)