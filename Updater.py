import io
import subprocess
import sys
import zipfile
from time import sleep

import requests
from progress.bar import Bar


def main():
    url_patch = "https://raw.githubusercontent.com/gianca1994/test/main/Infram.zip"
    print("\nDownloading the patch...\n")

    bar = Bar('b/s', max=100)

    for num in range(43):
        sleep(0.06)
        bar.next()

    r_patch = requests.get(url_patch, stream=True)
    check = zipfile.is_zipfile(io.BytesIO(r_patch.content))

    while not check:
        r_patch = requests.get(url_patch, stream=True)
        check = zipfile.is_zipfile(io.BytesIO(r_patch.content))
    else:
        z = zipfile.ZipFile(io.BytesIO(r_patch.content))
        z.extractall()

    for num in range(57):
        sleep(0.03)
        bar.next()

    bar.finish()

    subprocess.Popen("cmd /c start Infram.exe")
    sys.exit(0)


if __name__ == '__main__':
    main()
