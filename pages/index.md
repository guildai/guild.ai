layout: banner
banner_tagline:
    Discover and apply state-of-the-art TensorFlow models
banner_subtext:
    <strong>Guild AI</strong> is a developer toolkit that
    accelerates deep learning model development and reuse.
banner_action: Learn more
banner_action_link: #learn-more
hide_sidenav: yes
hide_pagenav: yes
hide_in_pagenav: yes
attribution:
    Shipping icon by
    <a href="https://www.freepik.com/free-vector/logistic-icons-set-flat_1530842.htm"
    target="_blank">Freepik</a>

<div id="learn-more" style="height:50px;margin-top:-50px"></div>

# Guild AI <small>&nbsp;streamline your TensorFlow and Keras development</small>

Guild AI automates TensorFlow and Keras deep learning workflow,
letting you focus on optimizing your models and getting them into
production as quickly as possible. The command line toolset, supports
your deep learning work end-to-end --- from model acquisition, through
training and testing, to deployment. You can even publish your models
for your collaborators to use!

<div class="row match-height">
  <div class="col-md-4 col-sm-6 promo center">
    <h4>Track</h4>
    <p>
      Automatically save each training run for later comparison or
      deployment.
    </p>
    <a href="/assets/img/guild-view-track.png" data-featherlight="image">
      <img alt="Track experiments" class="feature-grid-img"
           src="/assets/img/guild-view-track-zoom.png">
    </a>
  </div>

  <div class="col-md-4 col-sm-6 promo center">
    <h4>Compare</h4>
    <p>
      Compare accuracy, loss, architecture, steps, and
      hyperparameters.
    </p>
    <a href="/assets/img/guild-compare.png" data-featherlight="image">
      <img alt="Compare runs" class="feature-grid-img"
           src="/assets/img/guild-compare-zoom.png">
    </a>
  </div>

  <div class="col-md-4 col-sm-6 promo center">
    <h4>Deploy</h4>
    <p>
      Deploy your models to Cloud ML or serve them locally as a REST
      API.
    </p>
    <a href="/assets/img/cloud-ml.png" data-featherlight="image">
      <img alt="Deploy to Cloud ML" class="feature-grid-img"
           src="/assets/img/cloud-ml-zoom.png">
    </a>
  </div>

  <div class="col-md-4 col-sm-6 promo center">
    <h4>Visualize</h4>
    <p>
      Visualize metrics with TensorBoard and content with Guild View.
    </p>
    <a href="/assets/img/tb.png" data-featherlight="image">
      <img alt="TensorBoard" class="feature-grid-img"
           style="max-height:180px" src="/assets/img/tb-zoom.png">
    </a>
  </div>

  <div class="col-md-4 col-sm-6 promo center">
    <h4>Package</h4>
    <p>
      Package and distribute your models for others to use and learn
      from.
    </p>
    <img alt="Package models" class="feature-grid-img no-lightbox" style="height:150px"
         src="/assets/img/ship.svg">
  </div>

  <div class="col-md-4 col-sm-6 promo center">
    <h4>Discover</h4>
    <p>
      Explore state-of-the-art models in Guild AI&apos;s ever-growing
      ecosystem.
    </p>
    <a href="/models">
      <img alt="Platform support" class="feature-grid-img no-lightbox" style=""
           src="/assets/img/platform.png">
    </a>
  </div>

</div>

---

# Quick start

