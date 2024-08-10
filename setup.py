from setuptools import setup, find_packages

setup(
    name="sampy",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "colorama",
        "tqdm"
    ],
    entry_points={
        'console_scripts': [
            'sampy=sampy.installer:main',
        ],
    },
    author="Samuel Kinuthia",
    author_email="skinuthia77@gmail.com",
    description="A package to automate Django package installation and uninstallation.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Siymiel/sampy",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
