# jansmongodbkernel

![alt](jansmongodbkernel/logo-svg.svg)

A simple mongodb kernel for jupyter.
Created using IPython's kernel and pexpect's REPLWrapper subclasses.

## Installation

- install mongodb from your distro's package manager
- `pip install` jupyterlab and pexpect
- download/clone this project
- open shell in project folder
- `pip install -e ./`
- `jupyter kernelspec install --user jansmongodbkernel`

## Uninstall

- `jupyter kernelspec uninstall jansmongodbkernel`
- `pip uninstall jansmongodbkernel`