<div class="row quick-start">
  <div class="col-md-8">
    <h3>Step 1. Install Guild AI</h3>
    <p>Guild AI is installed
    using <a href="https://pip.pypa.io/en/stable/" target="_blank"
    class="ext">pip</a>. Select one of the installation methods below.
    </p>
    <div class="tabs tabs-text">
      <ul class="nav nav-tabs" role="tablist">
        <li role="presentation" class="active">
          <a href="#pip" role="tab" data-toggle="tab">Native pip</a>
        </li>
        <li role="presentation">
          <a href="#virtual-env" role="tab" data-toggle="tab">Virtual env</a>
        </li>
        <li role="presentation">
          <a href="#conda" role="tab" data-toggle="tab">Conda</a>
        </li>
      </ul>
      <div class="tab-content" style="padding-bottom:0">
        <div role="tabpanel" class="tab-pane active fade in" id="pip">
          <p>Install Guild AI using pip by running:</p>
          <pre>
            <code class="language-command">pip install guildai</code>
          </pre>
          <div class="admonition note">
            <p class="admonition-title">Note</p>
            <p>If you are unable to install Guild AI due to permission
              errors, you may need to run the command
              using <code>sudo</code>:
            </p>
            <pre>
              <code class="language-command">sudo pip install guildai</code>
            </pre>
          </div>
        </div>
        <div role="tabpanel" class="tab-pane fade" id="virtual-env">
          <p>Install Guild AI in a virtual environment
          named <code>guild</code> by running:</p>
          <pre>
            <code class="language-command">
              virtualenv guild
              . guild/bin/activate
              pip install guildai
            </code>
          </pre>
          <p>To install in a different virtual env,
          replace <code class="lit">guild</code> above with the
          alternate location.</p>
        </div>
        <div role="tabpanel" class="tab-pane fade" id="conda">
          <p>Install Guild AI in a Conda environment
          named <code>guild</code> by running:</p>
          <pre>
            <code class="language-command">
              conda create -n guild python=3.6
              source activate guild
              pip install guildai
            </code>
          </pre>
          <p>To install in a different virtual env,
          replace <code class="lit">guild</code> above with the
          alternate location.</p>
        </div>
      </div>
    </div>
    <p>For more information, see <a href="/install"
      target="_blank">Installing Guild AI</a>.
    </p>
    <p>Once Guild AI is installed, initialize the Guild environment by
    running:</p>
    <pre>
      <code class="language-command">guild init --env</code>
    </pre>
    <p>
      This step will verify that your environment is setup correctly
      and prompt you to install TensorFlow if it isn't already
      installed. Answer yes if prompted to install the TensorFlow
      package for your system.
    </p>
    <p>
      If you encounter errors at this stage,
      see <a href="/troubleshooting">Troubleshooting</a> for more
      information or <a href="https://github.com/guildai/guild/issues"
      target="_blank" class="ext">open an issue on GitHub</a> to get
      help.
    </p>
  </div>
  <div class="col-md-4 hidden-xs hidden-sm console-col">
    <img alt="Install Guild AI" class="quick-start-img no-lightbox"
         src="/assets/img/install.gif">
    <div class="img-caption">Installing Guild AI</div>
  </div>

  <div class="col-md-8">
    <h3>Step 2. Find and install models</h3>
    <p>Guild AI lets you find and install models in seconds. Search
    for <code class="lit">mnist</code> by running:</p>
    <pre>
      <code class="language-command">guild search mnist</code>
    </pre>
    <p>For this quick start, we'll work with the
    base <code>mnist</code> package. Install it by running:</p>
    <pre>
      <code class="language-command">guild install mnist</code>
    </pre>
    <p>List the models you installed by running:</p>
    <pre>
      <code class="language-command">guild models</code>
    </pre>
  </div>
  <div class="col-md-4 hidden-xs hidden-sm console-col">
    <img alt="Search for models" class="quick-start-img no-lightbox"
         src="/assets/img/search.gif">
    <div class="img-caption">Finding and installing models</div>
  </div>

  <div class="col-md-8">
    <h3>Step 3. Train the models</h3>
    <p>In this step we'll train <code>mnist-softmax</code>
      and <code>mnist-cnn</code>.
    </p>
    <p>First, train the softmax version by running:</p>
    <pre>
      <code class="language-command">guild train mnist-softmax</code>
    </pre>
    <p>
      Review the default values and
      press <code>ENTER</code>. The <code>mnist-softmax</code> model
      trains quickly even on systems that don't have a GPU.
    </p>
    <p>
      Next we'll train the CNN. Choose a method based on your system
      type.
    </p>
    <div class="tabs tabs-text">
      <ul class="nav nav-tabs" role="tablist">
        <li role="presentation" class="active">
          <a href="#gpu" role="tab" data-toggle="tab">GPU-accelerated</a>
        </li>
        <li role="presentation">
          <a href="#cpu" role="tab" data-toggle="tab">CPU only</a>
        </li>
      </ul>
      <div class="tab-content">
        <div role="tabpanel" class="tab-pane active fade in" id="gpu">
          <p>Most GPU accelerated systems will train the CNN model in
          a minute or two. If your system system has a GPU,
          train <code>mnist-cnn</code> for the default number of
          epochs by running:</p>
          <pre>
            <code class="language-command">guild train mnist-cnn</code>
          </pre>
        </div>
        <div role="tabpanel" class="tab-pane fade" id="cpu">
          <p>If you system doesn't have a GPU,
          the <code>mnist-cnn</code> model will train slowly. You can
          complete this step faster by training fewer epochs. Train
          for one epoch by running:</p>
          <pre>
            <code class="language-command">guild train mnist-cnn epochs=1</code>
          </pre>
        </div>
      </div>
    </div>
    <p>When both models are trained, view the list of runs by running:</p>
    <pre>
      <code class="language-command">guild runs</code>
    </pre>
  </div>
  <div class="col-md-4 hidden-xs hidden-sm console-col">
    <img alt="Train models" class="quick-start-img no-lightbox console"
         src="/assets/img/train.gif">
    <div class="img-caption">Training MNIST</div>
  </div>

  <div class="col-md-8">
    <h3>Step 4. Compare model performance</h3>
    <p>
      In this step we'll view the training
      results. <a href="/docs/commands/#running-commands-in-a-separate-console">Open
      a separate command line console</a> and run:
    </p>
    <pre>
      <code class="language-command">guild view</code>
    </pre>
    <p>
      <a href="/docs/visual/guild-view/">Guild View</a> is a visual
      application that lets you explore runs, compare model
      performance, and view generated files. Guild View will open
      automatically in your browser when run the command.
    </p>
    <p class="indent">
      <a href="/assets/img/guild-view-1.png" data-featherlight="image">
        <img alt="Guild View" class="screen"
             src="/assets/img/guild-view-zoom-2.png">
      </a>
    </p>
    <h4>Step 4.1. Compare runs in Guild View</h4>
    <p>
      In your browser, click <img alt="Compare runs"
      src="/assets/img/compare-runs.png" class="screen"> in the left
      sidebar. This will display a table containing the results of
      your two runs.
    </p>
    <p class="indent">
      <a href="/assets/img/guild-view-compare.png" data-featherlight="image">
        <img alt="Compare runs table" class="screen"
             src="/assets/img/guild-view-compare-table.png">
      </a>
    </p>
    <p>
      Use this view to select the run with the best performance. In
      this case, it's the CNN!
    </p>
    <h4>Step 4.2. Compare runs in TensorBoard</h4>
    <p>
      In your browser, click <img alt="View in TensorBoard"
      class="screen" src="/assets/img/view-in-tensorboard.png"> in the
      left sidebar. This will open another tab running TensorBoard,
      which will let you view detailed training data. Use the tabs at
      the top of TensorBoard to view different types of data.
    </p>
    <p class="indent">
      <a href="/assets/img/tb.png" data-featherlight="image">
        <img alt="TensorBoard" class="screen"
             src="/assets/img/tb-zoom-2.png">
      </a>
    </p>
  </div>
  <div class="col-md-4 hidden-xs hidden-sm img-col">
    <a href="/assets/img/guild-view-1.png" data-featherlight="image">
      <img alt="Guild View" class="feature-img screen"
           src="/assets/img/guild-view-1-zoom.png">
    </a>
    <div class="img-caption">Results in Guild View</div>
  </div>

  <div class="col-md-8">
    <h3>Step 5. Serve locally</h3>
    <p>
      In the previous step, we saw that the CNN model performs much
      better than the softmax! Let's serve that model locally as a
      REST prediction API.
    </p>
    <p>In
    a <a href="/docs/commands/#running-commands-in-a-separate-console">new
    command line console</a>, serve the CNN model by running:</p>
    <pre>
      <code class="language-command">guild serve -o mnist-cnn --host localhost --port 8083</code>
    </pre>
    <p>
      This command opens a new browser window for Guild Serve, which
      describes the REST endpoint for the trained MNIST CNN model. You
      can build your application and test locally before deploying to
      a production environment.
    </p>
  </div>
  <div class="col-md-4">
    <a href="/assets/img/guild-serve-1.png" data-featherlight="image">
      <img alt="Guild Serve" class="feature-img screen"
           src="/assets/img/guild-serve-1-zoom.png">
    </a>
    <div class="img-caption">Guild Serve</div>
  </div>

  <div class="col-md-8">
    <h3>Step 6. Deploy to Cloud ML</h3>
    <div class="admonition note">
      <p class="admonition-title">Note</p>
      <p>
        This step requires a Google Cloud Machine Learning Engine
        account. To setup your account and environment, follow the
        steps
        in <a href="https://cloud.google.com/ml-engine/docs/getting-started-training-prediction"
        target="_blank" class="ext">Cloud ML Engine - Getting
        Started</a>
      </p>
    </div>
    <p>
      When you're ready to run your prediction service in production, you can
      by running:
    </p>
    <pre>
      <code class="language-command">guild run mnist-cnn:cloudml-deploy bucket=$BUCKET_NAME</code>
    </pre>
    <p>
      <code class="lit">$BUCKET_NAME</code> should refer to a Google
      Cloud Storage bucket that you have write permission to.
    </p>
    <p>
      For a deep dive into Guild AI's Cloud ML support,
      see <a href="/docs/tutorials/train-and-predict-with-cloudml/">Train
      and predict with Cloud ML</a>.
    </p>
  </div>
  <div class="col-md-4">
    <img alt="Guild View" class="feature-img"
         style="max-width:260px"
         src="/assets/img/google-cloud-ml.png">
  </div>

</div>

---

# Next steps

<div class="row match-height" style="margin-bottom:40px">

<div class="col col-md-4">
<div class="promo left">
<h3>Go deeper with Guild AI</h3>
<p class="expand">

Go deeper into the Quick Start material above with a step-by-step
tutorial on training and deploying with Guild AI and Cloud ML.

</p>
<a class="btn btn-primary cta" href="/docs/tutorials/train-and-predict-with-cloudml/"
  >Go deeper with Guild AI <i class="fa next"></i></a>
</div>
</div>

<div class="col col-md-4">
<div class="promo left">
<h3>Explore models</h3>
<p class="expand">

Guild AI supports an ever-growing ecosystem of TensorFlow and Keras
models that you can install and train with a few simple commands.

</p>
<a class="btn btn-primary cta" href="/models/"
  >Discover the models <i class="fa next"></i></a>
</div>
</div>

<div class="col col-md-4">
<div class="promo left">
<h3>Browse the docs</h3>
<p class="expand">

If you're interested in a complete picture of Guild AI, start by
browsing its comprehensives documentation.

</p>
<a class="btn btn-primary" href="/docs/">Browse the docs <i class="fa next"></i></a>
</div>
</div>
</div>
