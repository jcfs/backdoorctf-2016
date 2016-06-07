# BusyBee - Writeup

## Problem text

A deadly virus is killing bees in Busybee's village Busybox, India. Unfortuantely, you have to go to the village to fight the infection. Get the flag virus out of the infected files. 
Village address: http://hack.bckdr.in/BUSYBEE/infected.tar

## Solution

Downloading the infected tar we get the following file structure

```
~/fun/ctf/backdoorctf-2016/busybee$ tree
.
├── 2b0fbc0e1ac044737fd881cff8164bb5a2c7bfbf90c40c87de3c3435f2c6a94e
│   ├── json
│   ├── layer.tar
│   └── VERSION
├── 983179bdb58ea980ec1fe7c45f63571d49b140bdd629f234be9c00a6edd8a4a7
│   ├── json
│   ├── layer.tar
│   └── VERSION
├── d51a083a3b01fe8c58086903595b91fc975de59a9e9ececec755df384a181026
│   ├── json
│   ├── layer.tar
│   └── VERSION
├── eaa21323de5e2cce7078df3af4dd292181114dfc94be761b948657efbe3af26b.json
├── manifest.json
└── repositories
```
This structure is the structure of a docker image (https://github.com/docker/docker/blob/master/image/spec/v1.md). Lets try to install the image locally and to see what it is.

```
~/fun/ctf/backdoorctf-2016/busybee$ docker load < infected.tar
~/fun/ctf/backdoorctf-2016/busybee$ sudo docker images
REPOSITORY                TAG                 IMAGE ID            CREATED             SIZE
busybox-1.24.1-infected   latest              eaa21323de5e        4 days ago          2.144 MB
```

Nice, it worked. The next step is try to run 

```
/fun/ctf/backdoorctf-2016/busybee$ sudo docker run -i -t busybox-1.24.1-infected /bin/sh
/ # id
uid=0(root) gid=0(root) groups=10(wheel)
/ # 
```

Since the problem text mentions a "deadly virus", the first guess is trying to see if any of the binaries on the system are infected.

```
~ # ls -l /bin/
(...)
-rwxr-xr-x  365 root     root       1031256 Mar 15 19:38 setfont
-rwxr-xr-x  365 root     root       1031256 Mar 15 19:38 setkeycodes
-rwxr-xr-x  365 root     root       1031256 Mar 15 19:38 setlogcons
-rwxr-xr-x  365 root     root       1031256 Mar 15 19:38 setserial
-rwxr-xr-x  365 root     root       1031256 Mar 15 19:38 setsid
-rwxr-xr-x  365 root     root       1031256 Mar 15 19:38 setuidgid
-rwxr-xr-x  365 root     root       1031256 Mar 15 19:38 sh
-rwxr-xr-x    2 root     root       1031328 Jun  3 16:11 sha1sum
-rwxr-xr-x  365 root     root       1031256 Mar 15 19:38 sha256sum
-rwxr-xr-x  365 root     root       1031256 Mar 15 19:38 sha3sum
-rwxr-xr-x  365 root     root       1031256 Mar 15 19:38 sha512sum
-rwxr-xr-x  365 root     root       1031256 Mar 15 19:38 showkey
-rwxr-xr-x  365 root     root       1031256 Mar 15 19:38 shuf
-rwxr-xr-x  365 root     root       1031256 Mar 15 19:38 slattach
(...)
```

Hmm, the sha1sum binary was changed (all the other binaries on the directory have the same date), lets try our luck...

```
~ # strings /bin/sha1sum
(...)
THIS IS WHAT YOU ARE LOOKING FOR:    ?????????????????????????????????????? (find it yourself)
```

And voilá - we get the flag


