# Convert NMEA Files tp GPX

Python / Jupyter Lab project to convert NNMEA GPS files with .LOG extension to GPX format

I use the OM System OM Share app to GeoTag my photos. When the photos are geotagged using the app, on 
the camera SD card it creates some GPS log files under the GPSLOG folder. They have the file extension
"LOG". These LOG files can also be obtained from the OM System App by using the "share track log" function
in the case that you recorded a track but never geotagged any files on the camera.

I wanted to convert these files to GPX so I can upload them to a mapping site or utility and
see the route I walked taking photos. For some reason OM System create the file in NMEA data format, 
there is more information about this format here: 

https://www.gpsworld.com/what-exactly-is-gps-nmea-data/

## Script

There is a script for running in Jupyter Lab or Notebook:

[ConvertNMEAFiles.ipynb](ConvertNMEAFiles.ipynb) : Batch process a folder of LOG files and convert to GPX format

The script has instructions on usage when opened in Jupyter.

## Running Scripts

To run these you need:

- Python : https://www.python.org/
- Jupyter Lab or Jupyter Notebook: https://jupyter.org/

I use Jupyter Lab. Jupyter is an interactive development environment for code and data based on Python and needs to be run as a server locally (or perhaps remote via a LAN or the Internet although I have not tried that).

I found the best way to run this is using a platform called Anaconda, a data science platform supporting various languages including Python. Anaconda allows to set up an environment with Jupyter and all the required Python packages etc so that the main OS environment doesn't have to be polluted with all of this. I use this on MacOS.

## Setup

Setting up can be tricky depending on the OS so some perseverence may be necessary.

Here is the rough guide to my setup if taking my scripts to use yourself - YMMV:

- Clone this repo from Github to your local HDD
- Install Anaconda free version from here: https://www.anaconda.com/
- Run up the Anaconda Navigator App
- Anaconda supports mutliple environments for langauges / package installation
- You can use the default, but I created a new one "BatCave" from Environments Section > "Create" button
- If creating a new environment, choose Python and the default version
- In the Anaconda Environment, install Jupyter Lab (it may be installed by default)
- I use VSCode (Visual Studio Code - free from Microsoft) for editing, so install that too if wanted
- Then you need to install various Anaconda and Python packages - see below.
- To run a script, launch Jupyter Lab in Anaconda. It will fire up in the web browser
- In Jupyter, browse to one of the ".ipynb" scripts and run 
- If the scripts fail, it is probably due to missing Python packages - see below
- Scripts can also be run from VSCode. It will connect to the Jupyter/Anaconda server

## Python Packages

To install packages, I used Python "pip" from the Terminal / bash.

- In Anaconda go to Enironments, click on your environment then "Open Terminal"
- This fires up a Terminal then do "pip/conda install" as per the list below

Here are the Anaconda packahes I installed first (I think this is the only one needed):

```
conda install -c conda-forge ipyfilechooser
```

Here are the Python packages I installed using 'pip':

```
pip install os
pip install fnmatch
pip install ipywidgets
```
## Editing / Developing

I use Visual Studio Code ('VSCode') for editing and developing the scripts. It can open and run the Jupyter Notebook files ('.ipynb' extension) connecting to a local Jupyter server.

VSCode can be obtained from here for Mac, Windows or Linux platforms: https://code.visualstudio.com/

A version of VSCode is also included with the Anaconda install environment.

![Screenshot 2023-02-17 at 18 55 14](https://user-images.githubusercontent.com/916460/219761707-77a280bc-1488-478a-a3bd-16ea30a0f568.png)









