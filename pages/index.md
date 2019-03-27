layout: front-page
hide_sidenav: yes
hide_pagenav: yes
hide_in_pagenav: yes

<div id="get-started-fab"></div>

<div class="row match-height top-features">
  <div class="col-md-4 col-sm-12 promo center feature-promo">
    <!--
    <h3></h3>
    -->
    <h3>Track Experiments Automatically</h3>
    <p>
      Track experiments, capturing every detail including
      performance, generated files, logs, and source code.
    </p>
    <img title="200x100"
         class="feature-grid-img"
         style="width:80%"
         src="/assets/img/record-experiments.jpg">
  </div>

  <div class="col-md-4 col-sm-12 promo center feature-promo">
    <h3>Analyze, Compare, Optimize</h3>
    <p>
      Learn from each experiment to optimize your model in less time
      &mdash; apply your own insights or use Auto ML.
    </p>
    <img title="Hyperparameter optimization"
         class="feature-grid-img"
         style="width:80%"
         src="/assets/img/select-experiment.jpg">
  </div>

  <div class="col-md-4 col-sm-12 promo center feature-promo">
    <h3>Get Started Fast &mdash; No Code Changes</h3>
    <p>
      Use your current training scripts without modification &mdash;
      there&apos;s no need to adopt another framework or library.
    </p>
    <img title="Use your code without modification"
         class="feature-grid-img"
         style="width:80%"
         src="/assets/img/own-code-sm.jpg">
  </div>
</div>

---

<div class="row match-height logos">
  <img src="/assets/img/tensorflow-logo.png" width="150">
  <img src="/assets/img/pytorch-logo.png" width="140">
  <img src="/assets/img/keras-logo.png" width="110">
  <img src="/assets/img/scikit-learn-logo.png" width="95">
  <img src="/assets/img/mxnet-logo.png" width="105">
  <img src="/assets/img/xgboost-logo.png" width="105">
</div>

---

<div class="row qa">
  <div class="col-lg-4">
    <h4>How does Guild AI help?</h4>
  </div>
  <div class="col-lg-8">
    <p>
      Guild helps you <strong>train better models in less
      time</strong>. Effective machine learning is a function of
      systematic experimentation &mdash; one experiment leads to
      another as you deepen your understanding. The faster and more
      effective you can apply experiments, the sooner you'll complete
      your work.
    </p>
  </div>
</div>

<div class="row qa">
  <div class="col-lg-4">
    <h4>Who uses Guild AI?</h4>
  </div>
  <div class="col-lg-8">
    <p>Guild AI is used by <strong>machine learning engineers and
      researchers</strong> to run, track, and compare
      experiments. Each experiment yields valuable information that is
      captured and used to inform next steps. Scientists and
      developers leverage their experiment results to build deeper
      intuition, troubleshoot issues, and automate model architecture
      and hyperparameter optimization.</p>
  </div>
</div>

<div class="row qa">
  <div class="col-lg-4">
    <h4>How is Guild AI different?</h4>
  </div>
  <div class="col-lg-8">
    <p style="margin-bottom:0">
      Guild is <strong>cross platform and framework
      independent</strong> &mdash; you can train and capture
      experiments in literally any language using any library. Guild
      runs your unmodified code, which means you get to use the
      libraries you want. Guild doesn't require databases or other
      infrastructure to management experiments &mdash; it's simple and
      easy to use. This frees you to focus on what's
      important: <em>building state-of-the-art models and machine
      learning apps</em>.
    </p>
  </div>
</div>

---

# Features

<div class="row match-height other-features">
  <div class="col-lg-4">
    <i class="far fa-box-check"></i>
    <h4>Experiment management</h4>
    <p>
      When you run your training scripts with Guild, you get
      experiment management automatically. Use the results to make
      informed decisions about your models.
    </p>
  </div>
  <div class="col-lg-4">
    <i class="far fa-bullseye-arrow"></i>
    <h4>Auto ML</h4>
    <p>
      Guild makes it easy to optimize hyperparameters and model
      architecture. With a single command, you can apply
      state-of-the-art algorithms to your training scripts.
    </p>
  </div>
  <div class="col-lg-4">
    <i class="far fa-balance-scale"></i>
    <h4>Reproducibility</h4>
    <p>
      Guild makes it easy to recreate your experiments. By
      systematically running your scripts and capturing their output,
      Guild lets others run and compare results.
    </p>
  </div>
</div>

<div class="row match-height other-features">
  <div class="col-lg-4">
    <i class="far fa-analytics"></i>
    <h4>Analytics</h4>
    <p>
      Guild provides a suite of visualization, comparison, and diffing
      tools for studying and comparing your experiment results.
    </p>
  </div>
  <div class="col-lg-4">
    <i class="far fa-route"></i>
    <h4>End-to-end learning</h4>
    <p>
      Guild has a powerful workflow feature that lets you optimize
      over a series of operations, letting you apply Auto ML to true
      end-to-end learning.
    </p>
  </div>
  <div class="col-lg-4">
    <i class="far fa-chart-network"></i>
    <h4>Remote training and backups</h4>
    <p>
      Guild lets you train remotely &mdash; e.g. on powerful GPU
      servers &mdash; as well as backup and restore your runs.
    </p>
  </div>
</div>

<div class="promo">
  <a class="btn btn-primary" href="/features/">More about features <i class="fa next"></i></a>
</div>
---

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

    <div class="text-editor inline" style="width:590px">
      <div class="text-body">
        $ <span class="typed-cursor">guild help</span>
      </div>
    </div>

    <p>&nbsp;</p>
    <p>&ldquo; &rdquo;&rsquo;</p>
    <p>&nbsp;</p>

    <!--

    <div class="text-editor inline" style="width:670px">
      <div class="text-body">
        $ <span class="typed-cursor">guild run key-findings</span>
      </div>
    </div>


    <div class="text-editor inline" style="width:670px">
      <div class="text-body">
        $ <span class="typed-cursor">guild push arya-experiments-on-s3</span>
      </div>
    </div>



    <div class="text-editor inline" style="width:670px">
      <div class="text-body">
        $ <span class="typed-cursor">guild run train.py dropout=uniform[0.0:0.9] --optimizer bayesian</span>
      </div>
    </div>

    <div class="text-editor inline">
      <div class="text-body">
        $ <span class="typed-cursor">guild pull arya-experiments-on-s3</span>
      </div>
    </div>

    <pre class="language-yaml gf-sample" style="width:560px">key-findings:
  description: Key findings for dropout between 0.8 and 0.95
  steps:
    - run: train.py dropout=0.8
    - run: train.py dropout=0.9
    - run: train.py dropout=0.95</pre>

    -->

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
