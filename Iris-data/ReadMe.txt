The Iris dataset was used in R.A. Fisher's classic 1936 paper, The Use of Multiple Measurements in Taxonomic Problems, and can also be found on the UCI Machine Learning Repository.

The purpose of this project is to explore data visualization techniques utilizing the Iris dataset.This project seeks to reproduce, and to visually modify the given code.

It includes three iris species with 50 samples each as well as some properties about each flower. One flower species is linearly separable from the other two, but the other two are not linearly separable from each other.

The use of multiple measurements in taxonomic problems. It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species. The data set consists of 50 samples from each of three species of Iris (Iris Setosa, Iris virginica, and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters.

The columns in this dataset are:

    SepalLengthCm
    SepalWidthCm
    PetalLengthCm
    PetalWidthCm
    Species


The class variale is "Species". It has 3 number of classes.

Classes are below:

	Iris-setosa
	Iris-versicolor
	Iris-virginica

These 3 classes depends upon 4 features.

Description of Every Columns

sepal_length
count    150.000000
mean       5.843333
std        0.828066
min        4.300000
25%        5.100000
50%        5.800000
75%        6.400000
max        7.900000
Name: sepal_length, dtype: float64

sepal_width
count    150.000000
mean       3.054000
std        0.433594
min        2.000000
25%        2.800000
50%        3.000000
75%        3.300000
max        4.400000
Name: sepal_width, dtype: float64

petal_length
count    150.000000
mean       3.758667
std        1.764420
min        1.000000
25%        1.600000
50%        4.350000
75%        5.100000
max        6.900000
Name: petal_length, dtype: float64

petal_width
count    150.000000
mean       1.198667
std        0.763161
min        0.100000
25%        0.300000
50%        1.300000
75%        1.800000
max        2.500000
Name: petal_width, dtype: float64

species
count             150
unique              3
top       Iris-setosa
freq               50
Name: species, dtype: object

To Duplicate the results
Run Requirements.txt
using pip install -r requirements.txt

then enter below command
python analysis.py



