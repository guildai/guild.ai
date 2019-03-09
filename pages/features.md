navbar_item: yes
hide_sidenav: yes
hide_pagenav: yes
hide_in_pagenav: yes

# Features

## Experiment management

<div class="row feature-focus">
  <div class="col-md-2 col-sm-2 icon">
    <i class="far fa-box-check feature-icon"></i>
  </div>
  <div class="col-md-10 col-sm-10 detail">
    <p>
      Guild tracks each operation as a unique experiment. Simply run
      your script with the <code>guild</code> command:

      <div class="text-editor inline sm">
        <div class="text-body">
          $ guild run train.py
        </div>
      </div>
    </p>
    <p>
      Guild automatically captures essential details about the
      training run:
      <ul class="md">
        <li>Model metrics such loss and accuracy</li>
        <li>Generated files such as checkpoints, images, text, etc.</li>
        <li>Logs and command output</li>
        <li>Source code used in the experiment</li>
      </ul>
    </p>
    <h4>What's the payoff?</h4>
    <p>
      When you systematically capture training runs, remarkable things
      happen:

      <ul class="md">
        <li>You <strong>know</strong> when you're improving and when
        you're regressing</li>
        <li>You can <strong>analyze</strong> differences across runs
        to better understand a result</li>
        <li>You can <strong>share</strong> your results with colleagues</li>
        <li>You can <strong>backup</strong> trained models&mdash;some
          of which may have taken days to generate&mdash;for
          safekeeping</li>
        <li>You can <strong>optimize</strong> your model by focussing
        on approaches that perform well and avoiding those that
        don't</li>
      </ul>
    </p>
    <h4>But I already use a spreadsheet to track results</h4>
    <p>
      Guild is <em>automatic</em>&mdash;it does the work for when you
      run your training script so you don't have to copy and paste. It
      captures everything associated with an
      experiment&mdash;hyperparameters, metrics, logs, generated
      files, and even source code snapshots! With this detail, you can
      do more than merely report results: you can
      <strong>systematically improve your model</strong>.
    </p>
    <p>And you can
      always <a href="/docs/guides/export-spreadsheet/">export your
      results to a spreadsheet</a> with Guild!
    </p>
  </div>
</div>

## Auto ML

<div class="row feature-focus">
  <div class="col-md-2 col-sm-2 icon">
    <i class="far fa-bullseye-arrow feature-icon"></i>
  </div>
  <div class="col-md-10 col-sm-10 detail">
    <p>
      Automated machine learning&mdash;<em>Auto ML</em>&mdash;is the
      process of applying machine learning to machine learning. Rather
      than manually design models and select hyperparameters, you
      leverage the power of the computer to automatically learn them!

      <div class="text-editor inline sm">
        <div class="text-body">
          $ guild run train.py x=[-2.0:2.0] --optimizer bayesian
        </div>
      </div>
    </p>
    <p>
      This commands runs your script <code>train.py</code> but applied
      a Bayesian optimizer to run it multiple times, each time using
      different hyperparameters
      <ul class="md">
        <li>xxx</li>
        <li>xxx</li>
        <li>xxx</li>
        <li>xxx</li>
      </ul>
    </p>
    <h4>When would I use this?</h4>
    <p>
      XXX
    </p>
  </div>
</div>

## Reproducibility

