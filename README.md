# GoPro 360 mp4 video to frames

Converts GoPro mp4s with equirectangular projections into single frames with correct metadata.


## Installation

You must have installed on you system:

* ffmpeg
    * by default we bind to default path, so test by running `ffmpeg` in your cli
	* if you need to install it : `sudo apt install ffmpeg`
* exiftool (:warning: release >= 13.56 if you use gopro2frames with a gopro max 2)
    * by default we bind to default path, so test by running `exiftool -ver` in your cli
	* if your release is too old:
	  * go to https://sourceforge.net/projects/exiftool/files/ and download the latest .tar.gz file.
	  * If your .tar.gz file is `Image-ExifTool-13.38.tar.gz` open your terminal and run these commands:
	    ```
		gzip -dc Image-ExifTool-13.59.tar.gz | tar -xf -
		cd Image-ExifTool-13.59
		perl Makefile.PL
		make test
		sudo make install
        ```
* imagemagick (optionnal)
	* by default we bind to default path, so test by running `convert` in your cli
*  make, to compile max2sphere
    * you can install it with `sudo apt install build-essential`


You can then install the required components:

Clone this repo:

```
git clone https://github.com/stefal/gopro2frames --recurse
```

Create a virtual environnment for gopro2frames and install it:

```
python3 -m venv venvgopro2frames
source venvgopro2frames/bin/activate
cd gopro2frames
pip install .
```

## Usage

```
gopro2frames [options] VIDEO_NAME.360
```

### Options

* `--media_folder_full_path`: where to save the frames
	* default: `frames` (will create a folder called `frames` in the current directory)
	* options: any valid path
* --`magick_path`: path to imagemagick
	* default (if left blank): assumes imagemagick is installed globally
* `--ffmpeg_path` (if left blank): path to ffmpeg
	* default: assumes ffmpeg is installed globally
* `--frame_rate`: sets the frame rate (frames per second) for extraction,
	* default: `auto`
	* options: `auto`, `0.5`,`1`,`2`,`5`,`10`,`25`,`29.97`,`30`
* `--time_warp`: The script does not support timewarp mode set to Auto speed (because it's impossible to determine the capture rate). Set the timewarp speed used when shooting in this field
	* default: `auto`
	* options: `auto`, `2x`, `5x`, `10x`, `15x`, `30x`
* `quality`: sets the extracted quality between 1-6. 1 being the highest quality (but slower processing). This is value used for ffmpeg `-q:v` flag.
	* default: `1`
	* options: `1`,`2`,`3`,`4`,`5`,`6`
* `debug`: enable debug mode.
	* Default: `FALSE`
	* options: `TRUE`,`FALSE`

### Run Tests

All the tests resides in `tests` folder.

To run all the tests, run:

```
python -m unittest discover tests -p '*_tests.py'
```

### Camera support

This script only accepts videos:

* Must be shot on GoPro camera
* Must have telemetry (GPS enabled when shooting)

It supports both 360 and non-360 videos. In the case of 360 videos, these must be processed by GoPro Software to final mp4 versions.

This script has currently been tested with the following GoPro cameras:

* GoPro HERO
	* HERO 8
	* HERO 9
	* HERO 10
* GoPro MAX
* GoPro MAX 2
* GoPro Fusion

It is very likely that older cameras are also supported, but we provide no support for these as they have not been tested.

### Logic

The general processing pipeline of gopro-frame-maker is as follows;

![](/docs/gopro-frame-maker-video-flow.jpg)

[Image source here](https://docs.google.com/drawings/d/1i6givGQnGsu7dW2fLt3qVSWaHDiP0TCciY_DtY5_mc4/edit)

[To read how this script works in detail, please read this post](/docs/LOGIC.md).

### Test cases

[A full library of sample files for each camera can be accessed here](https://guides.trekview.org/explorer/developer-docs/sequences/capture).

## License

[Apache 2.0](/LICENSE).