__________________________________________

<h1 align="center"> Difference generator</h1>

__________________________________________

## Hexlet tests and linter status   
[![Actions Status](https://github.com/spacewalrus73/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/spacewalrus73/python-project-50/actions)
[![Tests CI](https://github.com/spacewalrus73/python-project-50/actions/workflows/Project_check.yml/badge.svg)](https://github.com/spacewalrus73/python-project-50/actions)  
[![Maintainability](https://api.codeclimate.com/v1/badges/78249a13e03c7c051d4f/maintainability)](https://codeclimate.com/github/spacewalrus73/python-project-50/maintainability)  [![Test Coverage](https://api.codeclimate.com/v1/badges/78249a13e03c7c051d4f/test_coverage)](https://codeclimate.com/github/spacewalrus73/python-project-50/test_coverage)
----
## *Used technologies*
![](https://img.shields.io/badge/Python-v3.10-yellow?style=plastic&logo=python)  ![](https://img.shields.io/badge/flake8-v5.0.4-black?style=plastic&logo=flake8)  ![](https://img.shields.io/badge/Pyyaml-v6.0-yellow?style=plastic&logo=Python)  
![](https://img.shields.io/badge/Poetry-v1.3.2-blue?style=plastic&logo=poetry)  ![](https://img.shields.io/badge/Pytest-v7.2.1-yellowgreen?style=plastic&logo=Pytest)  ![](https://img.shields.io/badge/Git-v2.34.1-orange?style=plastic&logo=Git)
----
## _System requirements_
![](https://img.shields.io/badge/-OS%20Linux-black?style=plastic&logo=Linux) ![](https://img.shields.io/badge/-macOS-silver?style=plastic&logo=apple) ![](https://img.shields.io/badge/-OS%20Windows-9cf?style=plastic&logo=windows)
___
## _About difference generator_
Difference generator - a program that determines the difference between two data structures.  
Such a mechanism is used, for example, when outputting tests or when automatically tracking changes  
in configuration files.  

Utility features:
  
- Support for different input formats: _yaml_,  _json_ 
- Report generation as plain _text_, _stylish_ and _json_.
## _Installation_
1. You have to be installed Python (preferably python 3.10) and pip
2. Run the command in terminal:  
`python3 -m pip install --user git+https://github.com/spacewalrus73/python-project-50`  
or  
`git clone https://github.com/spacewalrus73/python-project-50` + `python3 -m pip install .`  
_Last command run from the root of project's directory. May not work python3 (usually on Windows), then use_ `python`  
## _How it works_
Used flag _-h_
```
usage: gendiff [-h] [-f FORMAT] first_file second_file
Compares two configuration files and show a difference.

positional arguments:
  first_file
  second_file

options:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output 
```  
You can select one of three output styles format: _PLAIN_, _STYLISH_(default), _JSON_.  
After the command `gendiff` you must specify the paths to the files being compared, you can compare files of both the same format   
and different ones. Incoming formats are only yml and json. The program works with "flat" and "tree" structures.  
## _Examples_
Comparison of flat _JSON_ files
![](https://raw.githubusercontent.com/spacewalrus73/Gifs/master/gif_2prj/first_gif_of_second_project.gif)  
****
Comparison of flat _YAML_ files  
![](https://raw.githubusercontent.com/spacewalrus73/Gifs/master/gif_2prj/yml_gif.gif)  
***
Recursive comparison of nested _JSON_ files  
![](https://raw.githubusercontent.com/spacewalrus73/Gifs/master/gif_2prj/json.gif)  
***
Recursive comparison of nested _YAML_ files  
![](https://raw.githubusercontent.com/spacewalrus73/Gifs/master/gif_2prj/yaml.gif)  
***
Plain format of two nested files  
![](https://raw.githubusercontent.com/spacewalrus73/Gifs/master/gif_2prj/plain.gif)  
***
Output _JSON_ format  
![](https://raw.githubusercontent.com/spacewalrus73/Gifs/master/gif_2prj/json_f.gif)