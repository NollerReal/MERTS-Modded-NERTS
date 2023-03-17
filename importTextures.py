#Code originally from noword on Github
#edited by NollerReal

import os
from tex import Tex
from PIL import Image

if __name__ == '__main__':
    for root, dirs, files in os.walk('Packed'):
        for f in files:
            if os.path.splitext(f)[1].lower() == '.tex':
                name = os.path.join(root, f)
                new_name = os.path.join('new', name).replace('.tex', '.png')
                tex = None
                if os.path.exists(new_name):
                    print(name)
                    tex = Tex(open(name, 'rb'))
                    tex.image = Image.open(new_name)
                    patch_name = '../patch/' + name
                else:
                    new_name = new_name.replace('half', '')
                    if os.path.exists(new_name):
                        print(name)
                        tex = Tex(open(name, 'rb'))
                        tex.image = Image.open(new_name).resize((tex.width, tex.height))
                        patch_name = '../patch/' + name
                if tex is not None:
                    try:
                        os.makedirs(os.path.split(patch_name)[0])
                    except BaseException:
                        pass
                    tex.save(open(patch_name, 'wb'))