<div class="row feature-focus">
  <div class="col-md-2 col-sm-2 icon">
    <i class="far fa-balance-scale feature-icon"></i>
  </div>
  <div class="col-md-10 col-sm-10 detail">
    <p>
    </p>
    <p><strong>Step 1</strong> - Get the project source code:
      <div class="text-editor inline sm">
        <div class="text-body">
          $ git checkout https://github.com/OliverRichter/SAVER
        </div>
      </div>
    </p>

    <p><strong>Step 2</strong> - Change to the project directory:
      <div class="text-editor inline sm">
        <div class="text-body">
          $ cd SAVER
        </div>
      </div>
    </p>

    <p><strong>Step 3</strong> - Use Guild to recreate the results:
      <div class="text-editor inline sm">
        <div class="text-body">
          $ guild run
        </div>
      </div>
    </p>

    <p>
      Guild takes care of the rest automatically:
      <ul class="md">
        <li>Download any required libraries and data sets</li>
        <li>Run the exact command prescribed by the author for
        recreating the result</li>
        <li>Capture the results for comparison</li>
      </ul>
    </p>
    <h4>I'm not a researcher, I don't need to reproduce my results!</h4>
    <p>
      To be fair, some researchers feel they don't need to reproduce
      their results <i class="far fa-smile-wink"></i>
    </p>
    <p>
      In time reproducibility in machine learning will become as
      important as it is in other engineering disciplines. If it's not
      important for you now, consider the benefits of automating your
      worflow:
      <ul class="md">
        <li>You can run more experiments, which gives you more data,
        which lets you build better models</li>
        <li>By automating your steps, you're less likely to make
        process-related mistakes (e.g. copying the wrong directory,
        using the wrong hyperparameter, etc.)</li>
        <li>When presenting your results to your boss, client, or
        sponsor, your credibility goes way up when you can confidently
        reproduce a result at any time</li>
      </ul>
    </p>
  </div>
</div>

## Analytics

<div class="row feature-focus">
  <div class="col-md-2 col-sm-2 icon">
    <i class="far fa-analytics feature-icon"></i>
  </div>
  <div class="col-md-10 col-sm-10 detail">
    <p>
      XXX

      <div class="text-editor inline sm">
        <div class="text-body">
          $ guild tensorboard
        </div>
      </div>
    </p>
    <p><img class="md shadow lozad" data-src="/assets/img/tb-feature.jpg" /></p>
    <figcaption class="under-shadow">Compare experiment results in TensorBoard</figcaption>
    <p>
      XXX
      <ul class="md">
        <li>xxx</li>
        <li>xxx</li>
        <li>xxx</li>
        <li>xxx</li>
      </ul>
    </p>
  </div>
</div>

## End-to-end learning

<div class="row feature-focus">
  <div class="col-md-2 col-sm-2 icon">
    <i class="far fa-route feature-icon"></i>
  </div>
  <div class="col-md-10 col-sm-10 detail">
    <p>
      XXX

      <div class="text-editor inline sm">
        <div class="text-body">
          $ guild run prepare-train-compress --optimizer forest --minimize overall_loss
        </div>
      </div>
    </p>
    <p>
      XXX
      <ul class="md">
        <li>xxx</li>
        <li>xxx</li>
        <li>xxx</li>
        <li>xxx</li>
      </ul>
    </p>
    <h4>I have no idea what you're talking about</h4>
    <p>
      Check out <a target="_blank" class="ext"
      href="https://www.ml4aad.org/wp-content/uploads/2018/12/AutoML-Tutorial-NeurIPS2018-MetaLearning.pdf#page=22">Learning
      Pipelines</a> from Frank Hutter and Joaquin Vanschoren,
      presented at <em>NeurIPS 2018 Tutorial on Automatic Machine
      Learning</em>. Then check out our step-by-step guide
      to <a href="/docs/guide/end-to-end/">End-to-End Learning</a>.
    </p>
  </div>
</div>

## Remote training and backups

<div class="row feature-focus">
  <div class="col-md-2 col-sm-2 icon">
    <i class="far fa-chart-network feature-icon"></i>
  </div>
  <div class="col-md-10 col-sm-10 detail">
    <p>
      XXX

      <div class="text-editor inline sm">
        <div class="text-body">
          $ guild push s3
        </div>
      </div>
    </p>
    <p>
      XXX
      <ul class="md">
        <li>xxx</li>
        <li>xxx</li>
        <li>xxx</li>
        <li>xxx</li>
      </ul>
    </p>
    <h4>Why should I care about backing anything up?</h4>
    <p>
      If you've never lost your work to an accident, this is an
      excellent question <i class="far fa-smile"></i>
    </p>
    <p>
      In all seriousness, you may not care about backing up trained
      models if you can easily recreate them. Guild makes it
      incredibly easy to recreate results so if you're model trains
      quickly and you have retained the original data set, you might
      skip this feature. However, if you're doing deep learning and
      your models take more than a few minutes to train, it's a simple
      matter to sync your runs to a remote service like S3. So why
      not?
    </p>
  </div>
</div>
