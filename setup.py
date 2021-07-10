from setuptools import setup


with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="sweet.web",
    version="0.0.1",
    author="tonglei",
    author_email="tonglei@qq.com",
    description="Sweet's web autotest module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sweeterio/web",
    packages=['sweet.modules.web'],
    package_data={'.': ['*.py']},
    install_requires=[
        'sweet',
        'selenium'
    ],      
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)