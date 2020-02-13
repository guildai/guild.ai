# Dependencies

[TOC]

## Introduction

Guild AI strives to minimize dependencies on software libraries and
external systems. Specifically, Guild does not require:

- Changes to your source code --- experiment tracking features are
  configured in a separate text file
- Databases or networked file system --- experiments are saved to the
  local file system
- Containers or container infrastructure --- everything is run as a
  standard operating system process
- Agents or long running services

Dependencies are costly. The impact your software in a number of ways:

- Increased complexity (complexity cost)
- Limitations of features when compared to alternatives (feature
  limitation cost)
- Increased risk associated with breaking upstream changes (breaking
  change cost)
- Limitation of portability to other environments and collaborators
  (portability cost)

Complex tools are costly to run. If an experiment tracking tool
requires an external database system, you not only need to install and
configure that system, you need to maintain it, upgrade it, and
monitor it. This requires specialized engineering expertise and in
some cases, dedicated support staff.

Feature limitation cost is when a library feature limits your
abilities in other areas. If an experiment tracking library requires
that models adhere to a specific interface to be used in experiment
tracking, any model that doesn't adhere to that interface can't be
used.

A breaking change cost is incurred when your upstream experiment
tracking system fails unexpectedly due to a change in its code or any
code it relies on. While you can expect that all software is
thoroughly tested, larger and more complex dependency chains are more
likely to fail than smaller, simpler ones.

Complex dependencies makes it harder to run scripts in different
environments. Each environment has to be configured to support the
requirements. These requirement may exclude some collaborators who
don't have the technical expertise or support personnel to install,
configure, and maintain required systems.

## Sample Training Script

Consider the following script `train.py`:

``` python
import fashion_mnist

learning_rate = 0.1
epochs = 10

trained_model = fashion_mnist.train(learning_rate, epochs)
trained_model.save()

print("accuracy: %f" % trained_model.accuracy)
```

An experiment tracking tool must address three topics when running
this script:

- How to specify and record the values of `learning_rate` and `epochs`
  (hyperparameters)
- Where to write the trained model (generated artifact)
- How to record the model accuracy (metrics)

As it is, the script depends on the Python module `fashion_mnist`,
which we assume is part of the project and not related to experiment
tracking.

## Modifications to Support Experiment Tracking

Consider modifications to `train.py` that add support for experiment
tracking provided by a hypothetical library named `experiments`.

``` python
import experiments as exp

import fashion_mnist

learning_rate = exp.hparam(0.1)
epochs = exp.hparam(10)

trained_model = fashion_mnist.train(learning_rate, epochs)
exp.save_model(trained_model)

print("accuracy: %f" % trained_model.accuracy)
exp.log_metric("accuracy", trained_model.accuracy)
```

The changes are simple and clean. Without considering their cost, the
effort of adding them appears justified given the benefit of
experiment tracking.

Let's consider their cost.

Global variables `learning_rate` and `epochs` are explicitly noted by
defining them with an `hparam` function. This is arguably an
improvement to the code as it makes this interface clear. The scheme
nonetheless incurs portability cost. Collaborators can no longer run
the script in different environments without first satisfying the
experiment tracking requirements.

The call to `exp.save_model()` is high cost if it limits the types of
models that can be saved. This is a feature limitation cost. The save
operation might work in the case of our sample, but if the author
wants to change the model implementation (e.g. from TensorFlow to
PyTorch, PyTorch to Keras, etc.) the save operation may not work. If
not, the author may be forced to re-implement the model simply to
satisfy the requirements of an experiment management framework.

If `experiments` saves models to a database, you incur complexity
cost. If the database is external, you have to ensure it's available
at the time the model is saved or risk losing your saved model. The
complexity extends to loading your saved model.

Saving metrics like training accuracy is similar to saving a model. If
the metrics are written to a database, the database must be available.

## Guild's Approach

Guild AI takes a strong position on dependencies. They're something to
avoid whenever possible. When a dependency is required, it should be
minimized as much as possible without compromising features.
