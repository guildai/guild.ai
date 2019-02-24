layout: front-page
hide_sidenav: yes
hide_pagenav: yes
hide_in_pagenav: yes

<div class="row match-height top-features">
  <div class="col-md-4 col-sm-6 promo center">
    <h3 style="white-space:nowrap">Track Experiments</h3>
    <p>Automatically track each experiment, capturing model
      performance, logs, and source code</p>
    <img title="200x100"
         class="feature-grid-img"
         style="width:80%"
         src="/assets/img/record-experiments.jpg">
  </div>

  <div class="col-md-4 col-sm-6 promo center">
    <h3 style="white-space:nowrap">Analyze, Compare, Optimize</h3>
    <p>Learn from each experiment to optimize your model in less time
      &mdash; either manually or with AutoML</p>
    <img title="Hyperparameter optimization"
         class="feature-grid-img"
         style="width:80%"
         src="/assets/img/select-experiment.jpg">
  </div>

  <div class="col-md-4 col-sm-6 promo center">
    <h3 style="white-space:nowrap">Run Your Code, Unmodified</h3>
    <p>Use your current training scripts without modification
      &mdash; no need to adopt another framework
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

<div class="row qa" style="margin-top:30px">
  <div class="col-lg-4">
    <h4>Who uses Guild AI?</h4>
  </div>
  <div class="col-lg-8">
    <p>Guild AI is used by machine learning engineers and researchers
      to run, track, and compare experiments. Each experiment yields
      valuable information that is captured and used to inform next
      steps. Scientists and developers leverage their experiment
      results to build deeper intuition, troubleshoot issues, and
      automate model architecture and hyperparameter optimization.</p>
  </div>
</div>

<div class="row qa" style="margin-top:0">
  <div class="col-lg-4">
    <h4>How can Guild AI help me?</h4>
  </div>
  <div class="col-lg-8">
    <p>
      Guild will help you train better models in less time. Effective
      machine learning is a function of systematic
      experimentation&mdash;one experiment leads to another until you
      achieve your goals. The faster and more effective you can apply
      experiments, the sooner you'll complete your work.
    </p>
  </div>
</div>

<div class="row qa" style="margin-top:0">
  <div class="col-lg-4">
    <h4>How is Guild AI different?</h4>
  </div>
  <div class="col-lg-8">
    <p style="margin-bottom:0">Traditional experiment management frameworks require that you
      modify your training scripts to use their APIs for getting
      hyperparameters, logging output, and writing files. Guild
      requires no such changes. It works with your existing scripts as
      an external command line tool, using standard operating systems
      conventions to provide hyperparameters and capture results.</p>
  </div>
</div>

---

# Features

<div class="row match-height other-features">
  <div class="col-lg-4">
    <i class="far fa-box-check"></i>
    <h4>Experiment management</h4>
    <p>Guild is a feature-rich toolkit for running, tracking, and
    comparing experiments. All of the features in this list stem from
    this core functionality.</p>
  </div>
  <div class="col-lg-4">
    <i class="far fa-bullseye-arrow"></i>
    <h4>AutoML</h4>
    <p>Guild makes it easy to optimize hyperparameters&mdash;and even
    model architecture.</p>
  </div>
  <div class="col-lg-4">
    <i class="far fa-route"></i>
    <h4>End-to-end learning</h4>
    <p>
      Curabitur tristique turpis at arcu sollicitudin, et venenatis
      mauris eleifend. Donec porttitor cursus nisl, ut ornare metus
      fringilla at. Nunc sed tempus mi.
    </p>
  </div>
</div>

<div class="row match-height other-features">
  <div class="col-lg-4">
    <i class="far fa-balance-scale"></i>
    <h4>Reproducibility</h4>
    <p>
      Curabitur tristique turpis at arcu sollicitudin, et venenatis
      mauris eleifend. Donec porttitor cursus nisl, ut ornare metus
      fringilla at. Nunc sed tempus mi.
    </p>
  </div>
  <div class="col-lg-4">
    <i class="far fa-analytics"></i>

    <h4>Analytics</h4>
    <p>
      Curabitur tristique turpis at arcu sollicitudin, et venenatis
      mauris eleifend. Donec porttitor cursus nisl, ut ornare metus
      fringilla at. Nunc sed tempus mi.
    </p>
  </div>
  <div class="col-lg-4">
    <i class="far fa-chart-network"></i>
    <h4>Remote training and backups</h4>
    <p>
      Curabitur tristique turpis at arcu sollicitudin, et venenatis
      mauris eleifend. Donec porttitor cursus nisl, ut ornare metus
      fringilla at. Nunc sed tempus mi.
    </p>
  </div>
</div>

---

# Run experiments

### Run your training script, unmodified

