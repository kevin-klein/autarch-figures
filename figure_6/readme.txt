Running

Install AutArch first using the provided README (https://doi.org/10.5281/zenodo.14999893).

Start docker desktop.

Step 1 (optionally)
AutArch needs to be running first.

Export the orientations of burials:

$ docker exec -it autarch-web-1 bash

Exporting corded ware orientations:
$ bin/rails export:orientations 2

Exporting bell beaker orientations:
$ bin/rails export:orientations 3

The created files (orientations-Bell Beaker.json and orientations-Corded Ware.json) are already included in this folder.

Step 2

Use your favorite command line (e.g. Powershell) to run this:
$ cd [current folder, e.g figure_6]
$ docker compose up

Two will be created in the output folder (bb.pdf, cw.pdf). The body figures were manually added using Illustrator.

OPTIONAL (required if Step 1 is used):
In case you decide to rebuild image:
$ docker build . -t kevin1252/autarch-figure6
