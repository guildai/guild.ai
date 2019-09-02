layout: front-page
hide_sidenav: yes
hide_pagenav: yes
hide_in_pagenav: yes
title: Experiment Tracking for Machine Learning Engineers

<div id="get-started-fab"></div>

<div class="row match-height logos">
  <img src="/assets/img/tensorflow-logo.png" width="150">
  <img src="/assets/img/pytorch-logo.png" width="140">
  <img src="/assets/img/keras-logo.png" width="110">
  <img src="/assets/img/scikit-learn-logo.png" width="95">
  <img src="/assets/img/mxnet-logo.png" width="105">
  <img src="/assets/img/xgboost-logo.png" width="105">
</div>

---

<p markdown="1" class="highlight">

Guild AI is a toolkit that helps you track experiments, compare
results, and automate your machine learning workflow. Run your
unmodified training scripts to automatically capture unique
experiments and leverage Guild's analysis and optimization features.

</p>

---

<div class="row match-height other-features">

  <div class="col-lg-6">
    <img class="feature-icon" src="/assets/icons/folder-check.svg">
    <h4>Track Experiments</h4>
    <p>

      Guild automatically captures every detail of your training runs
      as unique experiments.

    </p>
  </div>

  <div class="col-lg-6">
    <img class="feature-icon" src="/assets/icons/analytics-graph.svg">
    <h4>Compare and Analyze Runs</h4>
    <p>

      Use results to deepen your understanding and incrementally
      improve your models.

    </p>
  </div>

  <div class="col-lg-6">
    <img class="feature-icon" src="/assets/icons/seo-search-star.svg">
    <h4>Tune Hyperparameters</h4>
    <p>

      Find optimal hyperparameters and model architecture without
      setting up complicated trials.

    </p>
  </div>

  <div class="col-lg-6">
    <img class="feature-icon" src="/assets/icons/hierarchy.svg">
    <h4>Automate Workflow</h4>
    <p>

      Save time and avoid costly mistakes by automating your training
      steps.

    </p>
  </div>

  <div class="col-lg-6">
    <img class="feature-icon" src="/assets/icons/cloud-server.svg">
    <h4>Train and Backup Remotely</h4>
    <p>

      Train on GPU accelerated systems running in the cloud on
      on-prem.

    </p>
  </div>

  <div class="col-lg-6">
    <img class="feature-icon" src="/assets/icons/common-file-text-share.svg">
    <h4>Publish and Share Results</h4>
    <p>

      Share your results with colleagues through HTML, Markdown or
      LaTex based reports.

    </p>
  </div>

  <div class="col-lg-6">
    <img class="feature-icon" src="/assets/icons/app-window-code.svg">
    <h4>Command Line Interface</h4>
    <p>

      Use your current console based work flow with Guild's POSIX
      compliant interface.

    </p>
  </div>

  <div class="col-lg-6">
    <img class="feature-icon" src="/assets/icons/file-py.svg">
    <h4>Python API</h4>
    <p>

      Use Notebooks or interactive shells with Guild's Python
      interface.

    </p>
  </div>
</div>

---

<div class="row feature">
  <div class="hidden-xs col-sm-2">
    <img class="icon" src="/assets/icons/railroad-fast-train-1.svg">
  </div>
  <div class="col-sm-10">
    <h2><strong>Start Fast</strong> - Run your script directly</h2>
    <p>
      Run your code <strong>without modification</strong>
      to <strong>automatically capture</strong> unique experiments.
    </p>
    <div class="text-editor">
      <div class="text-body">
        $ <span id="typed-run"></span><span class="typed-cursor">|</span>
      </div>
    </div>
  </div>
</div>

<div class="row feature">
  <div class="hidden-xs col-sm-2">
    <img class="icon" src="/assets/icons/file-code-settings-1.svg">
  </div>
  <div class="col-sm-10">
    <h2><strong>Configure a Project</strong> - Use a Guild file for more control</h2>

    <p>

      Add a Guild file (named <code>guild.yml</code>) to your project
      to <strong>make things explicit</strong> and to keep experiment
      configuration <strong>outside your code</strong>.

    </p>

    <pre data-toolbar="hide"><code class="language-yaml">
        train-mnist:
          description: Train CNN on MNIST images
          main: train
          flags:
            lr:
              description: Learning rate
              default: 0.01
            batch_size:
              description: Training batch size
              default: 100
          requires:
            - http://pub.guild.ai/mnist.tar.gz

        eval-mnist:
          description: Evaluate a trained model
          main: eval
          requires: train-mnist
    </code></pre>

    <p>

      Guild files also <strong>document the interface</strong> to your
      project.

    </p>

  </div>
