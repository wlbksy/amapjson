from setuptools import find_packages, setup

setup(name='amapjson',
      version='0.1',
      description='geojson for amap',
      author='WANG Lei',
      author_email='wlbksy@126.com',
      license='MIT',
      packages=find_packages(),
      platforms=['Windows', 'Linux', 'Mac OS-X'],
      python_requires='>=3.5',
      classifiers=[
          'Intended Audience :: Education',
          'Intended Audience :: Science/Research',
          'Programming Language :: Python :: 3 :: Only',
          'Topic :: Scientific/Engineering',
          'Topic :: Scientific/Engineering :: GIS'
      ],
      zip_safe=False
      )
