from setuptools import setup, find_packages

setup(
    name='rss_reader',
    version='1.1',
    description='Pure Python command-line RSS reader',
    url="https://github.com/McReader/final_task",
    author='Dzianis Roi (McReader)',
    author_email='mcreader215@gmail.com',
    license='MIT',
    packages=find_packages(where="src"),
    install_requires=['argparse'],
    python_requires='>=3.9',
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "rss_reader=rss_reader:main",
        ],
    },
)
