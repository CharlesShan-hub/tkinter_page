import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="tkinter_page",
  version="0.0.5",
  author="Charles Shan",
  author_email="charles.shht@gmail.com",
  description="tkinter components extention",
  long_description=long_description,
  long_description_content_type="text/markdown",
  packages=setuptools.find_packages(),
  #url="https://github.com/pypa/pds",
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
)

#==========
# 建立包
# python3 setup.py sdist bdist_wheel

# 上传
# python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
# python3 -m twine upload dist/*

# 测试软件包
# python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps iiapds
# python3 -m pip install --index-url https://pypi.org/simple/ --no-deps iiapds






