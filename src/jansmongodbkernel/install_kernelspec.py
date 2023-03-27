#!/usr/bin/env python
import os, shutil
from jupyter_client.kernelspec import KernelSpecManager
json ="""{"argv":["python","-m","jansmongodbkernel", "-f", "{connection_file}"],
 "display_name":"MongoDB"
}"""

svg = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
   id="Layer_1"
   data-name="Layer 1"
   viewBox="0 0 300 300"
   version="1.1"
   width="300"
   height="300"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:dc="http://purl.org/dc/elements/1.1/">
  <defs
     id="defs35">
    <style
       id="style33">.cls-1{fill:#10aa50;}.cls-2{fill:#b8c4c2;}.cls-3{fill:#12924f;}.cls-4{fill:#21313c;}</style>
  </defs>
  <title
     id="title37">MongoDB_Logo_FullColorBlack_RGB</title>
  <g
     id="g350"
     transform="translate(78.457928,0.005)">
    <path
       class="cls-1"
       d="M 134.44,120.34 C 119.13,52.8 87.22,34.82 79.08,22.11 A 144.57,144.57 0 0 1 70.18,4.69 c -0.43,6 -1.22,9.78 -6.32,14.33 -10.24,9.13 -53.73,44.57 -57.39,121.31 -3.41,71.55 52.6,115.67 60,120.23 5.69,2.8 12.62,0.06 16,-2.51 27,-18.53 63.89,-67.93 52,-137.71"
       id="path39" />
    <path
       class="cls-2"
       d="m 72.5,222.46 c -1.41,17.71 -2.42,28 -6,38.12 0,0 2.35,16.86 4,34.72 h 5.84 a 324.73,324.73 0 0 1 6.37,-37.39 C 75.15,254.19 72.79,238 72.5,222.46 Z"
       id="path41" />
    <path
       class="cls-3"
       d="m 82.7,257.92 v 0 c -7.64,-3.53 -9.85,-20.06 -10.19,-35.46 a 725.83,725.83 0 0 0 1.65,-76.35 C 73.76,132.75 74.35,22.37 70.87,6.21 a 134.29,134.29 0 0 0 8.21,15.89 c 8.14,12.72 40.06,30.7 55.36,98.24 C 146.36,190 109.67,239.27 82.7,257.92 Z"
       id="path43" />
  </g>
  <metadata
     id="metadata345">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:title>MongoDB_Logo_FullColorBlack_RGB</dc:title>
      </cc:Work>
    </rdf:RDF>
  </metadata>
</svg>
"""



def install_kernelspec():
    kerneldir = "/tmp/jansmongodbkernel/"
    print('Creating tmp files...', end="")
    os.mkdir(kerneldir)

    with open(kerneldir + "kernel.json", "w") as f:
        f.write(json)

    with open(kerneldir + "logo-svg.svg", "w") as f:
        f.write(svg)
        
    print(' Done!')
    print('Installing Jupyter kernel...', end="")
    
    ksm = KernelSpecManager()
    ksm.install_kernel_spec(kerneldir, 'jansmongodbkernel', user=os.getenv('USER'))
    
    print(' Done!')
    print('Cleaning up tmp files...', end="")
    
    shutil.rmtree(kerneldir)
    
    print(' Done!')
    print('For uninstall use: jupyter kernelspec uninstall jansmongodbkernel')
    
    print('Adding custom prompt to ~/.mongoshrc.js ...', end="")
    os.system('echo "prompt = function() {return \`mongosh>>> \`;}" >> ~/.mongoshrc.js')
    print(' Done!')