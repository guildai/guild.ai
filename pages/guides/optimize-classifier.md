# Optimize Get Started Classifier

[TOC]

## Overview

This guide runs a more exhaustive hyperparameter tuning process for
the Iris classifier in [Get Started](/start/classifier.md).

Topics covered:

- Search methods
- Use of pipeline ([steps](ref:steps)) to automate search

## Iris SVM Classifier

This guide optimizes the Iris classifier implemented in
[`plot_iris_exercise.py`](ext:https://raw.githubusercontent.com/guildai/examples/master/iris-svm/plot_iris_exercise.py).

The classifier is adopted from [*scikit-learn SVM Exercise*
->](https://scikit-learn.org/stable/auto_examples/exercises/plot_iris_exercise.html).

The original scikit-learn example hard-coded a number of
hyperparameters that we want to expose as flags so that we can search
over various spaces to find values that maximize classification
accuracy.

The classifier uses C-Support Vector Classification. For details, see
[sklearn.svm.SVC
->](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html).

## Create a Project
