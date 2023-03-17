# MERTS-Modded-NERTS

This is an unoffical mod project for the game NERTS! Online.

First of all, you should own this game, you can buy it on [steam](https://store.steampowered.com/app/1131190/NERTS_Online/).

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

* copy the ``Packed`` folder from the game directory, typically located in ``C:\Program Files (x86)\Steam\steamapps\common\Nerts Online\Content`` and paste it in the  ``./images/`` folder of the mod directory

# Modify the textures
Run ``images/export_texture.py`` 

It will look directory in the ``images/Packed`` folder and convert all .tex files to .png into the directory ``pngOutput``.

Change the images that you want to modify. (Don't worry about editing the ``half`` and the ``fonts`` folder, as it gets automatically created later on)

Put all of the new textures in the `new` dirctory, and keep the same structure as the Packed folder. Names and everything. Should look like ``.\new\Packed\textures``.

Run ``convert.bat``, and the .tex files will be created including the ``half`` folder. They will be located in the ``patch`` directory.

copy the .tex files back into the NERTS! game directory, make sure to not just delete the ``texture`` folder already in the game as there are some files that shouldn't be deleted.

## Things to Note

Be careful when dealing with the vignette.tex as it typically doesn't look good when chaning the hue. (from what I've tested)

Make sure to also copy over the half files that get generated. As they are what seem to ascually change the look ingame.

All textures you modify are client sided so others won't see your changes. That includes card fronts and backs.
