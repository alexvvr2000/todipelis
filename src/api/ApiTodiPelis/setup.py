from setuptools import setup, find_packages

setup(
    name="ApiTodiPelis",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "wheel==0.43.0",
        "requests==2.31.0",
        "flask==3.0.3",
        "mariadb==1.1.9",
    ],
    extras_require={
        "dev": [
            "setuptools>=42.0.0",
        ]
    },
    author="Alejandro Valenzuela Rivera",
    author_email="alejandrovalenzuela051@gmail.com",
    description="Exposición de la base de datos por flask",
    url="https://github.com/alexvvr2000/todipelis",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12.3",
)
