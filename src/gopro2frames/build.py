from pathlib import Path
import platform, shutil, subprocess
from setuptools.command.build_py import build_py as _build_py

class BuildCExecutables(_build_py):
    """Compile max2sphere & fusion2sphere via their original Makefiles and
    drop the binaries into gopro2frames/bin/ inside the build/lib tree."""
    def run(self):
        super().run()                                # 1) copy Python files
        pkg_root = Path(self.get_package_dir('gopro2frames'))
        out_dir  = Path(self.build_lib, 'gopro2frames', 'bin')
        out_dir.mkdir(parents=True, exist_ok=True)
        data_out = Path(self.build_lib, 'gopro2frames', 'data')
        data_out.mkdir(parents=True, exist_ok=True)

        for name in ('max2sphere', 'fusion2sphere'):
            c_dir = pkg_root / 'csrc' / name 
            print(f'building {name} in {c_dir}')
            import os
            print("real cwd =", os.path.abspath(c_dir))
            print((Path(c_dir) / "Makefile-Linux").exists())
            self.announce(f'building {name} in {c_dir}', level=3)

            # run `make -f Makefile` inside its own directory
            running_plateform = platform.system()
            if running_plateform == 'Linux':
                if name == 'max2sphere':
                    subprocess.check_call('make -f Makefile-Linux', cwd=c_dir, shell=True)
                if name == 'fusion2sphere':
                    subprocess.check_call('make -f Makefile', cwd=c_dir, shell=True)

            exe = c_dir / (name + ('.exe' if platform.system() == 'Windows' else ''))
            shutil.copy2(exe, out_dir / exe.name)
        
        src_param = (
            pkg_root
            / 'csrc'
            / 'fusion2sphere'
            / 'parameter-examples'
            / 'video-5_2k-mode.txt'
        )
        shutil.copy2(src_param, data_out / 'params.txt')
