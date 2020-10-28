import sys
import subprocess
import toml
import glob

cwd = sys.argv[1]
config = toml.load(open(('/Users/mz-kimoto/.chpwd_cmd')))

for project in config['workdir']:
    dirpaths = glob.glob(config['workdir'][project]['dirpath'])
    if cwd in dirpaths:
        for cmd in config['workdir'][project]['cmd']:
            subprocess.run(cmd, cwd=cwd, shell=True)
