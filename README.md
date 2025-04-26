# AutArch README

## Summary

AutArch is an AI-assisted workflow capable of creating uniform archaeological datasets from heterogeneous published resources. The implementation provided here takes large and unsorted PDF files as input, and uses neural networks to conduct image processing, object detection, and classification.


## Recommended Hardware

We support Intel CPUs; we do not officially support ARM64 CPUs. This version/guide only uses a CPU for the ML models for easier compatibility. We strongly recommend at least 60 GB of free HDD space (40 GB for AutArch + 20 GB for figures). To reproduce all results we strongly recommend at least 16 GB of RAM.


## Recommended Operating Systems

This version/guide only covers the use of Windows or Linux while using WSL2. Other operating systems (e.g., Mac OS X) are not covered here (successful tests on Mac OS X have been carried out, though). Without loss of generality, the starting guide below is mostly written from the perspective of Windows (with WSL2).


## Starting Guide (Linux)

AutArch and the reproduction of the figures have been successfully tested on Linux systems running Ubuntu 24.04 and 24.10 – other Linux versions should work as well. Please refer to the official docker website for general installation information:

<https://docs.docker.com/engine/install/>


## Starting Guide (AutArch for Windows using WSL2)

This section is a prerequisite to the next section on reproducing the underlying paper’s figures and tables. The section is written at times from the perspective of Windows (with WSL2), but the instructions similarly apply to other operating systems.


### 1. Installing Docker Desktop

Download WSL2 Docker Desktop: https://docs.docker.com/desktop/features/wsl/ . Install WSL2 Docker Desktop on your computer and restart it. Open the Docker Desktop app and agree to the terms of service.

If Docker Desktop does not start, press CTRL + ALT + DELETE and end any instance of Docker running in the background. If you have not downloaded WSL before, you will get an error message saying that you need to update WSL. Go into the PowerShell in Windows and download/update WSL by entering the following command:

`wsl --update`

Reopen Docker Desktop and press finish. You should see the start page with the container.

For what follows, make sure that Docker Desktop is running in the background.


### 2. Locating the AutArch Docker folder

Go into the Windows PowerShell, change the directory to the unpacked folder you created when downloading and unzipping AutArch. Unpacking may have created an autarch_prebuilt folder within an autarch_prebuilt folder. 

Check that you are in the right directory – there should be files like these ones:

- The readme.

- The main Docker file autarch_prebuilt/compose.yml.

- …

This folder uses public prebuilt images that are pulled from the docker registry.


### 3. Running AutArch

Make sure that Docker Desktop is running in the background (see above).

Make sure that you are in the autarch_prebuilt folder in the shell (see above).

In the PowerShell, type the following command:

`$ docker compose up`

When you do this for the first time, this step may take quite a while because public prebuilt images are pulled from the docker registry.

Make sure to leave the terminal opened in the background. 

It may take a few minutes for the Docker containers to start up.

Watch out for output lines like the following to appear:

web-1      | * Listening on http://0.0.0.0:3000

db-1       | 2025-04-13 13:26:58.776 UTC [1] LOG:  database system is ready to accept connections

(These lines may not appear next to each other.)

Once these lines have appeared, AutArch should have finished booting.

Go to your internet browser (Chrome, Edge etc.) and enter the following address:

[http://localhost:3000] or [http://127.0.0.1:3000]

You should be at the homepage of the AutArch software.


### 4. Using AutArch

Make sure AutArch is up and running (see above).

Only some basic usage of AutArch is discussed here. See the Workflow section below for more information.

A basic function of AutArch is the ability to upload and analyse a publication that contains grave drawings. Click 'Upload Publication', choose a PDF file to upload, enter article information, then press 'create publication'. All PDFs used in the database can be found in the PDFs folder. We consider them a good starting point.

Analysing the PDF may take a while, depending on the nature of the document. Note: The Docker environment supplied will only rely on the CPU. Certain aspects of the processing of PDFs will be slower than if the environment had a compatible GPU available.

Once the analysis of the publication is done, proceed to 'Graves' and filter by the publication you just uploaded. The uploaded publication should be available in the list, which is ordered alphabetically. Select it and click 'filter'.

If graves have been successfully detected, these will show in the list below. You can make edits by clicking the 'edit' button. Follow the steps one by one until all graves have been processed or click 'Graves' to return to the list.

Click 'Publications', select any publication from the list and click 'Stats' for a graphical overview of some of the results (e.g. orientation of the graves, whole-outline analysis).

AutArch allows many other functionalities, such as comparing publications, mapping results etc. See Workflow below for more information.


### 5. Closing AutArch

Close the AutArch tab in your internet browser. 

In the PowerShell, press Ctrl + C to stop the process.

You can also stop the Docker container(s) autarch_prebuilt in Docker Desktop instead.


### 6. Reopening AutArch

Make sure Docker Desktop is running (see above).

Make sure the Docker container(s) autarch_prebuilt are running (see above).


## Reproducing figures and tables

Make sure Docker Desktop and AutArch are running (see above).

We recommend having one terminal window (such as Powershell) running AutArch while a second terminal window is used to reproduce the figures.

In the second terminal, go to the ‘repoduce_figures’ folder in the ‘autarch_prebuilt’ directory. (That is, keep the first terminal window open for running AutArch in Docker).

Most of the figures and tables can be reproduced automatically using docker-compose and prebuilt images. Figure 5 requires MATLAB and has to be run manually.

Table 2 and 3 require upload of supplied PDFs and manual review of the object detection results for 795 pages of PDF.

Instructions for Figure 1-7 and Table 1-3 are provided below.

Make sure you are in the  ‘repoduce_figures’ folder for what follows.


### Figure 1

This part does not require AutArch to be running. This is a self contained script which uses the model in reproduce_figures/figure_1/models/rcnn_dfg.model as the object detection model. Take a screenshot of page 13 of Dobeš & Limburský 2013 and save it as reproduce_figures/figure_1/scripts/dobes_2013_page_13.png.

Use Powershell or such to run this:

`$ cd figure_1`

`$ docker compose up`

The output will be found in the reproduce_figures/figure_1/output folder.

OPTIONAL:

In case you want to rebuild image:

`$ docker build . -t kevin1252/autarch-figure1`


### Figure 2

This part does not require AutArch to be running. This is a self contained script. All code is in reproduce_figures/figure_2/map.py.

Use Powershell or such to run this:

`$ cd figure_2`

`$ docker compose up`

The output will be found in the reproduce_figures/figure_2/output folder.

OPTIONAL:

In case you want to rebuild image:

`$ docker build . -t kevin1252/autarch-figure1`


### Figure 3

The reproduction of figure 3 requires AutArch to be running. 

Use Powershell or such to run this:

`$ cd figure_3`

`$ docker compose up`

The docker image will automatically take a screenshot of this page:

<http://localhost:3000/graves/4262/update_grave/resize_boxes?short=true>

The page that is used for the screenshot can be manually opened in the browser to validate its authenticity. It is the edit page of grave OBJ774 from Dobeš & Limburský 2013.

The resulting file can be found in the reproduce_figures/figure_3/output folder.

OPTIONAL:

In case you want to rebuild image:

`$ docker build . -t kevin1252/autarch-figure3`


### Figure 4

The reproduction of figure 4 requires AutArch to be running. 

Use Powershell or such to run this:

`$ cd figure_4`

`$ docker compose up`

The docker image will automatically take a screenshot of these pages:

<http://localhost:3000/maps?tag_id=3&commit=Search> 

<http://localhost:3000/publications/1/radar> 

<http://localhost:3000/publications/6/radar>

<http://localhost:3000/maps?tag_id=3&commit=Search>

This page contains the map filtered by the “Corded Ware” tag. It shows all skeletons that were shown inside burials that were assigned to the “Corded Ware” tag, have a location and that have a north arrow and a discernible orientation. By zooming in and clicking on a radar chart, all graves relevant to the  specific radar chart are shown.

<http://localhost:3000/publications/1/radar>

Under this URL a radar chart can be found that shows all orientations of skeletons inside burials with discernible orientation and of graves that have a north arrow from the publication Dobeš & Limburský 2013.

<http://localhost:3000/publications/6/radar>

This is the same type of chart as mentioned above but for the publication Limburský 2012.

The resulting files can be found in the reproduce_figures/figure_4/output folder(The figures in the paper were combined in Illustrator).


### Figure 5

The reproduction of figure 5 does not require AutArch to be running.

Use Powershell or such to run this:

`$ cd figure_5`

`$ docker compose up`

The output will appear in figure_5/output:

- Part a and c will be in figure_5/output/figure_5.pdf
- Part b will be created as follows:

In PAST:

- Open figure_5/output/past.csv in Past and select "Only data cells" under "Rows contain" and "Columns contain". Select "Comma" under "Separator".

- Select all data with ctr+a.

- Click Geometry > Outlines (2D) > Elliptic Fourier > EFA PCA.

- In the window that opens, 

- keep Modes set to 20, 

- tick 'invariant to rotation+start, and 

- click Compute

- In the Deformations tab, 

- Increase the score by 0.05 for PC1 and PC2 respectively.

### Figure 6

The reproduction of figure 6 requires AutArch to be running.

Use Powershell or such to run this:

`$ cd figure_6`

`$ docker compose up`

The docker image will automatically download the following urls as input:

<http://localhost:3000/graves/orientations.json?name=Corded%20Ware> 

<http://localhost:3000/graves/orientations.json?name=name=Bell%20Beaker> 

http://localhost:3000/graves/orientations.json?name=Corded%20Ware

This contains all data used for the map (see figure 4) accumulated for all sites where the graves were labeled as “Corded Ware” in the literature.

<http://localhost:3000/graves/orientations.json?name=Bell%20Beaker> 

This contains all data used for the map (see figure 4) accumulated for all sites where the graves were labeled as “Bell Beaker” in the literature.

The program “grave_orientation.py” contained in reproduce_figures/figure_6 is then used on the downloaded json files to perform the analysis as described in the publication.

The resulting files can be found in the reproduce_figures/figure_6/output folder. 

( Body figure drawings were added using Illustrator)


### Figure 7

The reproduction of figure 7 does not require AutArch to be running.

Use Powershell or such to run this:

`$ cd figure_7`

`$ docker compose up`

The results of the user study are supplied in reproduce_figures/figure_7/experiment. Inside this folder, the “comove” folder contains the data created by the users for the AutArch study while the “inkscape” folder contains the data created by the users using the Inkscape software. 

The AutArch data was exported to a csv file from the database at the end of the experiment. The users are internally identified with two numbers separated by an underscore. In the file reproduce_figures/figure_7/user_map.json every user is assigned a fixed number.

The original excel spreadsheet supplied to the users using Inkscape can be found under reproduce_figures/figure_7/co move collection spreadsheet.xlsx.

The following files are created in the reproduce_figures/figure_7/output folder:

inkscape_count.csv: the number of processed graves per user in Inkscape

comove_count.csv: the number of processed graves per user in AutArch

errors_comove.json: The errors per grave for all users, every list entry per user corresponds to one grave in AutArch

errors_inkscape.json: The errors per grave for all users, every list entry per user corresponds to one grave in Inkscape

box_errors.png: Figure 7 as used in the publication

OPTIONAL:

In case you want to rebuild image:

`$ docker build . -t kevin1252/autarch-figure7`


### Table 1

The reproduction of table 1 does not require AutArch to be running. 

Use Powershell or such to run this:

`$ cd table_1`

`$ docker compose up`

The output lists all the information to create Table 1.

OPTIONAL:

In case you want to rebuild image:

`$ docker build . -t kevin1252/autarch-table1`


### Table 2

Autarch needs to be running to reproduce table 2.

This figure requires the following publications as pdf:

Baron et al 2019

Sachsse 2015

Neugebauer-Maresch and Lenneis 2015

Wlodarczak 2018

 

We provide a step by step guide as a sample for the publication “Baron et al 2019.pdf”. The file can be found in reproduce_figures/table_2/. Upload this file to AutArch here: <http://localhost:3000/publications/new>

Please provide a suitable name, year and author in the form. After the upload has completed the publication can be found at the bottom of the list of publications: <http://localhost:3000/publications>

On the right side of the page there is a link called “Pages” which leads to a screen showing each page of the publication. Clicking “Next” shows the next page. An excel template is provided under reproduce_figures/table_2/Autarch Validation - Empty.xlsx. Navigate through all the pages and write down the page number in the respective column and count the number of true positive, false positive or false negative graves detected you encounter in any of the pages.

The excel spreadsheet showing our results is located in reproduce_figures/table_2/Autarch Validation.xlsx. 

All other publications should be processed in the same fashion. Please note that “Sachsse 2015” has 332 pages and “Neugebauer-Maresch and Lenneis 2015” has 406 pages.


### Table 3

Autarch needs to be running to reproduce table 3. 

This figure requires the following publications as pdf:

Wlodarczak 2018

We provide a step by step guide for the first burial. First location the file “Wlodarczak 2018.pdf”. The file can be found in reproduce_figures/table_3/. Upload this file to AutArch here: <http://localhost:3000/publications/new> We strongly recommend you use the text for the author “Wlodarczak 2018 validation”. 

An empty spreadsheet is available under reproduce_figures/table_3/Autarch Validation Empty.xslx under the sheet “workflow Wlodarzack 2018”.

Go to graves in the navbar: <http://localhost:3000/graves>

Filter for the publication you just uploaded by selecting “Wlodarczak 2018 validation” from the dropdown at the top of the page. Click the “Filter” button.

Click on the “Edit” link for the first grave in the list. Enter the identifier of the grave. Here it is “III/3” as indicated in the description of the drawing. Click “Next”.

Entering a site is not necessary here. Click “Next”.

Entering a tag is not necessary here. Click “Next”.

Click on the scale on the right side of the page. Adjust the bounding box that is highlighted to enclose the scale of the arrow. Make an entry in the spreadsheet accordingly under “Adjusted Scale”.

Add a north arrow if none is showing up on the right side by clicking on “New Figure”. And selecting “North Arrow” from the dropdown. Click “Next”.

Make sure that all contours seem to match the actual objects. Click “Next”.

As the text of the scale has not been automatically detected. Add the text “100” in the textbox and click “Next”. Make an entry in the spreadsheet accordingly under “manually added text to scale”.

Proceed in a similar manner for the other pages of this burial. After clicking “Next” on the last page, it will take you to the next burial. 


## Workflow

Publications can be imported under Publications -> Import

After the import has completed, the publication is available under Publications. It is recommended to go to the annotation screen and add all false negative objects.

To review all the graves, go to the grave screen. Use the filter on the top to select the publications just uploaded. Then click the edit button of the first grave on the list.


### Grave Data

The ID assigned to the burial by the authors in the source publication is recorded. In case multiple images of the same grave are shown, the software will prevent duplicates in the results using this ID. In this step, the expert also has the option to discard drawings incorrectly classified as a grave.


### Site

Graves can be assigned to specific sites. Sites can be added here.


### Tags

Graves can be given arbitrary tags to discern them and allow for filtering in the overview map. Tags can be added here.


### Boxes

Correcting bounding boxes. The user can manually add, remove or change the bounding box assigned to a specific grave. Potential tasks include selecting a different scale on the page, resizing bounding boxes because they do not fully encapsulate an object or marking north arrows that were initially missed by object detection. During this step, a manual arrow has to be drawn for every skeleton following the spine and pointing towards the skull, which is necessary to determine the orientation of the skeleton in the grave. Several automated steps are then performed. The contours are calculated using the new bounding boxes and the resulting changes in measurements are saved. The orientation of the north arrow and the deposition type of the skeleton are updated using their respective neural network. The analysis of the scale is performed again.


### Contours

All detected outlines in relation to one particular grave are highlighted, allowing the user, if any issue arises, to return to the previous step and fit, for instance, a manual bounding box around the grave or cross-section to indicate the width, length or depth.


### Scale

The next step is to validate the scale by checking the text indicating the real-world length of the scale. Once this step is completed, all measurements are updated with the new scale information. In case no individual scale is provided and the publication uses a fixed scale, e.g. all drawings are 1:20, a different screen is shown. In this screen, the actual height of the page (in cm) has to be entered manually, together with the ratio of the drawing. This way, all measurements can be calculated in the absence of a scale and the results are fully compatible with scaled publications.


### North Arrow

The angle of the north arrow can be adjusted manually based on a preview. In case an arrow is missing in the drawing, this screen will be skipped and size measurements and contours will still be collected without the orientation.


### Skeleton Information

Finally, the pose of all skeletons has to be validated, which (for now) consists of “unknown”, “flexed on the side” or “supine”. As described above, a neural network will set the initial body position, but it can be adjusted manually. Further positions could easily be added in the future. “Unknown” is used in cases where skeletal remains are visible, but no position can be identified.
