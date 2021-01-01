# -*- coding: utf-8 -*-
"""
oauth2-wildcard-application installation setup
"""
from setuptools import setup

setup(
    name='oauth2-wildcard-application',
    version='0.1.0',
    author='toxinu',
    author_email='geoffrey@opencraft.com',
    description='A custom OAuth2 Application to allow wildcard redirect URLs',
    license='GPL3',
    keywords='oauth, social auth, wildcard',
    url='https://github.com/open-craft/oauth2-wildcard-application',
    packages=[
        'wildcard_oauth2',
    ],
    entry_points={
        "lms.djangoapp": [
            "wildcard_oauth2 = wildcard_oauth2.apps:WildcardOauth2ApplicationConfig",
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Internet',
        'License :: OSI Approved :: GPL3 License',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.8',
    ],
)
