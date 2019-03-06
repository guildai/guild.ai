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
    <p>Track experiments, capturing every detail including
      performance, generated files, logs, and source code.</p>
    <img title="200x100"
         class="feature-grid-img"
         style="width:80%"
         src="/assets/img/record-experiments.jpg">
  </div>

  <div class="col-md-4 col-sm-12 promo center feature-promo">
    <h3>Analyze, Compare, Optimize</h3>
    <p>Learn from each experiment to optimize your model in less time
      &mdash; apply your own insights or use AutoML.</p>
    <img title="Hyperparameter optimization"
         class="feature-grid-img"
         style="width:80%"
         src="/assets/img/select-experiment.jpg">
  </div>

  <div class="col-md-4 col-sm-12 promo center feature-promo">
    <h3>Get Started Without Changing Your Code</h3>
    <p>Use your current training scripts without modification &mdash;
      there&apos;s no need to adopt another framework.
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
      systematic experimentation&mdash;one experiment leads to another
      as you deepen your understanding. The faster and more effective
      you can apply experiments, the sooner you'll complete your work.
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
    <p style="margin-bottom:0">Traditional experiment management
      frameworks require that you modify your training scripts to use
      their APIs for getting hyperparameters, logging output, and
      writing files. Guild requires no such
      changes&mdash;it <strong>runs your unmodified training
      scripts</strong> as an external command line tool and uses
      standard operating system conventions to specify hyperparameters
      and capture results.</p>
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
    <h4>AutoML</h4>
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
      Hidden with Guild's features is a powerful workflow feature that
      lets you optimize over a series of operations, letting you apply
      AutoML to true end-to-end learning.
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


<div class="promo" style="margin-top:0">
  <a class="btn btn-primary" href="/features/"
     >More information <i class="fa next"></i></a>
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

<div class="promo">
  <a class="btn btn-default" href="/docs/start/"
     >Step-by-step guide <i class="fa next"></i></a>
</div>

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

<div class="promo">
  <a class="btn btn-default" href="/docs/guides/grid-search/"
     >Step-by-step guide <i class="fa next"></i></a>
</div>

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

<div class="promo">
  <a class="btn btn-default" href="/docs/guides/random-search/"
     >Step-by-step guide <i class="fa next"></i></a>
</div>

### Find the best hyperparameters using Bayesian optimization

<div class="row">
  <div class="col-lg-12">
    <div class="text-editor inline">
      <div class="text-body">
        $ <span class="typed-cursor">guild run
        train.py learning-rate=[0.1:0.3] --optimizer bayesian</span>
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

<div class="promo">
  <a class="btn btn-default" href="/docs/guides/bayesian-optimization/"
     >Step-by-step guide <i class="fa next"></i></a>
</div>

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
      <p><img class="md terminal lozad" data-src="/assets/img/compare-list-1.jpg" /></p>
      <figcaption class="under-shadow">Interactive compare application</figcaption>
    </figure>
    <ul class="md features">
      <li>Spreadsheet-like application to compare experiment results</li>
      <li>Flexible display &mdash; customize what you see from the command line</li>
      <li>Mark best results for export or use in other trials</li>
    </ul>
  </div>
</div>

<div class="promo">
  <a class="btn btn-default" href="/docs/guides/compare/"
     >Step-by-step guide <i class="fa next"></i></a>
</div>

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

<div class="promo">
  <a class="btn btn-default" href="/docs/guides/export-runs/"
     >Step-by-step guide <i class="fa next"></i></a>
</div>

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
      <li>Use to answer, <i>&ldquo;What changed beween these two runs
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
    epochs:
      default: 3
      min: 1
      max: 10
    activation:
      default: relu
      choices: [relu, sigmoid]
    num_dense_layers:
      default: 1
      min: 1
      max: 5
    num_dense_nodes:
      default: 16
      min: 5
      max: 512
    learning_rate:
      default: 1e-5
      min: 1e-6
      max: 1e-2
  objective:
      maximize: epoch_val_acc
  requires:
   - url: http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz
   - url: http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz
   - url: http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz
   - url: http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz</pre>
    <p style="margin-top:12px; text-align: center">
      <code>guild.yml</code> located in project root directory
    </p>
  </div>
  <div class="col-lg-3">
    <p>
      The <code>requires</code> section defines a list of files that
      are needed by the operation. Guild automatically downloads the
      files and makes them available to training script. The download
      files are cached and reused without re-downloading.
    </p>
    <p>
      The <code>flags</code> section defines script hyperparameters
      including default values and information used for tuning.
    </p>
    <p>
      The <code>objective</code> section tells Guild what to optimize
      when running tuning operations. In this case, Guild tries to
      maximize validation accuracy.
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
    It's just this simple &mdash; Guild uses the information in the
    Guild file to automate the process.
  </div>
</div>

<div class="promo">
  <a class="btn btn-default" href="/docs/guides/reproducibility/"
     >Step-by-step guide <i class="fa next"></i></a>
</div>

---

# Next Steps

<div class="row match-height">
<div class="col col-md-4">
<div class="promo left">
<h3><i class="far fa-download"></i> Install Guild AI</h3>
<p class="expand">

It just takes a moment to install Guild. From there it's easy to run
and track your experiments &mdash; or apply state-of-the-art Bayesian
optimization.

</p>
<a class="btn btn-primary cta" href="/install/"
  >Install Guild AI <i class="fa next"></i></a>
</div>
</div>

<div class="col col-md-4">
<div class="promo left">
<h3><i class="far fa-compass"></i> Explore the features</h3>
<p class="expand">

Not convinced that Guild is right for you? Spend a few more minutes
browing its features.

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
