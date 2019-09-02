layout: front-page
hide_sidenav: yes
hide_pagenav: yes
hide_in_pagenav: yes
title: Tools for Machine Learning Automation

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

Guild AI is a software toolkit used by machine learning engineers to
build better models in less time. It automates experiments and
supports detailed analysis and comparison of results. Guild AI is free
software, available under the Apache 2 open source license.

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
    <h2><strong>Add Structure</strong> - Use a Guild file for more control</h2>

    <p>

      Add <code>guild.yml</code> to your project to <strong>make
      things explicit</strong> and to keep experiment
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

  </div>
</div>

<div class="row feature">
  <div class="hidden-xs col-sm-2">
    <img class="icon" src="/assets/icons/charging-flash-sync-1.svg">
  </div>
  <div class="col-sm-10">
    <h2><strong>Experiment</strong> - Run trials quickly and easily</h2>

    <p>

      Guild supports single trials, <strong>grid
      search</strong>, <strong>random search</strong>,
      and <strong>Baysian optimization</strong> through an elegant
      command line interface.

    </p>

    <div class="text-editor">
      <div class="text-body">
        $ <span id="typed-run2"></span><span class="typed-cursor">|</span>
      </div>
    </div>
  </div>
</div>

<div class="row feature">
  <div class="hidden-xs col-sm-2">
    <img class="icon" src="/assets/icons/seo-search-graph-1.svg">
  </div>
  <div class="col-sm-10">
    <h2><strong>Learn and Improve</strong> - Build understanding from
    the data</h2>

    <p>

      Guild comes with a tour de force of <strong>analytic
      tools</strong> that help you <strong>study results</strong> and
      <strong>inform your next steps</strong>.

    </p>

    <div class="text-editor">
      <div class="text-body">
        $ <span id="typed-view-and-compare"></span><span class="typed-cursor">|</span>
      </div>
    </div>

    <div class="view-and-compare-preview">
      <div id="view-and-compare-img-compare" class="show-hide">
        <img class="md shadow" src="/assets/img/compare-feature.png">
        <p>
          Compare results at the command line.
        </p>
      </div>
      <div id="view-and-compare-img-tensorboard" class="show-hide">
        <img class="md shadow" src="/assets/img/tensorboard-feature.png">
        <p>
          Built-in TensorBoard support.
        </p>
      </div>
      <div id="view-and-compare-img-view" class="show-hide">
        <img class="md shadow" src="/assets/img/view-feature.png">
        <p>
          View and compare results graphically.
        </p>
      </div>
      <div id="view-and-compare-img-diff" class="show-hide">
        <img class="md shadow" src="/assets/img/diff-feature.png">
        <p>
          View fine-grain differences between two runs.
        </p>
      </div>
      <div id="view-and-compare-img-open" class="show-hide">
        <img class="md shadow" src="/assets/img/open-feature.png">
        <p>
          Browse and open run files.
        </p>
      </div>
    </div>
  </div>
</div>

---

# Learn More

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
