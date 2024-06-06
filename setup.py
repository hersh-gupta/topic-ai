from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='topic_ai',
    version='0.1.0',
    author='Hersh Gupta',
    author_email='hersh.gupta@dc.gov',
    description='A library for identifying topics from open-ended text data using Azure OpenAI API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.in.dc.gov/OCTO/topic_ai',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
    install_requires=[
        'pandas',
        'openai',
    ],
)