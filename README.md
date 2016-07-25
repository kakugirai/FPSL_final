# FUNDAMENTALS OF PROGRAMMING WITH SCRIPT LANGUAGES FINAL PROJECT
## Introduction
This project aims to build an api for [SFC Course Summary](http://vu.sfc.keio.ac.jp/course_u/data/2016/title14_en.html).
Several useful functions like downloading, parsing HTML and courses searching are provided.

## Installation
### My Python environment
```sh
$ python -V
Python 2.7.11 :: Anaconda 4.0.0 (x86_64)
```
### make
```sh
$ make
```

## Example
```sh
$ python final.py --search ucu
+---------------+---------------------------------------------------+
| Course Number |                       B4005                       |
+---------------+---------------------------------------------------+
|  Course Name  | FUNDAMENTALS OF PROGRAMMING WITH SCRIPT LANGUAGES |
|    Teacher    |                    Ucu Maksudi                    |
|  Full or Half |                   Full Semester                   |
|    Semester   |                       Spring                      |
|  GIGA or not  |                        GIGA                       |
|      Time     |                 Tuesday 2nd Period                |
|    Language   |                      English                      |
+---------------+---------------------------------------------------+
```
## Current Problems
- Only one teacher can be added to teacher information list because of some encoding problems.