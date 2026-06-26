ubuntu@ip-172-31-2-102:~/CKAN-custom/test-infrastructure$ docker compose build --parallel
ubuntu@ip-172-31-2-102:~/CKAN-custom/test-infrastructure$ docker compose up -d
[+] Running 4/4
 ✔ Container test-infrastructure-ckan-postgres-1  Running                                                    0.0s 
 ✔ Container test-infrastructure-ckan-solr-1      Running                                                    0.0s 
 ✔ Container test-infrastructure-ckan-redis-1     Running                                                    0.0s 
 ✔ Container test-infrastructure-ckan-1           Started                                                   11.2s 
ubuntu@ip-172-31-2-102:~/CKAN-custom/test-infrastructure$ ./setup.sh 
[+] Running 4/4
 ✔ Container test-infrastructure-ckan-solr-1      Running                                                    0.0s 
 ✔ Container test-infrastructure-ckan-postgres-1  Running                                                    0.0s 
 ✔ Container test-infrastructure-ckan-1           Running                                                    0.0s 
 ✔ Container test-infrastructure-ckan-redis-1     Running                                                    0.0s 
Get:1 http://deb.debian.org/debian bookworm InRelease [151 kB]
Get:2 http://deb.debian.org/debian bookworm-updates InRelease [55.4 kB]
Get:3 http://deb.debian.org/debian-security bookworm-security InRelease [48.0 kB]
Get:4 http://deb.debian.org/debian bookworm/main amd64 Packages [8790 kB]
Get:5 http://deb.debian.org/debian bookworm-updates/main amd64 Packages [6924 B]
Get:6 http://deb.debian.org/debian-security bookworm-security/main amd64 Packages [313 kB]
Fetched 9364 kB in 1s (6724 kB/s)                    
Reading package lists... Done
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  postgresql-client-15 postgresql-client-common
Suggested packages:
  postgresql-15 postgresql-doc-15
The following NEW packages will be installed:
  postgresql-client postgresql-client-15 postgresql-client-common
