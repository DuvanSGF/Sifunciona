# -*- coding: utf-8 -*-

from sklearn import tree
features = [[7, 0.6, 40], [7, 0.6, 41], [37, 600, 37], [37, 600, 38]]
#labels = [chicken, chicken, horse, horse]
labels = [0, 0, 1, 1]
classif = tree.DecisionTreeClassifier()
classif.fit(features, labels)

print(classif.predict([[38, 600, 37.5]]))
 
# output
# [1]  or a Horse

from sklearn import tree
#Features = [ temperatura, Humeadad]
features = [[22, 89], [33, 60], [41, 35], [15, 99]]
#labels = [Frio, Templado, Soleado, LLuvioso]
labels = ["Frio", "Templado", "Soleado", "LLuvioso"]
classif = tree.DecisionTreeClassifier()
classif.fit(features, labels)

print(classif.predict([[12, 78]]))

# output
# ['LLuvioso']  