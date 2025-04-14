Running

Install AutArch first using the provided README (https://doi.org/10.5281/zenodo.14999893).

Start docker desktop.

Use your favorite command line (e.g. Powershell) to run this:
$ cd [current folder, e.g table_1]
$ docker compose up

This displays all information in the terminal to create Table 1. No file is created.

OPTIONAL:
In case you decide to rebuild image:
$ docker build . -t kevin1252/autarch-table1
