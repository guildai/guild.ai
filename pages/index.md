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
    <h3 style="white-space:nowrap">Easy to Get Started</h3>
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

- Generate Experiments
- Optimize Model Architecture and Hyperparameters
- Learn End-to-End
- Troubleshoot Training Issues
- Backup and Share Results
- Train Locally or Remotely
- Supports All Machine Learning Platforms

---

# Run experiments

### Run a single trial using your unmodified training script

<div class="row">
  <div class="col-lg-8">
    <div class="text-editor inline">
      <div class="text-body">
        $ <span class="typed-cursor">guild run train.py learning-rate=0.1</span>
      </div>
    </div>
  </div>

  <div class="col-lg-4 cmd-highlight-sidebar">
    Simply run your training scripts with Guild to automatically
    capture output, tracking each result in a repository of
    experiments.
  </div>
</div>

### Run trials over a set of choices (grid search)

<div class="row">
  <div class="col-lg-8">
    <div class="text-editor inline">
      <div class="text-body">
        $ <span class="typed-cursor">guild run train.py learning-rate=[0.1,0.2,0.3]</span>
      </div>
    </div>
  </div>

  <div class="col-lg-4 cmd-highlight-sidebar">
    Run multiple experiments with one command by specifying a list of
    hyperparameter values. Guild performs a grid search over the
    Cartesian product of specified values.
  </div>
</div>

### Run trials over a range of values (random search)

<div class="row">
  <div class="col-lg-8">
    <div class="text-editor inline">
      <div class="text-body">
        $ <span class="typed-cursor">guild run
        train.py learning-rate=[0.1:0.3] --max-trials 10</span>
      </div>
    </div>
  </div>

  <div class="col-lg-4 cmd-highlight-sidebar">
    Performa a random search over a specified range for a number of
    trials. Random search is a surprisingly effective way of finding
    optimal hyperparameters if you run enough experiments.
  </div>
</div>

### Find the best values over a range (Bayesian optimization)

<div class="row">
  <div class="col-lg-8">
    <div class="text-editor inline">
      <div class="text-body">
        $ <span class="typed-cursor">guild run
        train.py learning-rate=[0.1:0.3] --optimizer bayesian</span>
      </div>
    </div>
  </div>

  <div class="col-lg-4 cmd-highlight-sidebar">
    For an intractably large search space or very long training times
    (e.g. deep neural networks) Bayesian optimization is a remarkably
    efficient way to find optimal hyperparameters.
  </div>
</div>

---

# Analyze and Compare Results

<div class="row">
  <div class="col-lg-8">
    <div class="text-editor inline">
      <div class="text-body">
        $ <span class="typed-cursor">guild compare</span>
      </div>
    </div>
    <div>--screen shot of compare--</div>
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
