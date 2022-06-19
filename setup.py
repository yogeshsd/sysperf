from setuptools import setup
from sysperf import __version__

setup(name="sysperf",
      version=__version__,
      description="System performance dashboard showing real time cpu, memory, swap, disk and network performance metrics",
      author="Yogesh Deshpande",
      packages=["sysperf"],
      zip_safe=False,
      author_email="yogeshsd@gmail.com",
      url="https://github.com/yogeshsd/sysperf",
      install_requires=[
            'Flask',
            'psutil'
      ],
      include_package_data=True,
      entry_points={
              'console_scripts': [
                  'sysperf = sysperf.perf'
              ]
            }
      )