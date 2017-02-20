from setuptools import setup,find_packages
setup(name='fetchopenfmri',
      version='1.0',
      description='Fetches files for the latest version of an openfMRI dataset',
      packages=find_packages(),
      author='William Hedley Thompson',
      url='https://www.github.com/wiheto/fetchopenfmri',
      entry_points={
        'console_scripts': ['fetchopenfmri=fetchopenfmri.fetch:main'],
      },
      download_url = 'https://github.com/wiheto/fetchopenfmri/archive/v1.tar.gz'
      keyworkds={'openfmri','open data','fmri'}
      )
