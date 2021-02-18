from setuptools import find_packages
from setuptools import setup

setup(name='preprocessor',
      version='0.1',
      description='Audio Preprocessing Pipeline',
      author="Ian Cecil Mawuli Akoto",
      author_email = "iancecilakoto@gmail.com",
      url='https://github.com/ian0549/AI-Audio-Task',
      packages=find_packages(exclude=['tests*', 'testing*']),
      entry_points={
            'console_scripts': [
                  'preprocessor = bin.preprocessor.Preprocessor.main:main',
            ]
      },
      zip_safe=False)
