## Introduction
TRIP (Three-dimensional RNA Illustration Program) is a set of separate codes to model the 3D RNA folding shape based on polymer theory.
The set of codes is separated into seven different files, which categorized into four main parts: 
1. Simulation of RNA 
2. Simulation of RNA on a surface
3. Trajectory movie

The first two categories contains a code that outputs a distribution polt, and a code outputs corresponding visualization in 3D.
In Simulation of RNA, the code titled "simulation of mrna with or without ribosomes" is a simulation code that output the 5'-3' distribution from the samples of simulation, and code titled "Visualization mrna with or without ribosomes" is a simulation code that generates one strand of input length of RNA onto 3D Cartesian coordinates.
In Simulation of RNA on a surface,  the code titled "mRNA on a surface" and "Visualization mRNA on a surface" works the same as discussed above, except it simulates for a RNA that localized onto a surface. "Visualization of mRNA on surface with plane" is the visualization of mRNA on a surface displayed with its reference plane z=0.
Trajectory movie is a code that simulations 100 nucleotides long RNA strand and outputs for plot when each single strand is added, this can form a trajectory movie by stacking the images with the aid of image analyzer tool like FiJi.
## Instructions
Generally, to use the code, it just needs three inputs: sample number, the RNA length in numbers of nucleotide, and the number of ribosomes.
The first place ask for input is at the first looping function, which is indicated in each code, to input sample number\\
The second place ask for input is at the second looping function, which is indicated in each code, to input RNA length, the input equation is Length - 30 * (ribosome number)\\
The third place ask for input is at the ribosome() function, which is indicated in each code, to input the number of ribosomes
