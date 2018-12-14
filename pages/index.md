layout: banner
banner_action: Learn more
banner_action_link: #learn-more
hide_sidenav: yes
hide_pagenav: yes
hide_in_pagenav: yes

<div id="learn-more" style="height:50px;margin-top:-50px"></div>

<div class="row match-height">
  <div class="col-md-4 col-sm-6 promo center">
    <h4><a href="/docs/intro/#projects">TensorFlow projects</a></h4>
    <p>

      Add <code>guild.yml</code> to your TensorFlow or Keras project to
      automate tasks and enable experiment tracking,
      testing, distribution and remote training.

      <a class="red-link" href="/docs/intro/#guild-projects">Learn more</a>.

    </p>
    <a href="/docs/intro/#guild-projects">
      <img title="guild.yml added to TensorFlow project"
           class="feature-grid-img" src="/assets/img/guild-project.png">
    </a>
  </div>

  <div class="col-md-4 col-sm-6 promo center">
    <h4><a href="/docs/intro/#model-operations">Model operations</a></h4>
    <p>

      Train your model by running the command <code class="lit">guild
      run train</code> to generate a unique experiment that preserves
      training files and metadata.

      <a class="red-link" href="/docs/intro/#model-operations">Learn more</a>.

    </p>
    <a href="/docs/intro/#model-operations">
      <img title="Running the train operation"
           class="feature-grid-image" style="margin-top:5px;max-width:100%"
           src="/assets/img/guild-run.png">
    </a>
  </div>

  <div class="col-md-4 col-sm-6 promo center">
    <h4><a href="/docs/intro/#experiments">Experiments</a></h4>
    <p>

      Capture results as unique experiments by running
      operations&mdash;compare performance, diff changes, visualize
      with TensorBoard and backup to the cloud.

      <a class="red-link" href="/docs/intro/#experiments">Learn more</a>.

    </p>
    <a href="/docs/intro/#experiments">
      <img title="Each run tracked as an experiment"
           class="feature-grid-img" src="/assets/img/experiments.png">
    </a>
  </div>

  <div class="col-md-4 col-sm-6 promo center">
    <h4><a href="/docs/intro/#end-to-end-workflow">End-to-end workflow</a></h4>
    <p>

      Automate your model life cycle from data collection and
      pre-processing to training and evaluation to optimization and
      deployment.

      <a class="red-link" href="/docs/intro/#end-to-end-workflow">Learn more</a>.

    </p>
    <a href="/docs/intro/#end-to-end-workflow">
      <img title="Operations used for end-to-end workflow"
           class="feature-grid-img" src="/assets/img/workflow.png">
    </a>
  </div>

  <div class="col-md-4 col-sm-6 promo center">
    <h4><a href="/docs/intro/#model-tests">Automate testing</a></h4>
    <p>

      Verify all stages of your model workflow with tests that
      exercise code and check results such as expected loss and
      accuracy ranges.

      <a class="red-link" href="/docs/intro/#model-tests">Learn more</a>.

    </p>
    <a href="/docs/intro/#model-tests">
      <img title="Guild file containing model tests"
           class="feature-grid-img code" style="margin-top:5px"
           src="/assets/img/tests.png">
    </a>
  </div>

  <div class="col-md-4 col-sm-6 promo center">
    <h4><a href="/docs/intro/#packages">Packages</a></h4>
    <p>

      Save time and reduce errors by reusing tested, proven models and
      operations&mdash;developed by you and others in the TensorFlow
      community.

      <a class="red-link" href="/docs/intro/#packages">Learn more</a>.

    </p>
    <a href="/docs/intro/#packages">
      <img title="Guild project reusing code from TensorFlow, PyPI and GitHub"
           class="feature-grid-img" src="/assets/img/reuse.png">
    </a>
  </div>
</div>

<div class="row">
  <div class="col-xs-12 text-center">
    <a class="btn btn-primary btn-lg" href="/docs/intro/">Guild AI introduction <i class="fa next"></i></a>
  </div>
</div>

---

# More features

<div class="row feature">
  <div class="img img-smaller col hidden-xs col-sm-2">
    <img title="Amazon EC2" src="/assets/img/ec2.png">
  </div>
  <div class="body col col-xs-12 col-sm-10">
    <h3><a href="/docs/guides/train-on-ec2/">Train remotely on Amazon EC2</a></h3>
    <p>

      Guild supports remote training on EC2, including setup and tear
      down of EC2 infrastructure. If your local compute resources
      aren't enough for a training operation, start an EC2 remote and
      run your operation there.

      <p>
        <a class="red-link" href="/docs/guides/train-on-ec2/">Learn more</a>
      </p>

    </p>
  </div>
</div>

