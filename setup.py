from setuptools import find_packages, setup

setup(
    name="kanji_cmd",
    version="0.1.0",
    description="Command line based kanji tester",
    long_description="Command line based kanji tester",
    url="https://github.com/mattclarke/kanji_cmd",
    author="Matt Clarke",
    keywords="hardware simulation controls",
    packages=find_packages(exclude=["tests", "tests.*"]),
    python_requires=">=3.9.0",
    install_requires=[],
    entry_points={
        "console_scripts": [
            "kanji=kanji_cmd.runner:run",
        ],
    },
)
