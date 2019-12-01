# Project Network Science

This repository contains an app developed with the package pygame that simulates the Schelling's Segregation Model (references at the end of README).
In order to run everything properly, you need to have the following Python packages installed:
- pygame
- numpy

The main file, which runs the app, is simulation.py. This file needs some classes that are in the other files of these repository.

The app has three different screens. The first one allows you to choose between two categories of simulation.
The categories are 'Neighbourhoods' and 'Regular Model', which are explained in more detail below.
After choosing one of these, you will have to set the parameters of the chosen each model. 
Then, you can press the button 'Run' and it will open the last screen and run the simulation.

Regular Model

The category 'Regular Model' runs Schelling's Model with just small modifications.
You can set the number of traits (the distinguishing factors between the individuals) from 2 to 5, whereas Schelling's Model only allows 2.
Also, you can vary the minimum and maximum percentages that each individual needs as neighbours with the same traits as themselves.
The percentages of each trait can also be set, as well as the percentage of empty spots. 
The size (widht and height) of the city grid is also changeable.

Neighbourhoods

The category 'Neighbourhoods' was an idea that we had to test Schelling's Model in several separated neighbourhoods that are part of the same city.
In this simulation, you can choose the same parameters as in the regular one but instead of choosing the size of the city, you are choosing the size of each neighbourhood.
Beside, you also choose the amount of neighbourhoods you wish.
However, we do not have a feature that generates different neighbourhoods.
It creates them all with the same size.

Files

- box.py contains a class that can be used to generate boxes for all purposes.
- button.py contains a button class that inherites the properties of box and has several others. For example, it can be used to activate some function, like changing screens.
- text_box.py contains a text_box class that inherites the properties of box and has several others. For example, it can be used to write text in it that can be converted in inputs for the simulation.
- first_screen.py contains a class that generates the first window of the app.
- main_screen.py contains a class that generates the window that is shown after choosing the category in the previous one.
- running_screen.py contains a class that generates the window in which the simulation is run.
- screen.py is a general class for creating a window. It was not developed but all the other screen classes inherite from it.
- city.py is a class that is used for the simulation of the 'Regular Model' category. It contains the inputs given and uses them to do the simulation intended.
- city_neigh.py is a class that is used for the simulation of the 'Neighbourhoods' category. It contains the inputs given and uses them to do the simulation intended.

References

- [1] McCown, F. Schelling’s Model of Segregation.
Available from: http://nifty.stanford.edu/2014/mccown-schelling-model-segregation/
- [2] Easley, D. and J. Kleinberg, Networks, crowds, and markets: Reasoning about a highly connected
world. 2010: Cambridge University Press.
Available from: https://www.cs.cornell.edu/home/kleinber/networks-book/networks-book.pdf
- [3] Schelling, T.C., Dynamic models of segregation. Journal of Mathematical Sociology, 1971. 1(2):
p. 143-186.
Available from: http://norsemathology.org/longa/classes/stuff/DynamicModelsOfSegregation.pdf
- [4] Hart, V. and N. Case. Parable of the polygons: A playable post on the shape of society.
Available from: http://ncase.me/polygons
