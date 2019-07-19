from setuptools import setup

setup(
    name='scrapy-fake-useragent',
    version='1.2.0',
    description='Use a random User-Agent provided by fake-useragent for every request',
    long_description=open('README.rst').read(),
    keywords='scrapy proxy user-agent web-scraping',
    license='New BSD License',
    author="Alexander Afanasyev / Alfonso de la Guarda",
    author_email='alfonsodg@gmail.com',
    url='https://github.com/alfonsodg/scrapy-fake-useragent',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Scrapy',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    packages=[
        'scrapy_fake_useragent',
    ],
    install_requires=[
        'package @ git+https://github.com/alfonsodg/fake-useragent@0.1.15#egg=fake-useragent-0.1.15'
#        'fake-useragent>=0.1.15'
    ],
#    dependency_links=[
#        "git+https://github.com/alfonsodg/fake-useragent@0.1.15#egg=fake-useragent-0.1.15"
#    ]
)
