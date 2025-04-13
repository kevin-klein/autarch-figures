Running

AutArch needs to be running first.

Step 1 (optionally)
Export the orientations of burials:

$ docker exec -it autarch-web-1 bash

Exporting corded ware orientations:
$ bin/rails export:orientations 2

Exporting bell beaker orientations:
$ bin/rails export:orientations 3


The created files (orientations-Bell Beaker.json and orientations-Corded Ware.json) are already included in this folder.

Step 2

$ docker build . -t autarch-figure-6
$ docker run --rm -it --mount src="$(pwd)/output",target="/output",type=bind autarch-figure-6

Two will be created in the output folder (bb.pdf, cw.pdf). The body figures were manually added using Illustrator.