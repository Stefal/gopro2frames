from importlib import resources
import logging
from pathlib import Path
import shutil
import sys
import argparse, time
from colorama import init, Fore, Style
from .helper import GoProFrameMakerHelper
from .core import GoProFrameMaker

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="gopro2frames",
                                description="Convert GoPro 360/Fusion videos to frames")
    parser.add_argument("input", nargs="+", help="Video files (.mp4 or .360)")
    parser.add_argument("--media_folder_full_path", type=str, help="Output directory for frames.", default="frames")
    #ffmpeg binary
    parser.add_argument("--ffmpeg-path", type=str, help="Set the path for ffmpeg.", default=shutil.which("ffmpeg"))
    #ffmpeg options
    parser.add_argument("-r", "--frame-rate", type=float, help="Sets the frame rate (frames per second) for extraction (available=[0.5, 1, 2, 5, 10, 25, 29.97, 30]), default: 0.5.", default=0.5)
    parser.add_argument("-t", "--time-warp", type=str, help="Set time warp mode for gopro. available values are 2x, 5x, 10x, 15x, 30x", default="")
    parser.add_argument("-q", "--quality", type=int, help="Sets the extracted quality between 2-6. 1 being the highest quality (but slower processing), default: 1. This is value used for ffmpeg -q:v flag. ", default=1)

    #max2spherebatch
    parser.add_argument("--max-sphere", type=str, help="Set the path for MAX2sphere binary.", default=Path(resources.files("gopro2frames")).joinpath("bin", "max2sphere"))

    #fusion2sphere
    parser.add_argument("--fusion-sphere", type=str, help="Set the path for fusion2sphere binary.", default=Path(resources.files("gopro2frames")).joinpath("bin", "fusion2sphere"))

    #fusion params
    parser.add_argument("--fusion_sphere_params", type=str, help="Set the path for fusion params.txt.", default=Path(resources.files("gopro2frames")).joinpath("data", "params.txt"))

    #image magick binary
    parser.add_argument("--image_magick_path", type=str, help="Set the path for image magick.", default=shutil.which("convert"))

    #exiftool binary
    parser.add_argument("--exiftool_path", type=str, help="Set the path for exiftool.", default=shutil.which("exiftool"))

    #debug option
    parser.add_argument("-d", "--debug", action='store_true', help="Enable debug mode, default: off.", default=False)
    return parser

def main(argv: list[str] | None = None) -> None:
    args = build_parser().parse_args(argv)
    logging.debug
    validated = GoProFrameMakerHelper.validateArgs(args)
    if not validated["status"]:
        for msg in validated["errors"]:
            logging.error(msg)
        sys.exit(1)

    GoProFrameMaker(validated["args"]).initiateProcessing()

if __name__ == '__main__':
    main()
    


    

