#!/usr/bin/env python
from ipykernel.kernelapp import IPKernelApp
from .kernel import jansmongodbkernel
IPKernelApp.launch_instance(kernel_class=jansmongodbkernel)