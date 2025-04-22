#!/bin/sh
curl http://host.docker.internal:3000/graves/orientations.json?name=Corded%20Ware -o cw.json
curl http://host.docker.internal:3000/graves/orientations.json?name=Bell%20Beaker -o bb.json

python grave_orientation.py bb.json output/bb.pdf
python grave_orientation.py cw.json output/cw.pdf