</div>

<div class="row feature">
  <div class="hidden-xs col-sm-2">
    <img class="icon" src="/assets/icons/seo-search-graph-1.svg">
  </div>
  <div class="col-sm-10">
    <h2><strong>Study Results</strong> - Better understand your model with real data</h2>
    <div class="text-editor">
      <div class="text-body">
        $ <span id="typed-view-and-compare"></span><span class="typed-cursor">|</span>
      </div>
    </div>
    <div class="view-and-compare-preview">
      <img id="view-and-compare-img-compare" class="show-hide md shadow" src="/assets/img/compare-4.png">
      <div id="view-and-compare-img-tensorboard" class="show-hide">TensorBoard</div>
      <div id="view-and-compare-img-view" class="show-hide">View</div>
      <div id="view-and-compare-img-open" class="show-hide">Open</div>
      <div id="view-and-compare-img-diff" class="show-hide">Diff</div>
      <div id="view-and-compare-img-info" class="show-hide">Info</div>
      <div id="view-and-compare-img-cat" class="show-hide">Cat</div>
    </div>
  </div>
</div>

---

TODO: Move the "Features" stuff from the old site into the sections
below. This is just an elaboration on the grid items above with
samples, images, etc.

Each section *must* be very short and to te point, with a single image
to convey what it is. Include: what it is and why it's important.

<div id="features"></div>

## Manage Experiments

## Compare and Analyze Runs

## Tune Hyperparameters

## Automate Workflow

## Publish and Share Results

## Train and Backup Remotely

## Command Line Interface

## Python API

---

OLD STUFF

# Run experiments

### Run your training script with Guild to generate an experiment

<div class="row">
  <div class="col-lg-12">
    <div class="text-editor inline">
      <div class="text-body">
        $ <span class="typed-cursor">guild run train.py learning-rate=0.1</span>
      </div>
    </div>
    <ul class="md features">
      <li>Guild runs your script directly &mdash; no need to change
        your code</li>
      <li>Captures <i>files</i>, <i>metrics</i>, <i>output</i>, and
        <i>logs</i> as a unique experiment</li>
    </ul>
  </div>
</div>

<a class="btn btn-default btn-promo-next" href="/docs/start/">
  Get started with experiments<i class="fa next"></i></a>

### Run multiple trials for a set of choices (Grid Search)

<div class="row">
  <div class="col-lg-12">
    <div class="text-editor inline">
      <div class="text-body">
        $ <span class="typed-cursor">guild run train.py learning-rate=[0.1,0.2,0.3]</span>
      </div>
    </div>
    <ul class="md features">
      <li><code>[0.1,0.2,0.3]</code> is a list of three values &mdash; Guild runs a trial for each</li>
      <li>Runs trials over the Cartesian product of all values &mdash;
      i.e. performs a <i>grid search</i></li>
    </ul>
  </div>
</div>

<a class="btn btn-default btn-promo-next" href="/docs/start/grid-search/">
  Get started with Grid Search <i class="fa next"></i></a>

### Run trials for a range (Random Search)

<div class="row">
  <div class="col-lg-12">
    <div class="text-editor inline">
      <div class="text-body">
        $ <span class="typed-cursor">guild run
        train.py learning-rate=[0.1:0.3] --max-trials 10</span>
      </div>
    </div>
    <ul class="md features">
      <li><code>[0.1:0.3]</code> is a range of values &mdash; from
      minimum to maximum</li>
      <li>In this example Guild runs 10 trials, selecting values at
      random over a uniform distribution</li>
    </ul>
  </div>
</div>

<a class="btn btn-default btn-promo-next" href="/docs/start/random-search/">
  Get started with Random Search <i class="fa next"></i></a>

### Find the best hyperparameters using Bayesian optimization

<div class="row">
  <div class="col-lg-12">
    <div class="text-editor inline">
      <div class="text-body">
        $ <span class="typed-cursor">guild run
        train.py x=[-2.0:2.0] --optimizer bayesian</span>
      </div>
    </div>
    <ul class="md features">
      <li>Use <code>--optimizer</code> to minimize (or maximize) an objective</li>
      <li>Guild supports the latest Bayesian optimizers including
      <i>gaussian process</i>, <i>decision trees</i>, and <i>gradient boosted
        trees</i></li>
    </ul>
  </div>
</div>

<a class="btn btn-default btn-promo-next" href="/docs/start/optimization/">
  Guide to Hyperparameter Optimization<i class="fa next"></i></a>

---

# Analyze and Compare Results

### Compare experiments

