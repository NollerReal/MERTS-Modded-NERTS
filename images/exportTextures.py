#Code originally from noword on Github
#edited by NollerReal

import os
from tex import Tex

if __name__ == '__main__':
    for root, dirs, files in os.walk('Packed'):
        for f in files:
            if os.path.splitext(f)[1].lower() == '.tex':
                name = os.path.join(root, f)
                out_name = os.path.join('pngOutput', name).replace('.tex', '.png')
                print(name)
                tex = Tex(open(name, 'rb'))
                try:
                    os.makedirs(os.path.split(out_name)[0])
                except BaseException:
                    pass
                tex.image.save(out_name)
