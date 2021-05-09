import io
import subprocess
import sys
import zipfile
from time import sleep

import requests
from progress.bar import Bar


def main():
    url_patch = "https://raw.githubusercontent.com/inframbot/inframbot-autodownloader/main/Infram.zip"
    print("\nDownloading the patch...\n")
    bar = Bar('b/s', max=100)

    def progress(percent_max):
        for num in range(percent_max):
            sleep(0.06)
            bar.next()

    progress(10)
    r_patch = requests.get(url_patch, stream=True)
    progress(20)
    check = zipfile.is_zipfile(io.BytesIO(r_patch.content))
    progress(20)
    while not check:
        r_patch = requests.get(url_patch, stream=True)
        check = zipfile.is_zipfile(io.BytesIO(r_patch.content))
    else:
        progress(20)
        z = zipfile.ZipFile(io.BytesIO(r_patch.content))
        progress(20)
        z.extractall()
    progress(10)
    bar.finish()

    subprocess.Popen("cmd /c start Infram.exe")
    sys.exit(0)


if __name__ == '__main__':
    main()
