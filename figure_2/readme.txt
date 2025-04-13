Running

$ docker build . -t autarch-figure-2
$ docker run --rm -it --mount src="$(pwd)/output",target="/output",type=bind autarch-figure-2

The output will be found in the output folder. 