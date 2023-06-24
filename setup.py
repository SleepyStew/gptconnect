import setuptools


setuptools.setup(
    name="GPTConnect",
    version="0.1.6",
    author="SleepyStew",
    description="A python package to make GPT functions easy",
    packages=["gptconnect"],
    install_requires=["openai"],
    url="https://github.com/SleepyStew/gptconnect",
    long_description=open("README.md").read(),
)
