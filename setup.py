from setuptools import setup, find_packages

with open('README.rst', encoding='utf-8') as f:
    readme=f.read()

setup(
    name="pgbackup",
    version="0.1.0",
    description="Database backups locally or a AWS S3.",
    author="Jorge",
    author_email="jorge.davilardz@hotmail.com",
    install_requires=[],
    packages=find_packages('src'),
    package_dir={'': 'src'}
)
