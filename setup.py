# setup.py 파일이 있으면 pip로 설치 가능하다.
from setuptools import setup

setup(
    name = "myapi", # 이 이름으로 패키지가 설치된다.
    version = 0.0.1,
    description = "my api lib",
    url = "https://github.com/chomu97/api_project.git",
    author = "chomu97",
    author_email = "ach1219@naver.com",
    packages = ["my_api"],
    install_requires = [
        "requests"
    ]
)