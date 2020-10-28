from setuptools import setup, find_packages

with open('requirements.txt') as requirements_file:
    install_requirements = requirements_file.read().splitlines()

setup(
    name="chpwd_cmd",
    version="0.0.0",
    description="This program executes the commands in the configuration file according to the current working directory.",
    author="teddy@sfc.wide.ad.jp",
    packages=find_packages(),
    install_requires=install_requirements,
    entry_points={
        "console_scripts": [
            "chpwd_cmd=src.chpwd_cmd:main",
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3.7',
    ]
)
