from setuptools import find_packages, setup

LATEST_VERSION = "0.12.3"

exclude_packages = [
    "selenium",
    "webdriver",
    "fastapi",
    "fastapi.*",
    "uvicorn",
    "jinja2",
    "gpt-researcher",
    "langgraph"
]

with open(r"README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open("requirements.txt", "r") as f:
    reqs = [line.strip() for line in f if not any(pkg in line for pkg in exclude_packages)]

setup(
    name="multi-source-researcher",
    version=LATEST_VERSION,
    description="Multi-source autonomous research agent integrating Tavily search, WeChat articles and local documents.",
    package_dir={'gpt_researcher': 'gpt_researcher'},
    packages=find_packages(exclude=exclude_packages),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/your-repo",
    author="Your Name",
    author_email="your.email@example.com",
    license="Apache-2.0",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires='>=3.11',
    install_requires=reqs,


)