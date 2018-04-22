#!/usr/bin/env python3
import argparse
import subprocess
from pathlib import Path
import shutil

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Install django-base-project somewhere'
    )
    parser.add_argument('path')

    args = parser.parse_args()
    if args.path.split('/', 1)[1] == '':
        raise ValueError('Please provide a valid path')

    path = Path(args.path)
    if path.exists():
        raise ValueError('Path "{}" already exists!'.format(path))
    path = str(path)

    shutil.copytree('project_base', path)

    commands = [
        'cd {}'.format(path),
        'virtualenv -ppython3 .env',
        'source .env/bin/activate',
        'pip install --upgrade pip',
        'pip install pip-tools invoke',
        'echo "development" > environment',
        'inv pip',
        'inv migrate',
        'git init',
        'git add .',
        'git commit -m "Add auto generated base"'
    ]

    print('Files copied! Run the following command for lazy setup:')

    print(' && '.join(commands))
