Running

Install AutArch first using the provided README (https://doi.org/10.5281/zenodo.14999893).

Start docker desktop.

Use your favorite command line (e.g. Powershell) to run this:
$ cd [current folder, e.g table_1]
$ docker compose up

This prints all information to create Table 1.

OPTIONAL:
In case you decide to rebuild image:
$ docker build . -t kevin1252/autarch-table1