<div class="row feature">
  <div class="img img-smaller col hidden-xs col-sm-2">
    <img title="Amazon S3" src="/assets/img/s3.png">
  </div>
  <div class="body col col-xs-12 col-sm-10">
    <h3><a href="/docs/guides/backup-to-s3/">Backup runs to S3</a></h3>
    <p>

      Backup runs on S3 for safe keeping with Guild. All of Guild's
      run management commands are supported for S3, including list,
      delete, restore, and label.

    </p>

      <p>
        <a class="red-link" href="/docs/guides/backup-to-s3/">Learn more</a>
      </p>
  </div>
</div>

<div class="row feature">
  <div class="img img-bigger col hidden-xs col-sm-2">
    <img title="TensorBoard" src="/assets/img/tb-feature.png">
  </div>
  <div class="body col col-xs-12 col-sm-10">
    <h3><a href="/docs/visual/tensorboard/">Visualize runs with TensorBoard</a></h3>
    <p>

      TensorBoard is a powerful visualization tool for TensorFlow. Use
      Guild to start TensorBoard to view runs with a single
      command. Guild automatically synchronizes TensorBoard with your
      current set of runs---you only need to start TensorBoard once.

    </p>

      <p>
        <a class="red-link" href="/docs/visual/tensorboard/">Learn more</a>
      </p>
  </div>
</div>

<div class="row feature">
  <div class="img img-smaller col hidden-xs col-sm-2">
    <img title="Compare runs" src="/assets/img/compare-feature.png">
  </div>
  <div class="body col col-xs-12 col-sm-10">
    <h3><a href="/docs/guides/compare-runs/">Compare run performance and diff changes</a></h3>
    <p>

      As you run operations, Guild automatically captures run logs and
      files so you can study and compare them. Guild seamlessly
      indexes TensorFlow event logs to capture training and evaluation
      metrics, letting you quickly view model performance across runs.

    </p>

      <p>
        <a class="red-link" href="/docs/guides/compare-runs/">Learn more</a>
      </p>
  </div>
</div>

<div class="row feature">
  <div class="img col hidden-xs col-sm-2">
    <img title="PyPI" src="/assets/img/pypi-feature.jpg">
  </div>
  <div class="body col col-xs-12 col-sm-10">
    <h3><a href="/docs/packages/">Publish packaged models to PyPI</a></h3>
    <p>

      To share your models with other developers, Guild lets you
      quickly generate Python packages and upload them to PyPI. Users
      install your models using pip, Conda, or Guild.

    </p>

      <p>
        <a class="red-link" href="/docs/guides/publish-to-pypi/">Learn more</a>
      </p>
  </div>
</div>

---

# Get started

<div class="row match-height" style="margin-bottom:40px">

  <div class="col col-md-6">
    <div class="promo left">
      <h3><a href="/docs/intro/">Guild AI introduction</a></h3>
      <p class="expand">

        If you're new to Guild AI, this introduction covers core
        features and functionality. Start here to learn about
        projects, models and operations, runs, end-to-end workflow,
        automated testing and packaging.

      </p>
      <a class="btn btn-primary cta" href="/docs/intro/"
         >Guild AI introduction <i class="fa next"></i></a>
    </div>
  </div>

  <div class="col col-md-6">
    <div class="promo left">
      <h3><a href="/docs/guides/create-a-project/">Add Guild to your project</a></h3>
      <p class="expand">

        If you have scripts that train your TensorFlow or Keras
        models, add a Guild file (i.e. a file
        named <code>guild.yml</code>) to your project to enable Guild
        features.

      </p>
      <a class="btn btn-primary" href="/docs/guides/add-guild/">Add Guild to your project <i class="fa next"></i></a>
    </div>
  </div>

  <!--
  <div class="col col-md-6">
    <div class="promo left">
      <h3><a href="/docs/guides/guild-for-research/">Guild for research</a></h3>
      <p class="expand">

        As an experiment management toolkit, Guild is tailor made for
        researchers. This guide provides step-by-step instructions
        using Guild in your research.

      </p>
      <a class="btn btn-primary" href="/docs/guides/guild-for-research/">Guild for research <i class="fa next"></i></a>
    </div>
  </div>
  -->

  <div class="col col-md-6">
    <div class="promo left">
      <h3><a href="/docs/guides/create-image-classifier/">Create an image classifier</a></h3>
      <p class="expand">

        Guild supports a variety of feature-rich packages and project
        templates. This guide steps you through the process of
        creating an image classifier.

      </p>
      <a class="btn btn-primary" href="/docs/guides/create-image-classifier/">Create an image classifier <i class="fa next"></i></a>
    </div>
  </div>

  <div class="col col-md-6">
    <div class="promo left">
      <h3><a href="/docs/">Browse Guild AI documentation</a></h3>
      <p class="expand">

        If you're interested in a complete picture of Guild AI, start by
        browsing its comprehensives documentation.

      </p>
      <a class="btn btn-primary" href="/docs/">Browse documentation <i class="fa next"></i></a>
    </div>
  </div>
</div>
