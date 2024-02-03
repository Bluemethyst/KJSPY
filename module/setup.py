from setuptools import find_packages, setup

with open("app/README.md", "r") as f:
    long_description = f.read()

setup(
    name="kjspy",
    version="0.1.0",
    description="A Python way to write KubeJS scripts for Minecraft!",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Bluemethyst/KubePY",
    author="ArjanCodes",
    author_email="bluemethyst@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    python_requires=">=3.10",
)