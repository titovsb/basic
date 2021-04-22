import os, sys

sys.path.append(os.getcwd())

import md
from rd import RemoveDir
import mylist as ml

md.MakeDir()
RemoveDir()
print(ml.ShowRandomElement(range(10)))
