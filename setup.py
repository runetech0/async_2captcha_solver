import setuptools
import sys

required_packages = ["aiohttp",
                     "requests",
                     "requests_toolbelt",
                     "aiofiles"
                     ]


setuptools.setup(
    name="async-2captcha-solver",
    version="1.0",
    author="Rehman Ali",
    author_email="rehmanali.9442289@gmail.com",
    description="A discord API v9 wrapper for python",
    url="https://github.com/rehmanali1337/discord_api",
    packages=setuptools.find_packages(),
    install_requires=required_packages
)
