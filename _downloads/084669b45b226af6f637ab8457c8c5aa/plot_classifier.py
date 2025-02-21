"""
=======================================
Plotting Fuzzy Decision Tree Classifier
=======================================

An example plot of :class:`FuzzyDecisionTreeClassifier`
"""

from matplotlib import pyplot as plt
from mlxtend.plotting import plot_decision_regions
from sklearn.datasets import make_blobs

from fuzzytree import FuzzyDecisionTreeClassifier

X, y = make_blobs(
    n_samples=300,
    n_features=2,
    centers=[[10, 0], [20, 30], [40, 5]],
    cluster_std=[7, 11, 13],
    random_state=42,
)

clf = FuzzyDecisionTreeClassifier().fit(X, y)

plot_decision_regions(X=X, y=y, clf=clf, legend=2)
plt.title("Fuzzy Tree Classification on blobs")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")

plt.show()
