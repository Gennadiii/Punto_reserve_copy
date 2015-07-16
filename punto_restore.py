import shutil
import os.path
from datetime import datetime

shutil.rmtree(os.path.expanduser(r'~\AppData\Roaming\Yandex\Punto Switcher\User Data'))

file_name = open(os.path.expanduser(r'~\Dropbox\Volk\Back-up\punto\date.txt'), 'r')
date = file_name.readline()
file_name.close()

shutil.copytree(os.path.expanduser(r'~\Dropbox\Volk\Back-up\punto' + '\\' + str(date) + '\\' + 'User Data'), \
	os.path.expanduser(r'~\AppData\Roaming\Yandex\Punto Switcher\User Data'))