<div class="row">
  <div class="col-lg-12">
    <div class="text-editor inline">
      <div class="text-body">
        $ <span class="typed-cursor">guild compare</span>
      </div>
    </div>
    <p>After running experiments, use <code>guild compare</code> to
    launch an interactive spreadsheet-like application to explore,
    sort, and compare results.</p>
    <figure>
      <p><img class="md terminal lozad shadow" data-src="/assets/img/compare-1.png" /></p>
      <figcaption class="under-shadow">Interactive compare application</figcaption>
    </figure>
    <ul class="md features">
      <li>Spreadsheet-like application to compare experiment results</li>
      <li>Flexible display &mdash; customize what you see from the command line</li>
      <li>Mark best results for export or use in other trials</li>
    </ul>
  </div>
</div>

<a class="btn btn-default btn-promo-next" href="/docs/guides/compare/">
  Guide to comparing runs <i class="fa next"></i></a>

### Export to CSV or JSON

<div class="row">
  <div class="col-lg-12">
    <div class="text-editor inline">
      <div class="text-body">
        $ <span class="typed-cursor">guild compare --csv > results.csv</span>
      </div>
    </div>
    <ul class="md features">
      <li></li>
      <li>Generate CSV or JSON files containing experiment details</li>
      <li>Use with other tools and programs to analyze and visualize
      results</li>
    </ul>
  </div>
</div>

<a class="btn btn-default btn-promo-next" href="/docs/guides/export-runs/">
  Guide to exporting runs <i class="fa next"></i></a>

### Integrated visualizers

<div class="row">
  <div class="col-lg-12">
    <div class="text-editor inline">
      <div class="text-body">
        $ <span class="typed-cursor">guild view</span>
      </div>
    </div>
    <p>Use <code>guild view</code> to start a browser-based
      application to explore and compare experiment results.</p>
  </div>
  <div class="col-lg-6">
    <figure>
      <p><img class="md shadow lozad" data-src="/assets/img/view-files.jpg" /></p>
      <figcaption class="under-shadow">Files associated with a trial</figcaption>
    </figure>
  </div>
  <div class="col-lg-6">
    <figure>
      <p><img class="md shadow lozad" data-src="/assets/img/view-output.jpg" /></p>
      <figcaption class="under-shadow">Trial output</figcaption>
    </figure>
  </div>
  <div class="col-lg-12">
    <ul class="md features">
      <li>Explore and compare trial results in a browser</li>
      <li>Run as a shared server to support group collaboration</li>
      <li>Seamless integration with TensorBoard to view trial scalars
      (e.g. loss, accuracy, etc.)  and other logged events</li>
    </ul>
  </div>

  <div class="col-lg-12">
    <div class="text-editor inline">
      <div class="text-body">
        $ <span class="typed-cursor">guild tensorboard</span>
      </div>
    </div>
    <p>TensorBoard is used to study and compare trial metrics and
      generated output. Use <code>guild tensorboard</code> to quickly
      and easily start TensorBoard for your experiments.</p>
  </div>
  <div class="col-lg-6">
    <figure>
      <p><img class="md shadow lozad" data-src="/assets/img/tb-feature.jpg" /></p>
      <figcaption class="under-shadow">Compare experiment results in TensorBoard</figcaption>
    </figure>
  </div>
  <div class="col-lg-6">
    <figure>
      <p><img class="md shadow lozad" data-src="/assets/img/tb-feature-2.jpg" /></p>
      <figcaption class="under-shadow">View and compare model architecture</figcaption>
    </figure>
  </div>
  <div class="col-lg-12">
    <ul class="md features">
      <li>Compare loss, accuracy and other training metrics across runs</li>
      <li>Guild keeps TensorBoard up-to-date as you run new trials</li>
      <li>Support for generating TensorBoard logs automatically from training output</li>
    </ul>
  </div>
</div>


### Diff changes across experiments

<div class="row">
  <div class="col-lg-12">
    <div class="text-editor inline">
      <div class="text-body">
        $ <span class="typed-cursor">guild diff</span>
      </div>
    </div>
    <p>Use <code>guild diff</code> to compare two trials.</p>
  </div>
  <div class="col-lg-6">
    <figure>
      <p><img class="md shadow lozad" data-src="/assets/img/meld.jpg" /></p>
      <figcaption class="under-shadow">Detailed diff of two runs (trials)</figcaption>
    </figure>
  </div>
  <div class="col-lg-6">
    <figure>
      <p><img class="md shadow lozad" data-src="/assets/img/meld-diff.jpg" /></p>
      <figcaption class="under-shadow">Diff source code changes between two runs</figcaption>
    </figure>
  </div>
  <div class="col-lg-12">
    <ul class="md features">
      <li>Compare every detail: <i>hyperparameters</i>, <i>source
      code</i>, <i>logs</i>, <i>command</i>, environment and any
      generated file</li>
      <li>Use to answer, <i>&ldquo;What changed between these two runs
      that may have influenced this result?&rdquo;</i></li>
      <li>Customize using the diff tools of your choice</li>
    </ul>
  </div>
