__author__ = 'Will Maie, Matthew Hooker, Tom Wanielista, Ilja Bobkevic'
__author_email__ = 'wcmaier@m.aier.us, mwhooker@gmail.com, tom@simple.com, ilja.bobkevic@unibet.com'

import os
import subprocess

from setuptools import find_packages

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Fetch version from git tags, and write to version.py.
# Also, when git is not available (PyPi package), use stored version.py.
version_py = os.path.join(os.path.dirname(__file__), 'version.py')

try:
    p = subprocess.Popen(['git', 'describe', '--tags'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    o = p.communicate()
    if p.returncode != 0:
        raise Exception('git describe failed to execute reason: %s' % o[1])
    version_git = o[0].rstrip()
except Exception:
    version_git = '1.0'

version_msg = "# Do not edit this file"
with open(version_py, 'w') as fh:
    fh.write(version_msg + os.linesep + "__version__=" + version_git)

version = "{ver}".format(ver=version_git)

setup(name='unbound-ec2',
      version=version,
      description='Unbound DNS resolver to answer simple DNS queries using EC2 API calls',
      long_description=open('README.rst').read(),
      author=__author__,
      author_email=__author_email__,
      url='https://github.com/unibet/unbound-ec2',
      download_url='https://github.com/unibet/unbound-ec2/tarball/%s' % (version),
      packages=find_packages(exclude=['tests*']),
      zip_safe=False,
      test_suite="tests",
      setup_requires=[
      ],
      tests_require=[
          'coverage==3.7.1',
          'unittest2==0.5.1',
          'mock==1.0.1'
      ],
      install_requires=[
          'boto'
      ],
      data_files=[('/etc/unbound', [
          'data/unbound_ec2_script',
          'data/unbound_ec2.conf.example',
          'data/default_unbound.example'
      ])],
      scripts=['bin/unbound_ec2'],
      license="Apache License 2.0",
      platforms = "Posix; MacOS X",
      classifiers=[
         'Development Status :: 5 - Production/Stable',
         'Intended Audience :: Developers',
         'Natural Language :: English',
         'License :: OSI Approved :: Apache Software License',
         'Programming Language :: Python',
         'Programming Language :: Python :: 2.6',
         'Programming Language :: Python :: 2.7'
      ]
)
