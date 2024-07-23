irises = [
    {'sepal_length': '5.1', 'sepal_width': '3.5', 'petal_length': '1.4', 'petal_width': '0.2',
     'species': 'Iris-setosa'},
    {'sepal_length': '4.9', 'sepal_width': '3', 'petal_length': '1.4', 'petal_width': '0.2', 'species': 'Iris-setosa'},
    {'sepal_length': '4.7', 'sepal_width': '3.2', 'petal_length': '1.3', 'petal_width': '0.2',
     'species': 'Iris-setosa'},
    {'sepal_length': '4.6', 'sepal_width': '3.1', 'petal_length': '1.5', 'petal_width': '0.2',
     'species': 'Iris-setosa'},
    {'sepal_length': '5', 'sepal_width': '3.6', 'petal_length': '1.4', 'petal_width': '0.2', 'species': 'Iris-setosa'},
    {'sepal_length': '7', 'sepal_width': '3.2', 'petal_length': '4.7', 'petal_width': '1.4',
     'species': 'Iris-versicolor'},
    {'sepal_length': '6.4', 'sepal_width': '3.2', 'petal_length': '4.5', 'petal_width': '1.5',
     'species': 'Iris-versicolor'},
    {'sepal_length': '6.9', 'sepal_width': '3.1', 'petal_length': '4.9', 'petal_width': '1.5',
     'species': 'Iris-versicolor'},
    {'sepal_length': '5.5', 'sepal_width': '2.3', 'petal_length': '4', 'petal_width': '1.3',
     'species': 'Iris-versicolor'},
    {'sepal_length': '6.5', 'sepal_width': '2.8', 'petal_length': '4.6', 'petal_width': '1.5',
     'species': 'Iris-versicolor'},
    {'sepal_length': '6.3', 'sepal_width': '3.3', 'petal_length': '6', 'petal_width': '2.5',
     'species': 'Iris-virginica'},
    {'sepal_length': '5.8', 'sepal_width': '2.7', 'petal_length': '5.1', 'petal_width': '1.9',
     'species': 'Iris-virginica'},
    {'sepal_length': '7.1', 'sepal_width': '3', 'petal_length': '5.9', 'petal_width': '2.1',
     'species': 'Iris-virginica'},
    {'sepal_length': '6.3', 'sepal_width': '2.9', 'petal_length': '5.6', 'petal_width': '1.8',
     'species': 'Iris-virginica'},
    {'sepal_length': '6.5', 'sepal_width': '3', 'petal_length': '5.8', 'petal_width': '2.2',
     'species': 'Iris-virginica'}
]

with open("iris_02.csv", "w") as iris_w:
    header = ",".join(list(irises[0])) + "\n"
    iris_w.write(header)

    for iris in irises:
        iris_w.write(",".join(iris.values()) + "\n")
