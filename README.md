# jansmongodbkernel

![alt](jansmongodbkernel/logo-svg.svg)

A simple mongodb kernel for jupyter.
Created using IPython's kernel and pexpect's REPLWrapper subclasses.
This kernel still has some issues and therefore is a work in progress.
Somehow the REPLWrapper loses track of what to post back.
Also incomplete statements may hang the wrapper.

## Dev Installation

- install mongodb from your distro's package manager
- `pip install` jupyterlab and pexpect
- download/clone this project
- open shell in project folder
- `pip install -e ./`
- `jupyter kernelspec install --user jansmongodbkernel`

## Uninstall

- `jupyter kernelspec uninstall jansmongodbkernel`
- `pip uninstall jansmongodbkernel`
