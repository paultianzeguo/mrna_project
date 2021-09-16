## Introduction
TRIP (Three-dimensional RNA Illustration Program) is a set of separate Python scripts to simulate the 3D RNA folding shape based on hypothesized polymer model.
The set of codes is separated into six different files, which categorized into three main parts: 

1. Simulation of RNA 

  -mRNA simulation with or without ribosomes

  -Visualization mrna with or without ribosomes

2. Simulation of RNA on a surface

  -mRNA on a surface

  -Visualization mRNA on a surface

  -Visualization of mRNA on surface with plane

3. Trajectory movie

  -Trajectory movie

The first two categories each contains a script that outputs a distribution plot, and a script outputs the corresponding visualization in 3D Cartesian coordinates.
In Simulation of RNA, the script titled "simulation of mrna with or without ribosomes" is a simulation code that output the 5'-3' distribution from the samples of simulation, and code titled "Visualization mrna with or without ribosomes" is a simulation code that generates one strand of input length of RNA onto 3D Cartesian coordinates.

In Simulation of RNA on a surface,  the script titled "mRNA on a surface" and "Visualization mRNA on a surface" works the same as discussed above, except it simulates for a RNA that localized onto a surface. "Visualization of mRNA on surface with plane" is the visualization of mRNA on a surface displayed along with its reference plane z=0.

Trajectory movie is a code that simulations 100 nucleotides long RNA strand and outputs for plot when each single strand is added, this can form a trajectory movie by stacking the images with the aid of image analyzer tool FiJi.

## Instructions
Generally, to use the scripts, it shall be lauched and run in a python environment. It just needs three inputs: sample number, the RNA length in numbers of nucleotide, and the number of ribosomes.

The first place ask for input is at the first looping function, for example

![image](https://user-images.githubusercontent.com/75511362/133612275-fa74cd18-cd7a-475c-8e67-eba2f62f9dce.png)

which is indicated in each code, to input sample number in the parentheses. The sample number is set default to be 1000. To account for faster runtime or higher accuracy, the sample number can be manually adjusted.

The second place ask for input is at the second looping function, for example

![image](https://user-images.githubusercontent.com/75511362/133612501-029a9fb3-c56f-4b91-8876-b7f45b67d6b2.png)

which is indicated in each code, to input RNA length in the parentheses, the input equation is Length - 30 * (ribosome number), it can either take the equation (e.g. 10000-30*50), or the result (e.g. 8500).

The third place ask for input is at the ribosome() function, 

![image](https://user-images.githubusercontent.com/75511362/133612850-264ec8c0-8736-45ca-99ef-e2cde6a77691.png)


which is indicated in each code, to input the number of ribosomes in the parentheses.
