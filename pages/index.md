layout: front-page
hide_sidenav: yes
hide_pagenav: yes
hide_in_pagenav: yes

<!-- Matomo A/B Test -->
<script type="text/javascript">
    var tagline = document.querySelector("h1");
    var bulletOne = document.querySelector(".tagline-bullets li:first-child");
    var _paq = _paq || [];
    _paq.push(['AbTesting::create', {
        name: '1',
        percentage: 100,
        includedTargets: [{"attribute":"url","inverted":"0","type":"equals_simple","value":"https:\/\/guild.ai\/"}],
        excludedTargets: [],
        startDateTime: '2020/07/19 20:37:01 UTC',
        variations: [
            {
                name: 'original',
                activate: function (event) {
                }
            },
            {
                name: '1',
                activate: function(event) {
                    tagline.innerText = "The easiest way to track experiments";
                    bulletOne.childNodes[1].nodeValue = "Compare & Analyze";
                }
            },
            {
                name: '2',
                activate: function(event) {
                    tagline.innerText = "Open source ML experiment tracking";
                     bulletOne.childNodes[1].nodeValue = "Compare & Analyze";
                }
            },                        {
                name: '3',
                activate: function(event) {
                    tagline.innerText = "Track experiments without changing your code";
                    tagline.setAttribute("style", "max-width:15em");
                    bulletOne.childNodes[1].nodeValue = "Compare & Analyze";
                }
            }
        ],
        trigger: function () {
            return true;
        }
    }]);
</script>
<!-- Matomo A/B Test -->

<div class="row logos">
  <img src="/assets/img/tensorflow-logo.png" width="150">
  <img src="/assets/img/pytorch-logo.png" width="140">
  <img src="/assets/img/keras-logo.png" width="110">
  <img src="/assets/img/scikit-learn-logo.png" width="95">
  <img src="/assets/img/mxnet-logo.png" width="105">
  <img src="/assets/img/xgboost-logo.png" width="105">
</div>

---

<p class="highlight" markdown="1">

Guild AI brings systematic control to machine learning. Build better
models faster. Reduce errors. Guild supports best practices for ML
automation, measurement, and governance. It's freely available under
the Apache 2.0 open source license.

</p>

---

<div class="row other-features display-flex">

  <div class="col-sm-6">
    <img class="feature-icon" src="/assets/icons/folder-check.svg">
    <h4>Track Experiments</h4>
    <p>

      Guild automatically captures every detail of your training runs
      as unique experiments.

    </p>
  </div>

  <div class="col-sm-6">
    <img class="feature-icon" src="/assets/icons/analytics-graph.svg">
    <h4>Compare and Analyze Runs</h4>
    <p>

      Use results to deepen your understanding and incrementally
      improve your models.

    </p>
  </div>

  <div class="col-sm-6">
    <img class="feature-icon" src="/assets/icons/seo-search-star.svg">
    <h4>Tune Hyperparameters</h4>
    <p>

      Find optimal hyperparameters without setting up complicated
      trials.

    </p>
  </div>

  <div class="col-sm-6">
    <img class="feature-icon" src="/assets/icons/hierarchy.svg">
    <h4>Automate Pipelines</h4>
    <p>

      Accelerate model development, eliminate costly errors, and measure results.

    </p>
  </div>

  <div class="col-sm-6">
    <img class="feature-icon" src="/assets/icons/cloud-server.svg">
    <h4>Train and Backup Remotely</h4>
    <p>

      Train on GPU accelerated systems running on any cloud or on-prem
      environment.

    </p>
  </div>

  <div class="col-sm-6">
    <img class="feature-icon" src="/assets/icons/common-file-text-share.svg">
    <h4>Publish and Share Results</h4>
    <p>

      Share your results with colleagues through HTML, Markdown or
      LaTex based reports.

    </p>
  </div>

  <div class="col-sm-6">
    <img class="feature-icon" src="/assets/icons/app-window-code.svg">
    <h4>Command Line Interface</h4>
    <p>

      Use your current console based work flow with Guild's POSIX
      compliant interface.

    </p>
  </div>

  <div class="col-sm-6">
    <img class="feature-icon" src="/assets/icons/file-py.svg">
    <h4>Jupyter Notebook Integration</h4>
    <p>

      Use Notebooks or interactive shells with Guild's Python
      interface.

    </p>
  </div>
</div>

---

<div class="row img-features">

  <div class="col col-sm-6 match-height">
    <h5>Control and Measure</h5>
    <img class="md shadow" src="/assets/img/view-feature.png">
    <p>
      Record each operation, including source code, hyperparameters,
      results, and generated artifacts. Build with confidence having
      full governance and auditability.
    </p>
  </div>

  <div class="col col-sm-6 match-height">
    <h5>Go Beyond Notebooks</h5>
    <img class="md shadow" src="/assets/img/plot-feature.png">
    <p>
      Run your Notebook code with Guild to record summaries over the
      entire life cycle of your models. Know what changed three hours
      ago, or three years!
    </p>
  </div>

  <div class="col col-sm-6 match-height">
    <h5>Tune Hyperparameters</h5>
    <img class="md shadow" src="/assets/img/hparams-2-feature.png">
    <p>
      Apply state-of-the-art tuning algorithms to your models with
      simple commands. Easily optimize with upstream changes to data
      or model architecture.
    </p>
  </div>

  <div class="col col-sm-6 match-height">
    <h5>Compare and Diff</h5>
    <img class="md shadow" src="/assets/img/diff-feature.png">
    <p>
      Identify fine grained differences across runs to resolve complex
      issues and give data scientists the feedback needed to make
      informed decisions.
    </p>
  </div>

  <div class="col col-sm-6 match-height">
    <h5>Automate Tasks</h5>
    <img class="md shadow" src="/assets/img/code-feature.png">
    <p>
      Guild supports a simple configuration scheme that lets you
      define model operations that perform complex tasks with a single
      command.
    </p>
  </div>

  <div class="col col-sm-6 match-height">
    <h5>Follow Engineering Best Practices</h5>
    <img class="md shadow" src="/assets/img/compare-feature-3.png">
    <p>
      Integrate Guild features into any environment without
      reengineering effort. Commands are POSIX compliant and run
      without external dependencies.
    </p>
  </div>

</div>

---

<div class="row promo-qa">
  <div class="col-md-6">
    <h3>What is ML Engineering?</h3>

    <p>
      ML engineering is the application of automated methods to
      machine learning. In the tradition of release management,
      continuous integration, and DevOps, it ensures that machine
      learning efforts are measured, recreatable and
      auditable. Effective ML engineering supports fast development of
      performant models while maintaining the highest levels of
      quality.
    </p>
  </div>

  <div class="col-md-6">
    <h3>Why Guild AI?</h3>

    <p>
      Guild AI is a complete platform for engineers who want to apply
      to machine learning the same control and automation they use in
      other areas. This includes experiment tracking, tools for
      comparison and analysis, hyperparameter tuning, pipeline
      automation, and network operations on any cloud. Guild AI is
      open source, cross platform, and vendor independent.
    </p>
  </div>
</div>

---

<div class="col col-md-12 mt-5">
<div class="promo center">
<a class="btn btn-primary cta" href="https://my.guild.ai/start" target="_blank"><img src="/assets/icons/space-rocket-flying-white.svg" height="24"> Get Started with Guild AI</a>
</div>
</div>
