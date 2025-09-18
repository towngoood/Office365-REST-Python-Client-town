#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
from setuptools import setup, find_packages

with io.open("README.md", mode="r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="Office365-REST-Python-Client",
    version="2.5.3",
    author="Vadim Gremyachev",
    author_email="vvgrem@gmail.com",
    maintainer="Konrad Gądek, Domenico Di Nicola",
    maintainer_email="kgadek@gmail.com, dom.dinicola@gmail.com",
    description="Microsoft 365 & Microsoft Graph Library for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vgrem/Office365-REST-Python-Client",
    license="MIT",
    keywords="office365 microsoft365 graph api sharepoint teams outlook",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests",
        "msal",
        "pytz",
        "typing_extensions>=4.0.0",
    ],
    extras_require={
        "NtlmProvider": ["requests_ntlm"],
        "dev": ["pytest", "adal", "black", "flake8", "mypy"],
    },
    tests_require=["pytest", "adal"],
    test_suite="tests",
    packages=find_packages(
        exclude=["tests", "generator", "examples"]
    ),
    package_data={
        "office365": [
            "runtime/auth/providers/templates/SAML.xml",
            "runtime/auth/providers/templates/RST2.xml",
            "runtime/auth/providers/templates/FederatedSAML.xml",
        ]
    },
    entry_points={
        "console_scripts": [
            "office365-cli=office365.cli:main",
        ]
    },
    project_urls={
        "Bug Tracker": "https://github.com/vgrem/Office365-REST-Python-Client/issues",
        "Documentation": "https://office365-python-client.readthedocs.io/",
        "Source Code": "https://github.com/vgrem/Office365-REST-Python-Client",
    },
)
