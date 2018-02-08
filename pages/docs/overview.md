title: Overview
pagenav_title: Guild AI overview
tags: concepts

# Guild AI overview

[TOC]

Guild AI is a toolset for packaging and using deep learning models. It
shares many features with traditional software package managers like
`pip`, `npm` and `Homebrew` but provide specialized functionality for
deep learning models.

## Packages

Packages are containers for [models](#models) and required
[resources](#resources). They are the basis of deep learning model
distribution in Guild AI.

You can discover packages [online](/models/) or by using Guild's
[](cmd:search) command.

<a class="btn btn-primary" href="/docs/packages/">More about packages<i class="fa next"></i></a>

## Models

<a class="btn btn-primary" href="/docs/models/">More about models<i class="fa next"></i></a>

## Operations

Operations are *actions* that you can perform on a model. The most
common operation in deep learning is `train`, which optimizes a model
using data. But operations can be anything at all!

Examples of operations that a model might provide include:

`train`
: Train a model --- nearly every model supports it!

`fine-tune`
: Fine-tune a model using a pretrained model as a starting point.

`evaluate`
: Measure model performance using a test dataset.

`optimize`
: Optimize a model for a target environment (e.g. compress the model
  size for mobile applications)

`deploy`
: Deploy a model to a target environment.

<a class="btn btn-primary" href="/docs/operations/">More about
operations<i class="fa next"></i></a>

## Runs

A *run* is generated each time you start an operation with the
[](cmd:run) command. Runs preserves the outcome of each experiment,
allowing you to analyze your results and make informed decisions about
next steps.

<a class="btn btn-primary" href="/docs/runs/">More about runs <i
class="fa next"></i></a>

## Resources

<a class="btn btn-primary" href="/docs/resources/">More about resources <i
class="fa next"></i></a>
