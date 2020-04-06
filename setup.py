from setuptools import setup

setup(name='dev_aberto_elijose',
    version='0.1',
    description='Exemplo de Pacote Python',
    author='Eli Jose Abi Ghosn',
    author_email="elijag@al.insper.edu.br",
    url='https://github.com/elijose55/PacoteExemplo',
    classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests'
    ],
    packages=['dev_aberto'],
    scripts=['scripts/hello.py'],
    )