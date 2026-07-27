# GoPro 360 mp4 video to frames

Converts GoPro mp4s with equirectangular projections into single frames with correct metadata.

## Explorer

If you don't / can't run this script locally, our cloud product, Explorer, provides almost all of this scripts functionality in a web app.

* [Explorer app](https://explorer.trekview.org/).
* [Explorer docs](https://guides.trekview.org/explorer/overview).

## Installation

You must have:

* ffmpeg
    * by default we bind to default path, so test by running `ffmpeg` in your cli
* exiftool
    * by default we bind to default path, so test by running `exiftool` in your cli
* imagemagick
	* by default we bind to default path, so test by running `convert` in your cli

Installed on you system.

You can then install the required Trek View components:

This repo:

```
pip install .
```

## Usage

```
gopro2frames [options] VIDEO_NAME.mp4
```

### Options

* `media_folder_full_path`: where to save the frames
	* default: `frames` (will create a folder called `frames` in the current directory)
	* options: any valid path
* `name`: sequence name
	* default: none (you must set a value for this)
	* options: `a-z`,`1-3`,`-`,`_` chars only
* `mode`: determines input type (and processing steps). Either `equirectangular` for 360 .mp4's, `hero` for normal mp4's, `dualfish` for two Fusion fisheye videos, `eac` for MAX .360 files
	* default: none (you must set a value for this)
	* options: `equirectangular`,`hero`,`eac`,`dualfish`
* `magick_path`: path to imagemagick
	* default (if left blank): assumes imagemagick is installed globally
* `ffmpeg_path` (if left blank): path to ffmpeg
	* default: assumes ffmpeg is installed globally
* `frame_rate`: sets the frame rate (frames per second) for extraction,
	* default: `0.5`
	* options: `0.5`,`1`,`2`,`5`,`10`,`25`,`29.97`,`30`
* `quality`: sets the extracted quality between 1-6. 1 being the highest quality (but slower processing). This is value used for ffmpeg `-q:v` flag.
	* default: `1`
	* options: `1`,`2`,`3`,`4`,`5`,`6`
* `time_warp`: You NEED to use this if video was shot in timewarp mode, else telemetry will be inaccurate. The script does not support timewarp mode set to Auto speed (because it's impossible to determine the capture rate). Set the timewarp speed used when shooting in this field
	* default: blank (not timewarp)
	* options: `2x`, `5x`, `10x`, `15x`, `30x`
* `debug`: enable debug mode.
	* Default: `FALSE`
	* options: `TRUE`,`FALSE`

## Test cases

Our suite of test cases can be downloaded here:

* [Valid video files](https://guides.trekview.org/explorer/developer-docs/sequences/upload/good-test-cases)

### Run Tests

All the tests resides in `tests` folder.

To run all the tests, run:

```
python -m unittest discover tests -p '*_tests.py'
```

### Camera support

This scripte only accepts videos:

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