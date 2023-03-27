# jansmongodbkernel

![alt](jansmongodbkernel/logo-svg.svg)

A [mongodb](https://www.mongodb.com) kernel for jupyter.
Created using IPython's kernel and pexpect's REPLWrapper subclasses.
This relies on creating a custom prompt in mongosh like described [here](https://www.mongodb.com/docs/mongodb-shell/reference/customize-prompt/).

## Dev Installation

- install mongodb from your distro's package manager
- download/clone this project
- open shell in project folder
- `pip install -e ./`
- then install kernelspec (this will also add the custom prompt to your ~/.mongoshrc.js)
- `jansmongodbkernel`

## Uninstall

- `jupyter kernelspec uninstall jansmongodbkernel`
- `pip uninstall jansmongodbkernel`
- remove the line ```prompt = function() {return \`mongosh>>> \`;}``` from ~/.mongoshrc.js
