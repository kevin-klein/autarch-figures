Running

$ docker build . -t autarch-figure-7
$ docker run --rm -it --mount src="$(pwd)/output",target="/output",type=bind autarch-figure-7

After the experiment, the databases were exported from all participants and the results can be found in experiment/comove. Every file corresponds to one participant.
The excel spreadsheets used in the experiment were exported as csv and can be found in experiment/inkscape. The original supplied to the participants can be found in the root folder "co move collection spreadsheet.xlsx".

The following files are created in the output folder:

inkscape_count.csv: the number of processed graves per user in Inkscape
comove_count.csv: the number of processed graves per user in AutArch

errors_comove.json: The errors per grave for all users, every list entry per user corresponds to one grave in AutArch
errors_inkscape.json: The errors per grave for all users, every list entry per user corresponds to one grave in Inkscape

box_errors.png: Figure 7 as used in the publication