# SimonTask
Basic Programming in Python -- Final Project by Johanna Schillig, Georg Fasching, Franka TImm

# Replication and implementation of the Simon Task Experiment in Python

This repository contains an implementation of the „Simon Task Experiment“.

The „Simon Task Experiment“ was originally conducted in the late 1960s in order to explore specific reaction tendencies and resulting reaction time latencies when detecting a target visually. The so called „Simon Effect“ which is named after the conducting researcher J.R. Simon functioned as the original hypothesis and its existence could be replicated in numerous follow-up studies. The „Simon Effect“ describes the circumstance that reaction times decrease when the target and the required action (e.g. a button that is to be pressed) are located close to each other and increases when they lie at opposite positions. In the original experiment the stimuli were 2 colored circles to which  respective buttons were assigned. The stimuli were then presented either in the congruent condition, meaning on the side of the respective button or incongruent on the opposite side. The presentation of the different colors was shuffled so that the participants had to identify the color first in each trial. The reaction times for both conditions were measured and compared and it was found that the hypothesis actually holds.

# Experiment

The experiment uses a 3x3x2 design consisting of the factors congruency, color and validity which have the respective levels congruent/incongruent/baseline, blue/green/white, true/false. The design differs from the original design in the addition of a baseline for each participant in which the reaction time for a neutral position of stimulus and reaction key is measured. Like the original experiment it is conducted as a within-subject design.

# Python

Here the „Simon Task Experiment“ is to be replicated in Python using the package Expyriment and the collected data is analyzed and plotted with the help of Matplot, Scipy, Pandas and Seaborn. In addition the Numpy package and the Random package are used.

# Running the Experiment
 
Offline: Close the repository, install the required packages and run the experiment on your local machine.
