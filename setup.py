# -*- coding: utf-8 -*-
from io import open
from setuptools import setup
from sphinx-bootstrap-basic import __version__

setup(
    name='sphinx-bootstrap-basic',
    version=__version__,
    url='https://github.com/Blendify/sphinx-bootstrap-basic/',
    license='Apache License 2.0',
    author='Aaron Carlisle',
    author_email='carlisle.aaron00@gmail.com',
    description='Simple bootstrap theme',
    long_description=open('README.rst', encoding='utf-8').read(),
    zip_safe=False,
    packages=['sphinx-bootstrap-basic'],
    package_data={'sphinx-bootstrap-basic': [
        'theme.conf',
        '*.html',
        'static/css/*.css',
        'static/js/*.js',
    ]},
    include_package_data=True,
    # See http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
    entry_points = {
        'sphinx.html_themes': [
            'sphinx-bootstrap-basic = sphinx-bootstrap-basic',
        ]
    },
    classifiers=[
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Theme',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Apache License 2.0 License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)