</div>

---

# Reproducibility

<div class="row match-height steps">
  <div class="col-lg-4 step">
    <i class="far fa-file-alt"></i>
    <h4>Step 1: Add a Guild file<br>to your project</h4>
    <p>
      A Guild file is a simple text file named <code>guild.yml</code>
      that describes the operations for your project. Guild files
      support a range of features that automate reproducibility
      &mdash; just it to your project root and you're done!
    </p>
  </div>
  <div class="col-lg-4 step">
    <i class="far fa-bullhorn"></i>
    <h4>Step 2: Share your code<br>with colleagues</h4>
    <p>
      By adding a Guild file to your project, you make it easy for
      colleagues and other researchers to recreate your
      experiments. Simply share your project code through GitHub or
      your favorite version control system.
    </p>
  </div>
  <div class="col-lg-4 step">
    <i class="far fa-users-cog"></i>
    <h4>Step 3: Colleagues use Guild<br>to recreate experiments</h4>
    <p>
      After cloning your project repo, others can recreate your
      experiments using the <code>guild run</code> command. Guild
      takes care of everything needed to train your model and captures
      the results for easy comparison.
    </p>
  </div>
</div>

### Guild file &mdash; instructions for recreating an experiment

<div class="row">
  <div class="col-lg-9">
    <pre class="language-yaml gf-sample">train.py:
  flags:
    epochs: 3
    activation:
      default: relu
      choices:
        - relu
        - sigmoid
    num_dense_layers: 1
    num_dense_nodes: 16
    learning_rate: 1e-5
  requires:
   - url: http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz
   - url: http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz
   - url: http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz
   - url: http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz</pre>
    <p style="margin-top:18px; text-align: center">
      <code>guild.yml</code> located in project root directory
    </p>
  </div>
  <div class="col-lg-3">
    <p>
      The <code>flags</code> section defines hyperparameters. Guild
      uses the default values if not otherwise specified by the
      user. This makes it easy for someone to recreate an experiment
      by simply running <code>guild run</code>.
    </p>
    <p>
      The <code>requires</code> section defines a list of files that
      are needed by the operation. Guild automatically downloads
      required files and makes them available to training script.
    </p>
  </div>
</div>

### Steps to recreate an experiment

<div class="row">
  <div class="col-lg-10">
    <div class="text-editor inline">
      <div class="text-body">
        $ <span class="typed-cursor">guild run</span>
      </div>
    </div>
    <ul class="md features">
      <li>Run command in project root &mdash; i.e. the directory
        containing <code>guild.yml</code> (above)</li>
      <li>Guild downloads the required files and
        runs <code>train.py</code> using the default hyperparameter
        values defined in the Guild file
      </li>
      <li>Training results are automatically captured and available
      for comparison to published results</li>
    </ul>
  </div>
  <div class="col-lg-2">
    Guild uses the information in the Guild file to replicate the
    experiment, keeping things simple for new users.
  </div>
</div>

<a class="btn btn-default btn-promo-next" href="/docs/start/reproducibility/">
  Get started with reproducibility <i class="fa next"></i></a>

---

# Next Steps

<div class="row match-height">
<div class="col col-md-4">
<div class="promo left">
<h3><i class="far fa-arrow-circle-right"></i> Quick Start</h3>
<p class="expand">

It just takes a moment to install Guild and get started with a simple
experiment. From there you can learn about more advanced features.

</p>
<a class="btn btn-primary cta" href="/docs/start/"
  >Get Started <i class="fa next"></i></a>
</div>
</div>

<div class="col col-md-4">
<div class="promo left">
<h3><i class="far fa-compass"></i> Explore the features</h3>
<p class="expand">

Not convinced that Guild is right for you? Spend a few more minutes
browsing its features.

</p>
<a class="btn btn-primary cta" href="/features/"
  >Guild AI features <i class="fa next"></i></a>
</div>
</div>

<div class="col col-md-4">
<div class="promo left">
<h3><i class="far fa-book"></i> Browse Guild AI docs</h3>
<p class="expand">

If you're interested in a complete picture of Guild AI, start by
browsing its comprehensives documentation.

</p>
<a class="btn btn-primary" href="/docs/">Browse the docs <i class="fa next"></i></a>
</div>
</div>
</div>
