import setuptools
import sys

required_packages = ["aiohttp",
                     ]


setuptools.setup(
    name="async-2captcha-solver",
    version="1.0",
    author="Rehman Ali",
    author_email="rehmanali.9442289@gmail.com",
    description="An async API wrapper for official 2captcha.com API in python",
    url="https://github.com/rehmanali1337/async_2captcha_wrapper",
    packages=setuptools.find_packages(),
    install_requires=required_packages
)
