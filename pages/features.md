navbar_item: yes
hide_sidenav: yes
hide_pagenav: yes
hide_in_pagenav: yes

<div id="get-started-fab"></div>

# Features

## Experiment management

<div class="row feature-focus">
  <div class="col-md-2 col-sm-2 icon">
    <i class="far fa-box-check feature-icon"></i>
  </div>
  <div class="col-md-10 col-sm-10 detail">
    <p>
      Guild tracks each operation as a unique experiment. Simply run
      your script with the <code>guild</code> command.

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
        <li>You can <strong>backup</strong> trained models &mdash;
          some of which may have taken days to generate &mdash; for
          safekeeping</li>
        <li>You can <strong>optimize</strong> your model by focusing
        on approaches that perform well and avoiding those that
        don't</li>
      </ul>
    </p>
    <h4>But I already use a spreadsheet to track results</h4>
    <p>
      Guild is <em>automatic</em> &mdash; it does the work for when
      you run your training script so you don't have to copy and
      paste. It captures everything associated with an experiment
      &mdash; hyperparameters, metrics, logs, generated files, and
      even source code snapshots! With this detail, you can do more
      than merely report results: you can
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
      Auto ML stands for <em>automated machine learning</em> &mdash;
      the process of applying machine learning to machine
      learning. Rather than manually design models and select
      hyperparameters, automatically learn them! The result
      is <strong>better models in less time</strong>.

      <div class="text-editor inline sm">
        <div class="text-body">
          $ guild run train.py x=[-2.0:2.0] --optimizer bayesian --max-trials 100
        </div>
      </div>
    </p>
    <p>
      This commands runs <code>train.py</code> using a Bayesian
      optimizer:
      <ul class="md">
        <li>Runs the script 100 times, each time with different values
        for <code>x</code></li>
        <li>Selects values between <code>-2.0</code>
        and <code>2.0</code> &mdash; the <em>search space</em>
        for <code>x</code></li>
        <li>Uses the result of each trial to choose values
        for <code>x</code> that are likely to improve results
        (e.g. higher accuracy)</li>
      </ul>
    </p>
    <h4>When would I use this?</h4>
    <p>
      Whenever you want to improve your model! Model tuning is one of
      the most effective way to improve accuracy &mdash; in some cases
      it can be more effective than more data! And Guild makes it
      easy, so why not give it a try and see what happens?
    </p>
    <h4>What Bayesian methods does Guild support?</h4>
    <p>
      Guild supports a number of state-of-the-art optimization
      algorithms:
      <ul class="md">
        <li>Gaussian process</li>
        <li>Decision tree</li>
        <li>Gradient boosted trees</li>
        <li>Tree of Parzen estimator (coming)</li>
      </ul>
    </p>
    <h4>But I prefer manual tuning</h4>
    <p>
      We wholeheartedly agree! That's why Guild supports an
      incremental approach to hyperparameter tuning:
      <ul class="md">
        <li>Use well-known hyperparameters during model development
          <div class="text-editor inline sm">
            <div class="text-body">
              $ guild run train.py x=0.1
            </div>
          </div>
        </li>
        <li>Selectively expand the range with grid search (run once
        for each value specified)
          <div class="text-editor inline sm">
            <div class="text-body">
              $ guild run train.py x=[-0.1,0,0.1,0.2]
            </div>
          </div>
        </li>
        <li>If your search space is large, try random search
          <div class="text-editor inline sm">
            <div class="text-body">
              $ guild run train.py x=[-4.0:4.0] --optimizer random
            </div>
          </div>
        </li>
        <li>When you want to optimize your model, use Bayesian search
          <div class="text-editor inline sm">
            <div class="text-body">
              $ guild run train.py x=[-2.0:2.0] --optimizer bayesian
            </div>
          </div>
        </li>
      </ul>
    </p>
    <p>
      Of course you can always try Bayesian optimization to start
      &mdash; it can be remarkably efficient! Whatever approach you
      take, Guild lets you control every step.
    </p>
    <p>
      For a step-by-step guide,
      see <em><a href="/docs/start/optimization/">Get Started -
      Hyperparameter Optimization</a></em>.
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
      When you use Guild to train your models, you make it easier for
      others to reproduce your results &mdash; or at least to recreate
      your experiments. It looks something like this:
    </p>
    <p><strong>Step 1</strong> - Get the project source code
      <div class="text-editor inline sm">
        <div class="text-body">
          $ git checkout https://github.com/guildai/amazing-results-project
        </div>
      </div>
    </p>

    <p><strong>Step 2</strong> - Change to the project directory
      <div class="text-editor inline sm">
        <div class="text-body">
          $ cd amazing-results-project
        </div>
      </div>
    </p>

    <p><strong>Step 3</strong> - Use Guild to recreate the results
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
    <h4>I'm not a researcher, I don't need to reproduce my results</h4>
    <p>
      Even some researchers feel they don't need to reproduce
      their results <i class="fal fa-smile-wink"></i>
    </p>
    <p>
      Reproducibility aside, consider the benefits of automating your
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
    <p>
      For a step-by-step guide,
      see <em><a href="/docs/start/reproducibility/">Get Started -
      Reproducibility</a></em>.
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
      Guild is tightly integrated with analytic tools like
      TensorBoard, which let you easily compare experiment results and
      drill into training details.

      <div class="text-editor inline sm">
        <div class="text-body">
          $ guild tensorboard
        </div>
      </div>
    </p>
    <figure>
      <p><img class="md shadow lozad" data-src="/assets/img/tb-feature.jpg" /></p>
      <figcaption class="under-shadow">Compare experiment results in TensorBoard</figcaption>
    </figure>
    <p>
      Guild integration with TensorBoard consists of:
      <ul class="md">
        <li>Launch TensorBoard with a single command</li>
        <li>Automatically sync experiments with TensorBoard as they're updated</li>
        <li>Filter runs by operation name, label, and run status</li>
      </ul>
    </p>
    <p>
      For a step-by-step guide,
      see <em><a href="/docs/start/tensorboard/">Get Started -
      TensorBoard</a></em>.
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
      Guild has a powerful workflow feature, which lets you run
      multiple steps in a single operation. Consider this scenario for
      training and deploying a model for a mobile application:
      <ol class="md">
        <li>Prepare data set for training</li>
        <li>Train model</li>
        <li>Compress model</li>
      </ol>
    </p>
    <p>
      The primary goal is to maximize classification accuracy &mdash;
      but because the model is deployed to a resource constrained
      environment so you want to also <em>minimize</em> model size.
    </p>
    <p>
      Here's how you'd do it in Guild:

      <div class="text-editor inline sm">
        <div class="text-body">
          $ guild run workflow --optimizer bayesian --maximize accuracy --minimize model-size
        </div>
      </div>
    </p>
    <p>
      This is the <code>workflow</code> definition:
      <pre class="language-yaml gf-sample">workflow:
  description: Run training end-to-end, including model compression
  steps:
    - prepare-data
    - train
    - compress</pre>
    </p>
    <p>
      Running the <code>workflow</code> operation with a Bayesian
      optimizer, Guild attempts to both maximize model accuracy and
      minimize model size by adjusting hyperparameters across each of
      the three operations: <em>prepare-data</em>, <em>train</em>,
      and <em>compress</em>.
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
      Guild commands can be run remotely! Simply
      <a href="/docs/reference/user-config/#remote">define a
      remote</a> and reference it using the <code>--remote</code>
      command line option when running Guild commands.
    </p>
    <p>
      Here's an example of running <code>train.py</code> on a remote
      named <code>ec2-v100</code>:
      <div class="text-editor inline sm">
        <div class="text-body">
          $ guild run train.py --remote ec2-v100
        </div>
      </div>
    </p>
    <p>
      Here's a sample remote configuration:

      <pre class="language-yaml gf-sample">ec2-v100:
  type: ec2
  region: us-east-2
  ami: ami-0a47106e391391252
  instance-type: p3.2xlarge</pre>
    </p>
    <p>
      Guild also lets you easily copy experiments to and from remote
      locations, including AWS S3 and SSH accessible servers.
    </p>
    <p>
      Here's an example of copying local experiments to a remote
      named <code>s3</code>:
      <div class="text-editor inline sm">
        <div class="text-body">
          $ guild push s3
        </div>
      </div>
    </p>
    <p>
      And a sample configuration for <code>s3</code>:

      <pre class="language-yaml gf-sample">s3:
  type: s3
  bucket: my-experiments</pre>
    </p>
    <h4>Can't I just use floppy disks for backup?</h4>
    <p>
      1.44 MB is big but cloud storage even bigger!
    </p>
    <p>
      Backing experiments up to local storage is trivial with Guild
      &mdash; it's simply a matter of running the <code>push</code>
      command. Guild copies only the differences so it's an efficient
      operation.
    </p>
    <h4>Simple team collaboration</h4>
    <p>
      Remote backup is also easy way to collaborate with colleague and
      fellow machine learning engineers. Consider this simple
      workflow:
      <ol>
        <li>
          One or more scientists/engineers run experiments for a
          particular task with Guild (e.g. experiments explore task
          performance across a variety of models and hyperparameters).
        </li>
        <li>
          Each scientist/engineer routinely copies experiments to a
          common remote location &mdash; this serves to backup work
          but also makes that work available to everyone on the team!
        </li>
        <li>
          To compare results across the team, a scientist/engineer
          need only synchronize with the remote location using
          Guild <code>pull</code> to get everyone's experiments.
        </li>
      </ol>
    </p>
    <p>
      For step-by-step guides, see Get Started
      for <em><a href="/docs/start/backup-restore/">Backup and
      Restore</a></em>
      and <em><a href="/docs/start/remote-train/">Remote
      Training</a></em>.
    </p>
  </div>
</div>
