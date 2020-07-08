import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pdfplot",  # Replace with your own username
    version="0.0.3",
    author="Sauhaarda Chowdhuri",
    author_email="sauhaarda@mit.edu",
    description="Organize and version your matplotlib figures as PDFs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sauhaardac/pdfplot",
    packages=['pdfplot'],
    install_requires=['matplotlib'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.1',
)