0 upgraded, 3 newly installed, 0 to remove and 0 not upgraded.
Need to get 1792 kB of archives.
After this operation, 8637 kB of additional disk space will be used.
Get:1 http://deb.debian.org/debian bookworm/main amd64 postgresql-client-common all 248+deb12u1 [35.2 kB]
Get:2 http://deb.debian.org/debian-security bookworm-security/main amd64 postgresql-client-15 amd64 15.18-0+deb12u1 [1747 kB]
Get:3 http://deb.debian.org/debian bookworm/main amd64 postgresql-client all 15+248+deb12u1 [10.2 kB]
Fetched 1792 kB in 0s (47.8 MB/s)             
debconf: delaying package configuration, since apt-utils is not installed
Selecting previously unselected package postgresql-client-common.
(Reading database ... 23971 files and directories currently installed.)
Preparing to unpack .../postgresql-client-common_248+deb12u1_all.deb ...
Unpacking postgresql-client-common (248+deb12u1) ...
Selecting previously unselected package postgresql-client-15.
Preparing to unpack .../postgresql-client-15_15.18-0+deb12u1_amd64.deb ...
Unpacking postgresql-client-15 (15.18-0+deb12u1) ...
Selecting previously unselected package postgresql-client.
Preparing to unpack .../postgresql-client_15+248+deb12u1_all.deb ...
Unpacking postgresql-client (15+248+deb12u1) ...
Setting up postgresql-client-common (248+deb12u1) ...
Setting up postgresql-client-15 (15.18-0+deb12u1) ...
update-alternatives: using /usr/share/postgresql/15/man/man1/psql.1.gz to provide /usr/share/man/man1/psql.1.gz (psql.1.gz) in auto mode
Setting up postgresql-client (15+248+deb12u1) ...
WARNING: The directory '/usr/src/.cache/pip' or its parent directory is not owned or is not writable by the current user. The cache has been disabled. Check the permissions and owner of that directory. If executing pip with sudo, you should use sudo's -H flag.
Requirement already satisfied: pip in /usr/local/lib/python3.10/site-packages (23.0.1)
Collecting pip
  Downloading pip-26.1.2-py3-none-any.whl (1.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 43.1 MB/s eta 0:00:00
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 23.0.1
    Uninstalling pip-23.0.1:
      Successfully uninstalled pip-23.0.1
Successfully installed pip-26.1.2
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
WARNING: The directory '/usr/src/.cache/pip' or its parent directory is not owned or is not writable by the current user. The cache has been disabled. Check the permissions and owner of that directory. If executing pip with sudo, you should use sudo's -H flag.
Requirement already satisfied: setuptools in /usr/local/lib/python3.10/site-packages (79.0.1)
Collecting setuptools
  Downloading setuptools-82.0.1-py3-none-any.whl.metadata (6.5 kB)
Downloading setuptools-82.0.1-py3-none-any.whl (1.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.0/1.0 MB 65.8 MB/s  0:00:00
Installing collected packages: setuptools
  Attempting uninstall: setuptools
    Found existing installation: setuptools 79.0.1
    Uninstalling setuptools-79.0.1:
      Successfully uninstalled setuptools-79.0.1
Successfully installed setuptools-82.0.1
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager, possibly rendering your system unusable. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv. Use the --root-user-action option if you know what you are doing and want to suppress this warning.
WARNING: The directory '/usr/src/.cache/pip' or its parent directory is not owned or is not writable by the current user. The cache has been disabled. Check the permissions and owner of that directory. If executing pip with sudo, you should use sudo's -H flag.
Collecting alembic==1.18.4 (from -r requirements.txt (line 7))
  Downloading alembic-1.18.4-py3-none-any.whl.metadata (7.2 kB)
Collecting async-timeout==5.0.1 (from -r requirements.txt (line 9))
  Downloading async_timeout-5.0.1-py3-none-any.whl.metadata (5.1 kB)
Collecting babel==2.18.0 (from -r requirements.txt (line 11))
  Downloading babel-2.18.0-py3-none-any.whl.metadata (2.2 kB)
Collecting bleach==6.3.0 (from -r requirements.txt (line 15))
  Downloading bleach-6.3.0-py3-none-any.whl.metadata (31 kB)
Collecting blinker==1.9.0 (from -r requirements.txt (line 17))
  Downloading blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
Collecting cachelib==0.13.0 (from -r requirements.txt (line 21))
  Downloading cachelib-0.13.0-py3-none-any.whl.metadata (2.0 kB)
Collecting certifi==2026.2.25 (from -r requirements.txt (line 23))
  Downloading certifi-2026.2.25-py3-none-any.whl.metadata (2.5 kB)
Collecting charset-normalizer==3.4.7 (from -r requirements.txt (line 27))
  Downloading charset_normalizer-3.4.7-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (40 kB)
Collecting click==8.1.8 (from -r requirements.txt (line 29))
  Downloading click-8.1.8-py3-none-any.whl.metadata (2.3 kB)
Collecting croniter==6.2.2 (from -r requirements.txt (line 34))
  Downloading croniter-6.2.2-py3-none-any.whl.metadata (22 kB)
Collecting dominate==2.9.1 (from -r requirements.txt (line 36))
  Downloading dominate-2.9.1-py2.py3-none-any.whl.metadata (13 kB)
Collecting feedgen==1.0.0 (from -r requirements.txt (line 38))
  Downloading feedgen-1.0.0.tar.gz (258 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting file-keeper==0.2.4 (from -r requirements.txt (line 40))
  Downloading file_keeper-0.2.4-py3-none-any.whl.metadata (6.8 kB)
Collecting flask==3.1.3 (from -r requirements.txt (line 42))
  Downloading flask-3.1.3-py3-none-any.whl.metadata (3.2 kB)
Collecting flask-babel==4.0.0 (from -r requirements.txt (line 49))
  Downloading flask_babel-4.0.0-py3-none-any.whl.metadata (1.9 kB)
Collecting flask-login==0.6.3 (from -r requirements.txt (line 51))
  Downloading Flask_Login-0.6.3-py3-none-any.whl.metadata (5.8 kB)
Collecting flask-session==0.8.0 (from -r requirements.txt (line 53))
  Downloading flask_session-0.8.0-py3-none-any.whl.metadata (5.2 kB)
Collecting flask-wtf==1.2.2 (from -r requirements.txt (line 55))
  Downloading flask_wtf-1.2.2-py3-none-any.whl.metadata (3.4 kB)
Collecting greenlet==3.4.0 (from -r requirements.txt (line 57))
  Downloading greenlet-3.4.0-cp310-cp310-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (3.7 kB)
Collecting idna==3.11 (from -r requirements.txt (line 59))
  Downloading idna-3.11-py3-none-any.whl.metadata (8.4 kB)
Collecting itsdangerous==2.2.0 (from -r requirements.txt (line 61))
  Downloading itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting jinja2==3.1.6 (from -r requirements.txt (line 65))
  Downloading jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting lxml==6.1.0 (from -r requirements.txt (line 70))
  Downloading lxml-6.1.0-cp310-cp310-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl.metadata (4.0 kB)
Collecting mako==1.3.11 (from -r requirements.txt (line 72))
  Downloading mako-1.3.11-py3-none-any.whl.metadata (2.9 kB)
Collecting markdown==3.10.2 (from -r requirements.txt (line 74))
  Downloading markdown-3.10.2-py3-none-any.whl.metadata (5.1 kB)
Collecting markupsafe==3.0.3 (from -r requirements.txt (line 76))
  Downloading markupsafe-3.0.3-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.7 kB)
Collecting msgspec==0.21.1 (from -r requirements.txt (line 83))
  Downloading msgspec-0.21.1-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (5.8 kB)
Collecting packaging==26.1 (from -r requirements.txt (line 87))
  Downloading packaging-26.1-py3-none-any.whl.metadata (3.5 kB)
Collecting passlib==1.7.4 (from -r requirements.txt (line 89))
  Downloading passlib-1.7.4-py2.py3-none-any.whl.metadata (1.7 kB)
Collecting pluggy==1.6.0 (from -r requirements.txt (line 91))
  Downloading pluggy-1.6.0-py3-none-any.whl.metadata (4.8 kB)
Collecting polib==1.2.0 (from -r requirements.txt (line 93))
  Downloading polib-1.2.0-py2.py3-none-any.whl.metadata (15 kB)
Collecting psycopg2==2.9.11 (from -r requirements.txt (line 95))
  Downloading psycopg2-2.9.11.tar.gz (379 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting pyjwt==2.12.1 (from -r requirements.txt (line 97))
  Downloading pyjwt-2.12.1-py3-none-any.whl.metadata (4.1 kB)
Collecting pyparsing==3.3.2 (from -r requirements.txt (line 99))
  Downloading pyparsing-3.3.2-py3-none-any.whl.metadata (5.8 kB)
Collecting pysolr==3.11.0 (from -r requirements.txt (line 101))
  Downloading pysolr-3.11.0.tar.gz (63 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Installing backend dependencies ... done
  Preparing metadata (pyproject.toml) ... done
Collecting python-dateutil==2.9.0.post0 (from -r requirements.txt (line 103))
  Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting python-magic==0.4.27 (from -r requirements.txt (line 108))
  Downloading python_magic-0.4.27-py2.py3-none-any.whl.metadata (5.8 kB)
Collecting pytz==2026.1.post1 (from -r requirements.txt (line 112))
  Downloading pytz-2026.1.post1-py2.py3-none-any.whl.metadata (22 kB)
Collecting pyyaml==6.0.3 (from -r requirements.txt (line 116))
  Downloading pyyaml-6.0.3-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.4 kB)
Collecting redis==7.4.0 (from -r requirements.txt (line 120))
  Downloading redis-7.4.0-py3-none-any.whl.metadata (12 kB)
Collecting requests==2.33.1 (from -r requirements.txt (line 122))
  Downloading requests-2.33.1-py3-none-any.whl.metadata (4.8 kB)
Collecting rq==2.8.0 (from -r requirements.txt (line 126))
  Downloading rq-2.8.0-py3-none-any.whl.metadata (10 kB)
Collecting simplejson==4.0.1 (from -r requirements.txt (line 128))
  Downloading simplejson-4.0.1-cp310-cp310-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (3.8 kB)
Collecting six==1.17.0 (from -r requirements.txt (line 130))
  Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Collecting sqlalchemy==2.0.49 (from -r requirements.txt (line 132))
  Downloading sqlalchemy-2.0.49-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (9.5 kB)
Collecting sqlparse==0.5.5 (from -r requirements.txt (line 136))
  Downloading sqlparse-0.5.5-py3-none-any.whl.metadata (4.7 kB)
Collecting tomli==2.4.1 (from -r requirements.txt (line 138))
  Downloading tomli-2.4.1-py3-none-any.whl.metadata (10 kB)
Collecting typing-extensions==4.15.0 (from -r requirements.txt (line 140))
  Downloading typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
Collecting tzlocal==5.3.1 (from -r requirements.txt (line 147))
  Downloading tzlocal-5.3.1-py3-none-any.whl.metadata (7.6 kB)
Collecting urllib3==2.6.3 (from -r requirements.txt (line 149))
  Downloading urllib3-2.6.3-py3-none-any.whl.metadata (6.9 kB)
Collecting watchdog==6.0.0 (from -r requirements.txt (line 151))
  Downloading watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl.metadata (44 kB)
Collecting webassets==3.0.0 (from -r requirements.txt (line 153))
  Downloading webassets-3.0.0-py3-none-any.whl.metadata (2.8 kB)
Collecting webencodings==0.5.1 (from -r requirements.txt (line 155))
  Downloading webencodings-0.5.1-py2.py3-none-any.whl.metadata (2.1 kB)
Collecting werkzeug==3.1.8 (from werkzeug[watchdog]==3.1.8->-r requirements.txt (line 157))
  Downloading werkzeug-3.1.8-py3-none-any.whl.metadata (4.0 kB)
Collecting wtforms==3.2.1 (from -r requirements.txt (line 163))
  Downloading wtforms-3.2.1-py3-none-any.whl.metadata (5.3 kB)
Collecting zope-dottedname==7.1 (from -r requirements.txt (line 165))
  Downloading zope_dottedname-7.1-py3-none-any.whl.metadata (4.2 kB)
Collecting zope-interface==8.3 (from -r requirements.txt (line 167))
  Downloading zope_interface-8.3-cp310-cp310-manylinux1_x86_64.manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_5_x86_64.whl.metadata (46 kB)
Requirement already satisfied: setuptools in /usr/local/lib/python3.10/site-packages (from pysolr==3.11.0->-r requirements.txt (line 101)) (82.0.1)
Downloading alembic-1.18.4-py3-none-any.whl (263 kB)
Downloading async_timeout-5.0.1-py3-none-any.whl (6.2 kB)
Downloading babel-2.18.0-py3-none-any.whl (10.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.2/10.2 MB 239.0 MB/s  0:00:00
Downloading bleach-6.3.0-py3-none-any.whl (164 kB)
Downloading blinker-1.9.0-py3-none-any.whl (8.5 kB)
Downloading cachelib-0.13.0-py3-none-any.whl (20 kB)
Downloading certifi-2026.2.25-py3-none-any.whl (153 kB)
Downloading charset_normalizer-3.4.7-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (216 kB)
Downloading click-8.1.8-py3-none-any.whl (98 kB)
Downloading croniter-6.2.2-py3-none-any.whl (45 kB)
Downloading dominate-2.9.1-py2.py3-none-any.whl (29 kB)
Downloading file_keeper-0.2.4-py3-none-any.whl (69 kB)
Downloading flask-3.1.3-py3-none-any.whl (103 kB)
Downloading flask_babel-4.0.0-py3-none-any.whl (9.6 kB)
Downloading Flask_Login-0.6.3-py3-none-any.whl (17 kB)
Downloading flask_session-0.8.0-py3-none-any.whl (24 kB)
Downloading flask_wtf-1.2.2-py3-none-any.whl (12 kB)
Downloading greenlet-3.4.0-cp310-cp310-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (611 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 612.0/612.0 kB 542.0 MB/s  0:00:00
Downloading idna-3.11-py3-none-any.whl (71 kB)
Downloading itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Downloading jinja2-3.1.6-py3-none-any.whl (134 kB)
Downloading lxml-6.1.0-cp310-cp310-manylinux_2_26_x86_64.manylinux_2_28_x86_64.whl (5.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.3/5.3 MB 129.0 MB/s  0:00:00
Downloading mako-1.3.11-py3-none-any.whl (78 kB)
Downloading markdown-3.10.2-py3-none-any.whl (108 kB)
Downloading markupsafe-3.0.3-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (20 kB)
Downloading msgspec-0.21.1-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (222 kB)
Downloading packaging-26.1-py3-none-any.whl (95 kB)
Downloading passlib-1.7.4-py2.py3-none-any.whl (525 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 525.6/525.6 kB 525.4 MB/s  0:00:00
Downloading pluggy-1.6.0-py3-none-any.whl (20 kB)
Downloading polib-1.2.0-py2.py3-none-any.whl (20 kB)
Downloading pyjwt-2.12.1-py3-none-any.whl (29 kB)
Downloading pyparsing-3.3.2-py3-none-any.whl (122 kB)
Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Downloading python_magic-0.4.27-py2.py3-none-any.whl (13 kB)
Downloading pytz-2026.1.post1-py2.py3-none-any.whl (510 kB)
Downloading pyyaml-6.0.3-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (770 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 770.3/770.3 kB 399.4 MB/s  0:00:00
Downloading redis-7.4.0-py3-none-any.whl (409 kB)
Downloading requests-2.33.1-py3-none-any.whl (64 kB)
Downloading urllib3-2.6.3-py3-none-any.whl (131 kB)
Downloading rq-2.8.0-py3-none-any.whl (119 kB)
Downloading simplejson-4.0.1-cp310-cp310-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (165 kB)
Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
Downloading sqlalchemy-2.0.49-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (3.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.2/3.2 MB 346.4 MB/s  0:00:00
Downloading sqlparse-0.5.5-py3-none-any.whl (46 kB)
Downloading tomli-2.4.1-py3-none-any.whl (14 kB)
Downloading typing_extensions-4.15.0-py3-none-any.whl (44 kB)
Downloading tzlocal-5.3.1-py3-none-any.whl (18 kB)
Downloading watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl (79 kB)
Downloading webassets-3.0.0-py3-none-any.whl (142 kB)
Downloading webencodings-0.5.1-py2.py3-none-any.whl (11 kB)
Downloading werkzeug-3.1.8-py3-none-any.whl (226 kB)
Downloading wtforms-3.2.1-py3-none-any.whl (152 kB)
Downloading zope_dottedname-7.1-py3-none-any.whl (6.0 kB)
Downloading zope_interface-8.3-cp310-cp310-manylinux1_x86_64.manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_5_x86_64.whl (258 kB)
Building wheels for collected packages: feedgen, psycopg2, pysolr
  Building wheel for feedgen (pyproject.toml) ... done
  Created wheel for feedgen: filename=feedgen-1.0.0-py2.py3-none-any.whl size=45393 sha256=735c88a8f995a21eb1478794784ca8de045cbc50c1ca2bbdd23a470b7c594f75
  Stored in directory: /tmp/pip-ephem-wheel-cache-gjnbch4r/wheels/c8/6a/ca/669bc8c68b06dae2638b85a110fb7b341b635dcd33f2d78650
  Building wheel for psycopg2 (pyproject.toml) ... done
  Created wheel for psycopg2: filename=psycopg2-2.9.11-cp310-cp310-linux_x86_64.whl size=483213 sha256=22e6c789f3de5a7272b1f1ba1f565bef410ec2dd6f5e877cb829365e052875e9
  Stored in directory: /tmp/pip-ephem-wheel-cache-gjnbch4r/wheels/ef/c7/1c/9c6a8c0c80fc6713248040b66f381cbd07b64ef067ceba5da2
  Building wheel for pysolr (pyproject.toml) ... done
  Created wheel for pysolr: filename=pysolr-3.11.0-py3-none-any.whl size=19633 sha256=99b0c4cb26c92b3780eb76dba76e1aa6a13d77505cf5d4c7c5e737bc0a4a1895
  Stored in directory: /tmp/pip-ephem-wheel-cache-gjnbch4r/wheels/2c/9f/07/2c9c1ba33a097184f08fb12e2d2141efa72ceadaeff213468e
Successfully built feedgen psycopg2 pysolr
Installing collected packages: webencodings, pytz, polib, passlib, zope-interface, zope-dottedname, watchdog, urllib3, tzlocal, typing-extensions, tomli, sqlparse, six, simplejson, pyyaml, python-magic, pyparsing, psycopg2, pluggy, packaging, msgspec, markupsafe, markdown, lxml, itsdangerous, idna, greenlet, dominate, click, charset-normalizer, certifi, cachelib, blinker, bleach, babel, async-timeout, wtforms, werkzeug, webassets, sqlalchemy, requests, redis, python-dateutil, pyjwt, mako, jinja2, file-keeper, pysolr, flask, feedgen, croniter, alembic, rq, flask-wtf, flask-session, flask-login, flask-babel
Successfully installed alembic-1.18.4 async-timeout-5.0.1 babel-2.18.0 bleach-6.3.0 blinker-1.9.0 cachelib-0.13.0 certifi-2026.2.25 charset-normalizer-3.4.7 click-8.1.8 croniter-6.2.2 dominate-2.9.1 feedgen-1.0.0 file-keeper-0.2.4 flask-3.1.3 flask-babel-4.0.0 flask-login-0.6.3 flask-session-0.8.0 flask-wtf-1.2.2 greenlet-3.4.0 idna-3.11 itsdangerous-2.2.0 jinja2-3.1.6 lxml-6.1.0 mako-1.3.11 markdown-3.10.2 markupsafe-3.0.3 msgspec-0.21.1 packaging-26.1 passlib-1.7.4 pluggy-1.6.0 polib-1.2.0 psycopg2-2.9.11 pyjwt-2.12.1 pyparsing-3.3.2 pysolr-3.11.0 python-dateutil-2.9.0.post0 python-magic-0.4.27 pytz-2026.1.post1 pyyaml-6.0.3 redis-7.4.0 requests-2.33.1 rq-2.8.0 simplejson-4.0.1 six-1.17.0 sqlalchemy-2.0.49 sqlparse-0.5.5 tomli-2.4.1 typing-extensions-4.15.0 tzlocal-5.3.1 urllib3-2.6.3 watchdog-6.0.0 webassets-3.0.0 webencodings-0.5.1 werkzeug-3.1.8 wtforms-3.2.1 zope-dottedname-7.1 zope-interface-8.3
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager, possibly rendering your system unusable. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv. Use the --root-user-action option if you know what you are doing and want to suppress this warning.
WARNING: The directory '/usr/src/.cache/pip' or its parent directory is not owned or is not writable by the current user. The cache has been disabled. Check the permissions and owner of that directory. If executing pip with sudo, you should use sudo's -H flag.
Collecting beautifulsoup4==4.14.3 (from -r dev-requirements.txt (line 4))
  Downloading beautifulsoup4-4.14.3-py3-none-any.whl.metadata (3.8 kB)
Collecting cookiecutter==2.7.1 (from -r dev-requirements.txt (line 5))
  Downloading cookiecutter-2.7.1-py3-none-any.whl.metadata (7.3 kB)
Collecting coverage==7.13.5 (from -r dev-requirements.txt (line 6))
  Downloading coverage-7.13.5-cp310-cp310-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (8.5 kB)
Collecting factory-boy==3.3.3 (from -r dev-requirements.txt (line 7))
  Downloading factory_boy-3.3.3-py2.py3-none-any.whl.metadata (15 kB)
Collecting Faker==40.15.0 (from -r dev-requirements.txt (line 8))
  Downloading faker-40.15.0-py3-none-any.whl.metadata (16 kB)
Collecting flask-debugtoolbar==0.16.0 (from -r dev-requirements.txt (line 9))
  Downloading flask_debugtoolbar-0.16.0-py3-none-any.whl.metadata (2.0 kB)
Collecting freezegun==1.5.5 (from -r dev-requirements.txt (line 10))
  Downloading freezegun-1.5.5-py3-none-any.whl.metadata (13 kB)
Collecting ipdb==0.13.13 (from -r dev-requirements.txt (line 11))
  Downloading ipdb-0.13.13-py3-none-any.whl.metadata (14 kB)
Collecting junit2html==31.0.5 (from -r dev-requirements.txt (line 12))
  Downloading junit2html-31.0.5-py3-none-any.whl.metadata (423 bytes)
Collecting junitparser==5.0.0 (from -r dev-requirements.txt (line 13))
  Downloading junitparser-5.0.0-py3-none-any.whl.metadata (9.6 kB)
Collecting Pillow==12.2.0 (from -r dev-requirements.txt (line 14))
  Downloading pillow-12.2.0-cp310-cp310-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (8.8 kB)
Collecting pip-tools==7.5.3 (from -r dev-requirements.txt (line 15))
  Downloading pip_tools-7.5.3-py3-none-any.whl.metadata (27 kB)
Collecting pytest-cov==7.1.0 (from -r dev-requirements.txt (line 16))
  Downloading pytest_cov-7.1.0-py3-none-any.whl.metadata (32 kB)
Collecting pytest-factoryboy==2.8.1 (from -r dev-requirements.txt (line 17))
  Downloading pytest_factoryboy-2.8.1-py3-none-any.whl.metadata (13 kB)
Collecting pytest-freezegun==0.4.2 (from -r dev-requirements.txt (line 18))
  Downloading pytest_freezegun-0.4.2-py2.py3-none-any.whl.metadata (4.5 kB)
Collecting pytest-split==0.11.0 (from -r dev-requirements.txt (line 19))
  Downloading pytest_split-0.11.0-py3-none-any.whl.metadata (9.5 kB)
Collecting pytest==9.0.3 (from -r dev-requirements.txt (line 20))
  Downloading pytest-9.0.3-py3-none-any.whl.metadata (7.6 kB)
Collecting responses==0.26.0 (from -r dev-requirements.txt (line 21))
  Downloading responses-0.26.0-py3-none-any.whl.metadata (48 kB)
Collecting sphinx-rtd-theme==3.1.0 (from -r dev-requirements.txt (line 22))
  Downloading sphinx_rtd_theme-3.1.0-py2.py3-none-any.whl.metadata (4.5 kB)
Collecting sphinx==8.1.3 (from -r dev-requirements.txt (line 23))
  Downloading sphinx-8.1.3-py3-none-any.whl.metadata (6.4 kB)
Collecting toml==0.10.2 (from -r dev-requirements.txt (line 24))
  Downloading toml-0.10.2-py2.py3-none-any.whl.metadata (7.1 kB)
Collecting towncrier==25.8.0 (from -r dev-requirements.txt (line 25))
  Downloading towncrier-25.8.0-py3-none-any.whl.metadata (4.3 kB)
Collecting soupsieve>=1.6.1 (from beautifulsoup4==4.14.3->-r dev-requirements.txt (line 4))
  Downloading soupsieve-2.8.4-py3-none-any.whl.metadata (4.6 kB)
Requirement already satisfied: typing-extensions>=4.0.0 in /usr/local/lib/python3.10/site-packages (from beautifulsoup4==4.14.3->-r dev-requirements.txt (line 4)) (4.15.0)
Collecting binaryornot>=0.4.4 (from cookiecutter==2.7.1->-r dev-requirements.txt (line 5))
  Downloading binaryornot-0.6.0-py3-none-any.whl.metadata (2.9 kB)
Requirement already satisfied: Jinja2<4.0.0,>=2.7 in /usr/local/lib/python3.10/site-packages (from cookiecutter==2.7.1->-r dev-requirements.txt (line 5)) (3.1.6)
Requirement already satisfied: click<9.0.0,>=7.0 in /usr/local/lib/python3.10/site-packages (from cookiecutter==2.7.1->-r dev-requirements.txt (line 5)) (8.1.8)
Requirement already satisfied: pyyaml>=5.3.1 in /usr/local/lib/python3.10/site-packages (from cookiecutter==2.7.1->-r dev-requirements.txt (line 5)) (6.0.3)
Collecting python-slugify>=4.0.0 (from cookiecutter==2.7.1->-r dev-requirements.txt (line 5))
  Downloading python_slugify-8.0.4-py2.py3-none-any.whl.metadata (8.5 kB)
Requirement already satisfied: requests>=2.23.0 in /usr/local/lib/python3.10/site-packages (from cookiecutter==2.7.1->-r dev-requirements.txt (line 5)) (2.33.1)
Collecting arrow (from cookiecutter==2.7.1->-r dev-requirements.txt (line 5))
  Downloading arrow-1.4.0-py3-none-any.whl.metadata (7.7 kB)
Collecting rich (from cookiecutter==2.7.1->-r dev-requirements.txt (line 5))
  Downloading rich-15.0.0-py3-none-any.whl.metadata (18 kB)
Requirement already satisfied: flask>=2.3.0 in /usr/local/lib/python3.10/site-packages (from flask-debugtoolbar==0.16.0->-r dev-requirements.txt (line 9)) (3.1.3)
Requirement already satisfied: python-dateutil>=2.7 in /usr/local/lib/python3.10/site-packages (from freezegun==1.5.5->-r dev-requirements.txt (line 10)) (2.9.0.post0)
Collecting ipython>=7.31.1 (from ipdb==0.13.13->-r dev-requirements.txt (line 11))
  Downloading ipython-8.39.0-py3-none-any.whl.metadata (5.1 kB)
Requirement already satisfied: tomli in /usr/local/lib/python3.10/site-packages (from ipdb==0.13.13->-r dev-requirements.txt (line 11)) (2.4.1)
Collecting decorator (from ipdb==0.13.13->-r dev-requirements.txt (line 11))
  Downloading decorator-5.3.1-py3-none-any.whl.metadata (3.9 kB)
Collecting build>=1.0.0 (from pip-tools==7.5.3->-r dev-requirements.txt (line 15))
  Downloading build-1.5.0-py3-none-any.whl.metadata (5.7 kB)
Requirement already satisfied: pip>=22.2 in /usr/local/lib/python3.10/site-packages (from pip-tools==7.5.3->-r dev-requirements.txt (line 15)) (26.1.2)
Collecting pyproject_hooks (from pip-tools==7.5.3->-r dev-requirements.txt (line 15))
  Downloading pyproject_hooks-1.2.0-py3-none-any.whl.metadata (1.3 kB)
Requirement already satisfied: setuptools in /usr/local/lib/python3.10/site-packages (from pip-tools==7.5.3->-r dev-requirements.txt (line 15)) (82.0.1)
Requirement already satisfied: wheel in /usr/local/lib/python3.10/site-packages (from pip-tools==7.5.3->-r dev-requirements.txt (line 15)) (0.45.1)
Requirement already satisfied: pluggy>=1.2 in /usr/local/lib/python3.10/site-packages (from pytest-cov==7.1.0->-r dev-requirements.txt (line 16)) (1.6.0)
Collecting inflection (from pytest-factoryboy==2.8.1->-r dev-requirements.txt (line 17))
  Downloading inflection-0.5.1-py2.py3-none-any.whl.metadata (1.7 kB)
Requirement already satisfied: packaging in /usr/local/lib/python3.10/site-packages (from pytest-factoryboy==2.8.1->-r dev-requirements.txt (line 17)) (26.1)
Collecting exceptiongroup>=1 (from pytest==9.0.3->-r dev-requirements.txt (line 20))
  Downloading exceptiongroup-1.3.1-py3-none-any.whl.metadata (6.7 kB)
Collecting iniconfig>=1.0.1 (from pytest==9.0.3->-r dev-requirements.txt (line 20))
  Downloading iniconfig-2.3.0-py3-none-any.whl.metadata (2.5 kB)
Collecting pygments>=2.7.2 (from pytest==9.0.3->-r dev-requirements.txt (line 20))
  Downloading pygments-2.20.0-py3-none-any.whl.metadata (2.5 kB)
Requirement already satisfied: urllib3<3.0,>=1.25.10 in /usr/local/lib/python3.10/site-packages (from responses==0.26.0->-r dev-requirements.txt (line 21)) (2.6.3)
Collecting docutils<0.23,>0.18 (from sphinx-rtd-theme==3.1.0->-r dev-requirements.txt (line 22))
  Downloading docutils-0.22.4-py3-none-any.whl.metadata (15 kB)
Collecting sphinxcontrib-jquery<5,>=4 (from sphinx-rtd-theme==3.1.0->-r dev-requirements.txt (line 22))
  Downloading sphinxcontrib_jquery-4.1-py2.py3-none-any.whl.metadata (2.6 kB)
Collecting sphinxcontrib-applehelp>=1.0.7 (from sphinx==8.1.3->-r dev-requirements.txt (line 23))
  Downloading sphinxcontrib_applehelp-2.0.0-py3-none-any.whl.metadata (2.3 kB)
Collecting sphinxcontrib-devhelp>=1.0.6 (from sphinx==8.1.3->-r dev-requirements.txt (line 23))
  Downloading sphinxcontrib_devhelp-2.0.0-py3-none-any.whl.metadata (2.3 kB)
Collecting sphinxcontrib-htmlhelp>=2.0.6 (from sphinx==8.1.3->-r dev-requirements.txt (line 23))
  Downloading sphinxcontrib_htmlhelp-2.1.0-py3-none-any.whl.metadata (2.3 kB)
Collecting sphinxcontrib-jsmath>=1.0.1 (from sphinx==8.1.3->-r dev-requirements.txt (line 23))
  Downloading sphinxcontrib_jsmath-1.0.1-py2.py3-none-any.whl.metadata (1.4 kB)
Collecting sphinxcontrib-qthelp>=1.0.6 (from sphinx==8.1.3->-r dev-requirements.txt (line 23))
  Downloading sphinxcontrib_qthelp-2.0.0-py3-none-any.whl.metadata (2.3 kB)
Collecting sphinxcontrib-serializinghtml>=1.1.9 (from sphinx==8.1.3->-r dev-requirements.txt (line 23))
  Downloading sphinxcontrib_serializinghtml-2.0.0-py3-none-any.whl.metadata (2.4 kB)
Collecting docutils<0.23,>0.18 (from sphinx-rtd-theme==3.1.0->-r dev-requirements.txt (line 22))
  Downloading docutils-0.21.2-py3-none-any.whl.metadata (2.8 kB)
Collecting snowballstemmer>=2.2 (from sphinx==8.1.3->-r dev-requirements.txt (line 23))
  Downloading snowballstemmer-3.1.1-py3-none-any.whl.metadata (7.9 kB)
Requirement already satisfied: babel>=2.13 in /usr/local/lib/python3.10/site-packages (from sphinx==8.1.3->-r dev-requirements.txt (line 23)) (2.18.0)
Collecting alabaster>=0.7.14 (from sphinx==8.1.3->-r dev-requirements.txt (line 23))
  Downloading alabaster-1.0.0-py3-none-any.whl.metadata (2.8 kB)
Collecting imagesize>=1.3 (from sphinx==8.1.3->-r dev-requirements.txt (line 23))
  Downloading imagesize-2.0.0-py2.py3-none-any.whl.metadata (1.5 kB)
Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/site-packages (from Jinja2<4.0.0,>=2.7->cookiecutter==2.7.1->-r dev-requirements.txt (line 5)) (3.0.3)
Requirement already satisfied: charset_normalizer<4,>=2 in /usr/local/lib/python3.10/site-packages (from requests>=2.23.0->cookiecutter==2.7.1->-r dev-requirements.txt (line 5)) (3.4.7)
Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/site-packages (from requests>=2.23.0->cookiecutter==2.7.1->-r dev-requirements.txt (line 5)) (3.11)
Requirement already satisfied: certifi>=2023.5.7 in /usr/local/lib/python3.10/site-packages (from requests>=2.23.0->cookiecutter==2.7.1->-r dev-requirements.txt (line 5)) (2026.2.25)
Requirement already satisfied: blinker>=1.9.0 in /usr/local/lib/python3.10/site-packages (from flask>=2.3.0->flask-debugtoolbar==0.16.0->-r dev-requirements.txt (line 9)) (1.9.0)
Requirement already satisfied: itsdangerous>=2.2.0 in /usr/local/lib/python3.10/site-packages (from flask>=2.3.0->flask-debugtoolbar==0.16.0->-r dev-requirements.txt (line 9)) (2.2.0)
Requirement already satisfied: werkzeug>=3.1.0 in /usr/local/lib/python3.10/site-packages (from flask>=2.3.0->flask-debugtoolbar==0.16.0->-r dev-requirements.txt (line 9)) (3.1.8)
Collecting jedi>=0.16 (from ipython>=7.31.1->ipdb==0.13.13->-r dev-requirements.txt (line 11))
  Downloading jedi-0.20.0-py2.py3-none-any.whl.metadata (23 kB)
Collecting matplotlib-inline (from ipython>=7.31.1->ipdb==0.13.13->-r dev-requirements.txt (line 11))
  Downloading matplotlib_inline-0.2.2-py3-none-any.whl.metadata (2.4 kB)
Collecting pexpect>4.3 (from ipython>=7.31.1->ipdb==0.13.13->-r dev-requirements.txt (line 11))
  Downloading pexpect-4.9.0-py2.py3-none-any.whl.metadata (2.5 kB)
Collecting prompt_toolkit<3.1.0,>=3.0.41 (from ipython>=7.31.1->ipdb==0.13.13->-r dev-requirements.txt (line 11))
  Downloading prompt_toolkit-3.0.52-py3-none-any.whl.metadata (6.4 kB)
Collecting stack_data (from ipython>=7.31.1->ipdb==0.13.13->-r dev-requirements.txt (line 11))
  Downloading stack_data-0.6.3-py3-none-any.whl.metadata (18 kB)
Collecting traitlets>=5.13.0 (from ipython>=7.31.1->ipdb==0.13.13->-r dev-requirements.txt (line 11))
  Downloading traitlets-5.15.1-py3-none-any.whl.metadata (10 kB)
Collecting wcwidth (from prompt_toolkit<3.1.0,>=3.0.41->ipython>=7.31.1->ipdb==0.13.13->-r dev-requirements.txt (line 11))
  Downloading wcwidth-0.8.1-py3-none-any.whl.metadata (43 kB)
Collecting parso<0.9.0,>=0.8.6 (from jedi>=0.16->ipython>=7.31.1->ipdb==0.13.13->-r dev-requirements.txt (line 11))
  Downloading parso-0.8.7-py2.py3-none-any.whl.metadata (8.2 kB)
Collecting ptyprocess>=0.5 (from pexpect>4.3->ipython>=7.31.1->ipdb==0.13.13->-r dev-requirements.txt (line 11))
  Downloading ptyprocess-0.7.0-py2.py3-none-any.whl.metadata (1.3 kB)
Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/site-packages (from python-dateutil>=2.7->freezegun==1.5.5->-r dev-requirements.txt (line 10)) (1.17.0)
Collecting text-unidecode>=1.3 (from python-slugify>=4.0.0->cookiecutter==2.7.1->-r dev-requirements.txt (line 5))
  Downloading text_unidecode-1.3-py2.py3-none-any.whl.metadata (2.4 kB)
Collecting tzdata (from arrow->cookiecutter==2.7.1->-r dev-requirements.txt (line 5))
  Downloading tzdata-2026.2-py2.py3-none-any.whl.metadata (1.4 kB)
Collecting markdown-it-py>=2.2.0 (from rich->cookiecutter==2.7.1->-r dev-requirements.txt (line 5))
  Downloading markdown_it_py-4.2.0-py3-none-any.whl.metadata (7.4 kB)
Collecting mdurl~=0.1 (from markdown-it-py>=2.2.0->rich->cookiecutter==2.7.1->-r dev-requirements.txt (line 5))
  Downloading mdurl-0.1.2-py3-none-any.whl.metadata (1.6 kB)
Collecting executing>=1.2.0 (from stack_data->ipython>=7.31.1->ipdb==0.13.13->-r dev-requirements.txt (line 11))
  Downloading executing-2.2.1-py2.py3-none-any.whl.metadata (8.9 kB)
Collecting asttokens>=2.1.0 (from stack_data->ipython>=7.31.1->ipdb==0.13.13->-r dev-requirements.txt (line 11))
  Downloading asttokens-3.0.1-py3-none-any.whl.metadata (4.9 kB)
Collecting pure-eval (from stack_data->ipython>=7.31.1->ipdb==0.13.13->-r dev-requirements.txt (line 11))
  Downloading pure_eval-0.2.3-py3-none-any.whl.metadata (6.3 kB)
Downloading beautifulsoup4-4.14.3-py3-none-any.whl (107 kB)
Downloading cookiecutter-2.7.1-py3-none-any.whl (41 kB)
Downloading coverage-7.13.5-cp310-cp310-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (248 kB)
Downloading factory_boy-3.3.3-py2.py3-none-any.whl (37 kB)
Downloading faker-40.15.0-py3-none-any.whl (2.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.0/2.0 MB 405.7 MB/s  0:00:00
Downloading flask_debugtoolbar-0.16.0-py3-none-any.whl (413 kB)
Downloading freezegun-1.5.5-py3-none-any.whl (19 kB)
Downloading ipdb-0.13.13-py3-none-any.whl (12 kB)
Downloading junit2html-31.0.5-py3-none-any.whl (21 kB)
Downloading junitparser-5.0.0-py3-none-any.whl (14 kB)
Downloading pillow-12.2.0-cp310-cp310-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (7.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.1/7.1 MB 294.0 MB/s  0:00:00
Downloading pip_tools-7.5.3-py3-none-any.whl (71 kB)
Downloading pytest_cov-7.1.0-py3-none-any.whl (22 kB)
Downloading pytest_factoryboy-2.8.1-py3-none-any.whl (16 kB)
Downloading pytest_freezegun-0.4.2-py2.py3-none-any.whl (4.6 kB)
Downloading pytest_split-0.11.0-py3-none-any.whl (11 kB)
Downloading pytest-9.0.3-py3-none-any.whl (375 kB)
Downloading responses-0.26.0-py3-none-any.whl (35 kB)
Downloading sphinx_rtd_theme-3.1.0-py2.py3-none-any.whl (7.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.7/7.7 MB 318.0 MB/s  0:00:00
Downloading sphinx-8.1.3-py3-none-any.whl (3.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.5/3.5 MB 395.0 MB/s  0:00:00
Downloading toml-0.10.2-py2.py3-none-any.whl (16 kB)
Downloading towncrier-25.8.0-py3-none-any.whl (65 kB)
Downloading docutils-0.21.2-py3-none-any.whl (587 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 587.4/587.4 kB 473.5 MB/s  0:00:00
Downloading sphinxcontrib_jquery-4.1-py2.py3-none-any.whl (121 kB)
Downloading alabaster-1.0.0-py3-none-any.whl (13 kB)
Downloading binaryornot-0.6.0-py3-none-any.whl (14 kB)
Downloading build-1.5.0-py3-none-any.whl (26 kB)
Downloading exceptiongroup-1.3.1-py3-none-any.whl (16 kB)
Downloading imagesize-2.0.0-py2.py3-none-any.whl (9.4 kB)
Downloading iniconfig-2.3.0-py3-none-any.whl (7.5 kB)
Downloading ipython-8.39.0-py3-none-any.whl (831 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 831.8/831.8 kB 595.0 MB/s  0:00:00
Downloading prompt_toolkit-3.0.52-py3-none-any.whl (391 kB)
Downloading jedi-0.20.0-py2.py3-none-any.whl (4.9 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.9/4.9 MB 204.9 MB/s  0:00:00
Downloading parso-0.8.7-py2.py3-none-any.whl (107 kB)
Downloading pexpect-4.9.0-py2.py3-none-any.whl (63 kB)
Downloading ptyprocess-0.7.0-py2.py3-none-any.whl (13 kB)
Downloading pygments-2.20.0-py3-none-any.whl (1.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 397.7 MB/s  0:00:00
Downloading python_slugify-8.0.4-py2.py3-none-any.whl (10 kB)
Downloading snowballstemmer-3.1.1-py3-none-any.whl (104 kB)
Downloading soupsieve-2.8.4-py3-none-any.whl (37 kB)
Downloading sphinxcontrib_applehelp-2.0.0-py3-none-any.whl (119 kB)
Downloading sphinxcontrib_devhelp-2.0.0-py3-none-any.whl (82 kB)
Downloading sphinxcontrib_htmlhelp-2.1.0-py3-none-any.whl (98 kB)
Downloading sphinxcontrib_jsmath-1.0.1-py2.py3-none-any.whl (5.1 kB)
Downloading sphinxcontrib_qthelp-2.0.0-py3-none-any.whl (88 kB)
Downloading sphinxcontrib_serializinghtml-2.0.0-py3-none-any.whl (92 kB)
Downloading text_unidecode-1.3-py2.py3-none-any.whl (78 kB)
Downloading traitlets-5.15.1-py3-none-any.whl (85 kB)
Downloading arrow-1.4.0-py3-none-any.whl (68 kB)
Downloading decorator-5.3.1-py3-none-any.whl (10 kB)
Downloading inflection-0.5.1-py2.py3-none-any.whl (9.5 kB)
Downloading matplotlib_inline-0.2.2-py3-none-any.whl (9.5 kB)
Downloading pyproject_hooks-1.2.0-py3-none-any.whl (10 kB)
Downloading rich-15.0.0-py3-none-any.whl (310 kB)
Downloading markdown_it_py-4.2.0-py3-none-any.whl (91 kB)
Downloading mdurl-0.1.2-py3-none-any.whl (10.0 kB)
Downloading stack_data-0.6.3-py3-none-any.whl (24 kB)
Downloading asttokens-3.0.1-py3-none-any.whl (27 kB)
Downloading executing-2.2.1-py2.py3-none-any.whl (28 kB)
Downloading pure_eval-0.2.3-py3-none-any.whl (11 kB)
Downloading tzdata-2026.2-py2.py3-none-any.whl (349 kB)
Downloading wcwidth-0.8.1-py3-none-any.whl (323 kB)
Installing collected packages: text-unidecode, pure-eval, ptyprocess, wcwidth, tzdata, traitlets, toml, sphinxcontrib-serializinghtml, sphinxcontrib-qthelp, sphinxcontrib-jsmath, sphinxcontrib-htmlhelp, sphinxcontrib-devhelp, sphinxcontrib-applehelp, soupsieve, snowballstemmer, python-slugify, pyproject_hooks, pygments, Pillow, pexpect, parso, mdurl, junitparser, iniconfig, inflection, imagesize, Faker, executing, exceptiongroup, docutils, decorator, coverage, binaryornot, asttokens, alabaster, towncrier, stack_data, sphinx, responses, pytest, prompt_toolkit, matplotlib-inline, markdown-it-py, junit2html, jedi, freezegun, factory-boy, build, beautifulsoup4, arrow, sphinxcontrib-jquery, rich, pytest-split, pytest-freezegun, pytest-factoryboy, pytest-cov, pip-tools, ipython, flask-debugtoolbar, sphinx-rtd-theme, ipdb, cookiecutter
Successfully installed Faker-40.15.0 Pillow-12.2.0 alabaster-1.0.0 arrow-1.4.0 asttokens-3.0.1 beautifulsoup4-4.14.3 binaryornot-0.6.0 build-1.5.0 cookiecutter-2.7.1 coverage-7.13.5 decorator-5.3.1 docutils-0.21.2 exceptiongroup-1.3.1 executing-2.2.1 factory-boy-3.3.3 flask-debugtoolbar-0.16.0 freezegun-1.5.5 imagesize-2.0.0 inflection-0.5.1 iniconfig-2.3.0 ipdb-0.13.13 ipython-8.39.0 jedi-0.20.0 junit2html-31.0.5 junitparser-5.0.0 markdown-it-py-4.2.0 matplotlib-inline-0.2.2 mdurl-0.1.2 parso-0.8.7 pexpect-4.9.0 pip-tools-7.5.3 prompt_toolkit-3.0.52 ptyprocess-0.7.0 pure-eval-0.2.3 pygments-2.20.0 pyproject_hooks-1.2.0 pytest-9.0.3 pytest-cov-7.1.0 pytest-factoryboy-2.8.1 pytest-freezegun-0.4.2 pytest-split-0.11.0 python-slugify-8.0.4 responses-0.26.0 rich-15.0.0 snowballstemmer-3.1.1 soupsieve-2.8.4 sphinx-8.1.3 sphinx-rtd-theme-3.1.0 sphinxcontrib-applehelp-2.0.0 sphinxcontrib-devhelp-2.0.0 sphinxcontrib-htmlhelp-2.1.0 sphinxcontrib-jquery-4.1 sphinxcontrib-jsmath-1.0.1 sphinxcontrib-qthelp-2.0.0 sphinxcontrib-serializinghtml-2.0.0 stack_data-0.6.3 text-unidecode-1.3 toml-0.10.2 towncrier-25.8.0 traitlets-5.15.1 tzdata-2026.2 wcwidth-0.8.1
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager, possibly rendering your system unusable. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv. Use the --root-user-action option if you know what you are doing and want to suppress this warning.
WARNING: The directory '/usr/src/.cache/pip' or its parent directory is not owned or is not writable by the current user. The cache has been disabled. Check the permissions and owner of that directory. If executing pip with sudo, you should use sudo's -H flag.
Obtaining file:///usr/src
  Installing build dependencies ... done
  Checking if build backend supports build_editable ... done
  Getting requirements to build editable ... done
  Preparing editable metadata (pyproject.toml) ... done
Requirement already satisfied: setuptools>=44.1.0 in /usr/local/lib/python3.10/site-packages (from ckan==2.13.0a0) (82.0.1)
Building wheels for collected packages: ckan
  Building editable for ckan (pyproject.toml) ... done
  Created wheel for ckan: filename=ckan-2.13.0a0-0.editable-py3-none-any.whl size=9231 sha256=cd2d3ab1322d4191fde63cf4761d8115599ba6f5a1a44805117324b832e51eec
  Stored in directory: /tmp/pip-ephem-wheel-cache-en1lbdj5/wheels/d0/9b/0f/3cbd797712c91ea97357c1fd4e5a74023608fa9532aa4203e8
Successfully built ckan
Installing collected packages: ckan
Successfully installed ckan-2.13.0a0
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager, possibly rendering your system unusable. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv. Use the --root-user-action option if you know what you are doing and want to suppress this warning.
WARNING: The directory '/usr/src/.cache/pip' or its parent directory is not owned or is not writable by the current user. The cache has been disabled. Check the permissions and owner of that directory. If executing pip with sudo, you should use sudo's -H flag.
No broken requirements found.
ERROR:  role "ckan_default" already exists
createdb: error: database creation failed: ERROR:  database "ckan_test" already exists
ERROR:  role "datastore_read" already exists
ERROR:  role "datastore_write" already exists
createdb: error: database creation failed: ERROR:  database "datastore_test" already exists
You are now connected to database "datastore_test" as user "ckan".
REVOKE
REVOKE
GRANT
GRANT
GRANT
GRANT
REVOKE
GRANT
GRANT
GRANT
ALTER DEFAULT PRIVILEGES
CREATE VIEW
ALTER VIEW
GRANT
CREATE FUNCTION
ALTER FUNCTION
DO
NOTICE:  relation "_table_stats" already exists, skipping
CREATE TABLE
ALTER TABLE
CREATE FUNCTION
ALTER FUNCTION
CREATE FUNCTION
ALTER FUNCTION
CREATE FUNCTION
ALTER FUNCTION
ERROR:  extension "tablefunc" already exists
Upgrading DB: SUCCESS
gzip: .test_durations.gz: No such file or directory
ubuntu@ip-172-31-2-102:~/CKAN-custom/test-infrastructure$ docker compose exec ckan bash -lc 'cd /usr/src && pip install -e .'
WARNING: The directory '/usr/src/.cache/pip' or its parent directory is not owned or is not writable by the current user. The cache has been disabled. Check the permissions and owner of that directory. If executing pip with sudo, you should use sudo's -H flag.
Obtaining file:///usr/src
  Installing build dependencies ... done
  Checking if build backend supports build_editable ... done
  Getting requirements to build editable ... done
  Preparing editable metadata (pyproject.toml) ... done
Requirement already satisfied: setuptools>=44.1.0 in /usr/local/lib/python3.10/site-packages (from ckan==2.13.0a0) (82.0.1)
Building wheels for collected packages: ckan
  Building editable for ckan (pyproject.toml) ... done
  Created wheel for ckan: filename=ckan-2.13.0a0-0.editable-py3-none-any.whl size=9231 sha256=385b1999e8a96d46cad664fa210b25d8a04b68274e8baef81606f9e59981256d
  Stored in directory: /tmp/pip-ephem-wheel-cache-q6hg1ii2/wheels/d0/9b/0f/3cbd797712c91ea97357c1fd4e5a74023608fa9532aa4203e8
Successfully built ckan
Installing collected packages: ckan
  Attempting uninstall: ckan
    Found existing installation: ckan 2.13.0a0
    Uninstalling ckan-2.13.0a0:
      Successfully uninstalled ckan-2.13.0a0
Successfully installed ckan-2.13.0a0
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager, possibly rendering your system unusable. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv. Use the --root-user-action option if you know what you are doing and want to suppress this warning.
ubuntu@ip-172-31-2-102:~/CKAN-custom/test-infrastructure$ docker compose exec ckan bash -lc 'cd /usr/src && ckan -c test-core-ci.ini db init'
Upgrading DB: SUCCESS
ubuntu@ip-172-31-2-102:~/CKAN-custom/test-infrastructure$ docker compose exec ckan bash -lc 'cd /usr/src && ckan -c test-core-ci.ini run -H 0.0.0.0 -p 5000'
2026-06-26 11:23:09,034 INFO  [werkzeug] WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.18.0.4:5000
2026-06-26 11:23:09,034 INFO  [werkzeug] Press CTRL+C to quit
2026-06-26 11:23:09,050 INFO  [werkzeug]  * Restarting with watchdog (inotify)
2026-06-26 11:23:11,265 WARNI [werkzeug]  * Debugger is active!
2026-06-26 11:23:11,265 INFO  [werkzeug]  * Debugger PIN: 986-496-182