<div class="row">
  <div class="col-lg-10">
    <div class="text-editor inline">
      <div class="text-body">
        $ <span class="typed-cursor">guild run train.py learning-rate=0.1</span>
      </div>
    </div>
    <ul class="md features">
      <li>Guild runs your script directly &mdash; no need to change
        anything</li>
      <li>Captures <i>files</i>, <i>metrics</i>, <i>output</i>, and
        <i>logs</i> as a unique experiment</li>
    </ul>
  </div>
</div>

### Run multiple trials for a set of choices (Grid search)

<div class="row">
  <div class="col-lg-10">
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

### Run trials for a range (Random search)

<div class="row">
  <div class="col-lg-10">
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

### Find the best hyperparameters using Bayesian optimization

<div class="row">
  <div class="col-lg-10">
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

---

# Analyze and Compare Results

### Compare experiments

<div class="row">
  <div class="col-lg-10">
    <div class="text-editor inline">
      <div class="text-body">
        $ <span class="typed-cursor">guild compare</span>
      </div>
    </div>
    <div>--screen shot of compare--</div>
  </div>
</div>

### Visualize metrics and generated output

<div class="row">
  <div class="col-lg-8">
    <div class="text-editor inline">
      <div class="text-body">
        $ <span class="typed-cursor">guild view</span>
      </div>
    </div>
    <div>--screen shots of source TensorBoard and Guild View--</div>
  </div>

  <div class="col-lg-4 cmd-highlight-sidebar">
    Curabitur tristique turpis at arcu sollicitudin, et venenatis
    mauris eleifend. Donec porttitor cursus nisl, ut ornare metus
    fringilla at. Nunc sed tempus mi.
  </div>
</div>

### Diff changes across experiments

<div class="row">
  <div class="col-lg-8">
    <div class="text-editor inline">
      <div class="text-body">
        $ <span class="typed-cursor">guild diff</span>
      </div>
    </div>
    <div>--screen shot of source code diff--</div>
  </div>

  <div class="col-lg-4 cmd-highlight-sidebar">
    Curabitur tristique turpis at arcu sollicitudin, et venenatis
    mauris eleifend. Donec porttitor cursus nisl, ut ornare metus
    fringilla at. Nunc sed tempus mi.
  </div>
</div>

---

# Other fun stuff, in Latin?

Curabitur tristique turpis at arcu sollicitudin, et venenatis mauris
eleifend. Donec porttitor cursus nisl, ut ornare metus fringilla
at. Nunc sed tempus mi. Aliquam porttitor mauris sit amet consequat
condimentum. Vestibulum semper ultricies lobortis. Ut hendrerit non
velit quis sagittis. Vestibulum eu mi sapien. In vitae arcu nec justo
dictum convallis. Aliquam erat volutpat. Ut id quam rhoncus, facilisis
libero ut, auctor nibh. Curabitur sagittis euismod congue.

Mauris congue, sem sed posuere imperdiet, massa justo suscipit mi,
quis semper tellus purus in odio. Integer sit amet odio quam. Morbi
suscipit erat nibh. Aliquam vitae augue et lectus gravida lacinia id
in dui. Suspendisse ante erat, molestie a nunc non, condimentum
tristique nibh. Nam at tortor mi. Cras viverra nec ante at lobortis.

Donec nec ante vel leo ornare porttitor. Donec pulvinar, felis et
varius porta, neque neque tempus tortor, vitae tristique eros felis
sed odio. Vestibulum a lacus placerat, pulvinar dui in, tincidunt
risus. Proin tincidunt nisi quis felis consectetur, ultrices efficitur
metus placerat. Interdum et malesuada fames ac ante ipsum primis in
faucibus. Donec non laoreet lectus, vitae pharetra quam. Donec
lobortis efficitur ultricies. Nam euismod, magna id posuere lobortis,
dolor tortor semper dolor, eu sollicitudin quam sapien id
libero. Integer dictum dignissim nisl, sit amet malesuada metus rutrum
non.

Sed leo mauris, laoreet non augue sit amet, malesuada luctus orci. Nam
vitae felis fermentum nulla dictum sodales. Quisque rhoncus dui non
metus blandit placerat. Aenean quis lorem vitae dui commodo
euismod. Aenean eu nunc diam. Aliquam maximus leo ipsum, interdum
vulputate lacus ornare eget. Mauris non nunc id lacus tincidunt
interdum. Vivamus sapien dolor, faucibus vel libero ac, elementum
dapibus erat. Suspendisse odio purus, vulputate et magna vel, ornare
pretium leo. Suspendisse potenti. Vestibulum eros nibh, elementum ac
felis eget, facilisis mollis nisi. Proin tempor ex vitae risus
placerat, ac sagittis sapien eleifend. Fusce vestibulum sapien at
convallis aliquam.
