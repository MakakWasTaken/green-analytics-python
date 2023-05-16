import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='green-analytics',
    version='0.1.0',    
    description='Green Analytics is a Python library for connecting to the green-analytics.com dashboard.',
    url='https://github.com/MakakWasTaken/green-analytics-python',
    author='Markus Moltke',
    author_email='markus@unknown-studios.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires=['codecarbon', 'requests'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Sustainable Companies',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)