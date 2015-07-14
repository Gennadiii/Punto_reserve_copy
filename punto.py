import shutil
import os.path
from datetime import datetime

shutil.copytree(os.path.expanduser(r'~\AppData\Roaming\Yandex\Punto Switcher\User Data'), os.path.expanduser(r'~\Dropbox\Volk\Back-up\punto' + '\\' + str(datetime.now().date())))
