ags: get-started

# Train an Image Classifier

In this guide, we train an image classifier on the Fashion-MNIST data
set.

![Fashion-MNIST](/assets/img/fashion-mnist.png)

[TOC]

## Requirements

{!start-requirements.md!}

## Image classifier training script

In this step, we create a script named `fashion_mnist_mlp.py`, which
is an image classifier training script adapted from the Keras
examples. [^example-src]

[^example-src]: The training script for the image classifier is
    adapted from [keras/examples/mnist_mlp.py on GitHub
    ->](https://github.com/keras-team/keras/blob/master/examples/mnist_mlp.py)

The training script we create in this step doesn't actually train
anything, but instead simulates the training process of accepting
hyperparameters as inputs and generating a *[loss
->](https://en.wikipedia.org/wiki/Loss_function)*.

If you haven't done so already, create a new directory for the
project:

``` command
mkdir guild-start
```

Create a file named `fasion_mnist_mlp.py`, located in the
`guild-start` directory:

``` python
from tensorflow import keras

from keras.datasets import fashion_mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop

batch_size = 128
epochs = 5
dropout = 0.2
lr = 0.001
lr_decay = 0.0
rho = 0.0

(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255
y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)

model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(784,)))
model.add(Dropout(dropout))
model.add(Dense(512, activation='relu'))
model.add(Dropout(dropout))
model.add(Dense(10, activation='softmax'))

model.compile(
    loss='categorical_crossentropy',
    optimizer=RMSprop(lr=lr, rho=rho, decay=lr_decay),
    metrics=['accuracy'])

model.fit(
    x_train, y_train,
    batch_size=batch_size,
    epochs=epochs,
    verbose=1,
    validation_data=(x_test, y_test),
    callbacks=[keras.callbacks.TensorBoard()])
```

^ guild-start/fashion_mnist_mlp.py

As an alternative to copying the script, download
[fashion_mnist_mlp.py
->](https://raw.githubusercontent.com/guildai/examples/master/start/fashion_mnist_mlp.py)
and save it to the `guild-start` directory.

Verify that your project structure is:

<div class="file-tree">
<ul>
<li class="is-folder open">guild-start
 <ul>
 <li class="is-file">fashion_mnist_mlp.py</li>
 <li class="is-file disabled">echo.py <small>(from <a href="/docs/start/">Quick Start</a> - not used in this guide)</small></li>
 <li class="is-file disabled">train.py <small>(from <a href="/docs/start/">Quick Start</a> - not used in this guide)</small></li>
 </ul>
</li>
</ul>
</div>

## Train with default settings

In a command console, change to the `guild-start` project:

``` command
cd guild-start
```

Run `fashion_mnist_mlp.py`:

``` command
guild run fashion_mnist_mlp.py
```

``` output
You are about to run fashion_mnist_mlp.py
  batch_size: 128
  dropout: 0.2
  epochs: 5
  lr: 0.001
  lr_decay: 0.0
  rho: 0.0
Continue? (Y/n)
```

Press `Enter` to start training.

By default, the script is configured to train over 5 epochs.

## Train classifier over more epochs

## Compare runs

## Optimize learning rate

## Summary

## Next Steps

{!start-reproducibility.md!}

{!start-tensorboard.md!}

{!start-diff.md!}

{!start-backup-restore.md!}

{!start-remote-train.md!}
