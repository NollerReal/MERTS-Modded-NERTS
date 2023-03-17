# MERTS-Modded-NERTS

This is an unoffical mod project for the game NERTS! Online.

First at all, you should own this game, you can buy it on [steam](https://store.steampowered.com/app/1131190/NERTS_Online/).

# Prepare the Environment
## 1. Install [python](https://www.python.org/) and some dependent libraries.

* install python 3 from their [website](https://www.python.org/downloads/) or from the Windows Store App

* install [pandas](https://pandas.pydata.org/)
  ```
  pip install pandas
  ```
* install [openpyxl](https://openpyxl.readthedocs.io/en/stable/)
  ```
  pip install openpyxl
  ```
* install [pillow](https://python-pillow.org/)
  ```
  pip install pillow
  ```
* install [python-lz4](https://github.com/python-lz4/python-lz4)
  ```
  pip install lz4
  ```
  
## 2. copy game files to MERTS working directory

* copy ``Packed/*.tex`` to ``./images/Packed``

# Modify the textures
Run ``images/export_texture.py`` 

It will traverse directory ``images/Packed``, convert all .tex files to .png into the directory ``out``.

Pick up the images what you want to modify. (No need for ``half``'s, they will be generated  automatically.)

Put all of them in the `new` dirctory, keep the same directory struct.

Run ``run.bat``, the patch folder with the new .tex files will be generated in ``patch`` directory.
