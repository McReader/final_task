from setuptools import setup, find_packages, find_namespace_packages

setup(
    name='rss_reader',
    version='1.4',
    description='Pure Python command-line RSS reader',
    url="https://github.com/McReader/final_task",
    author='Dzianis Roi (McReader)',
    author_email='mcreader215@gmail.com',
    license='MIT',
    packages=find_packages(where="src"),
    install_requires=[
        'argparse==1.4.0',
        'coverage==6.4.4',
        'dataclasses==0.8',
        'datetime==4.5',
        'enum==0.4.7',
        'FB2==0.1.7',
        'logging==0.4.9.6',
        'requests==6.0.10',
        'tinydb==4.7.0'
    ],
    python_requires='>=3.9',
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "rss_reader=rss_reader_cli:main",
        ],
    },
)
