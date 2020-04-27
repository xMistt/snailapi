import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="snailapi",
    version="1.0.0",
    author="xMistt",
    description="Asynchronous Python wrapper for Snail API.",
    project_urls={
        "Documentation": "https://github.com/xMistt/snailapi/wiki",
        "Issues": "https://github.com/xMistt/snailapi/issues",
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xMistt/snailapi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'aiohttp',
    ],
)