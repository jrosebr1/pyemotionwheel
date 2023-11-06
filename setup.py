from setuptools import setup, find_packages

setup(
    name='pyemotionwheel',
    version='0.1.0',
    author='Adrian Rosebrock',  # Replace with your name
    author_email='your.email@example.com',  # Replace with your email
    description='Python library providing a programmatic interface to an emotion wheel, a simple psychological tool for identifying and articulating emotions.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/jrosebr1/pyemotionwheel',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'anytree>=2.8.0',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',  # Change once official v1 is released
        'Intended Audience :: Developers',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Education',
        'Topic :: Software Development :: Libraries',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.7',
    keywords=[
        'emotion wheel',
        'psychological tool',
        'emotion identification',
        'emotional intelligence',
        'therapeutic tool',
        'education',
        'personal development',
        'emotional articulation',
        'emotional literacy',
        'emotional hierarchy',
    ],
    project_urls={
        'Documentation': 'https://github.com/jrosebr1/pyemotionwheel#README',
        'Source': 'https://github.com/jrosebr1/pyemotionwheel',
        'Tracker': 'https://github.com/jrosebr1/pyemotionwheel/issues',
    },
)
