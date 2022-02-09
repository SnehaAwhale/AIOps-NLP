from setuptools import setup

with open("README.md","r",encoding='utf-8') as f:
    long_description= f.read()

setup(
    name='src',
    version='0.0.1',
    author= 'SnehaAwhale',
    description='small package for ml pipline',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/SnehaAwhale/AIOps-NLP/tree/master',
    # author_email:'snehaawhale26@gmail.com',
    packages=['src'],
    python_requires=">=3.7",
    install_requires=[
        'dvc',
        'pandas',
        'scikit_learn'
    ]

)

