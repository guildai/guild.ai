title: FAQ
navbar_item: yes
hide_sidenav: yes
hide_pagenav: yes

<div id="get-started-fab"></div>

# Frequently Asked Questions

[TOC]

## About

### What is Guild AI?

Guild AI is an experiment tracking system for machine learning. It's
used by engineers and researchers to run scripts, compare results, and
automate machine learning workflow.

Guild is a light weight, external tool that doesn't require changes to
your code. It runs scripts in written in any language or framework on
Linux, macOS, and Windows.

Guild AI also refers to the company behind the platform. In cases
where we differentiate the software from the company, we use *Guild AI
platform* or *Guild AI software*.

### When would I use Guild AI?

Guild gives you insight into your machine learning work. Use it when
you want to:

- Track experiments
- Tune hyperparameters
- Automate reproducibility for yourself and others
- Establish performance baselines for ongoing work and comparison
- Create an audit trail for ML explainability and regulatory
  compliance

Use Guild early to measure progress or after the project stabilizes to
tune hyperparameters and automate reproducibility. When it's time to
run in production, use Guild to track pipeline artifacts for
operational control.

### How much does Guild cost?

Guild is 100% open source. It's freely available under the [Apache
2.0](https://github.com/guildai/guildai/blob/master/LICENSE.txt)
license.

### How is Guild different from other experiment management systems?

- Guild is an external tool, not an embedded library
- Guild does not require you to modify your code
- Guild does not require additional software or systems like databases
  or containers

### Why not just embed a library for experiment tracking?

When you modify your code to support a library, you take on a new set
of requirements. Your code relies on the new software. It relies on
the infrastructure and services that software uses.

 - Databases
 - Servers
 - Container management systems
 - Distributed file systems
 - Non-free (closed-source, paid) back-end services

Simple changes to your code (e.g. a few decorated functions) can lead
to surprisingly high costs.

 - System installation and maintenance
 - Hardware and networking
 - Vendor lock in
 - Runtime complexity
 - Non-portability of your models

Non-portable models have a particularly high cost: *lost feedback and
contributions from colleagues who can't run your code because the
overall system requirements are too high.*

### Is Guild AI affiliated with a closed source platform or vendor?

Guild AI is an independent open source company without ties to a
proprietary platform or cloud.

### What is Guild AI's business model?

Guild AI is an open source company that generates revenue from
services and support around the Guild AI platform. Guild AI supports
companies in the development of controlled machine learning
pipelines. We specialize in building high performance models that meet
the safety and ethical guidelines defined by our clients and
regulatory agencies.

See [*Guild AI Services*](/services.md) for information on how Guild
AI can support your organization.

### Is it "Guild AI" or "guild.ai"?

When writing Guild AI, use "Guild AI" --- not guild.ai.

guild.ai is used in the logo and is also the product domain. Guild AI,
with a space, is the correct use of the both the product and company
name.

## Using Guild AI

### What's the fatest way to get started?

- [Get Started with Guild AI](https://my.guild.ai/start)
- [Ask a question](https://my.guild.ai/new-topic?category=general)

### Can I customize Guild?

Guild AI lets you explicitly configure all aspects of your project.

Guild AI is designed to start quickly and easily and to evolve to
support advanced functions as needed. Guild supports a number
auto-detect features:

- User input interface: *command line arguments* or *global variables*
- User input flag names, types, and descriptions
- Output metrics

All of these features can be controlled using explicit project
configuration.

Refer to [*Guild Files*](https://my.guild.ai/docs/guildfiles) for
information on configuring a project.

### My script needs a file but can't find it!

Guild executes each run in the context of a [*run
directory*](https://my.guild.ai/docs/runs#run-directory), which is
initially empty. Your script assumes that it's run from your *project
directory*. Any files that your script requires *must be explicitly
configured using a Guild file*.

Refer to [*Dependencies*](https://my.guild.ai/docs/dependencies) for
details on configuring required resources for your operations.

## Implemenetation

### How does Guild work without requiring code changes?

Guild is a traditional build tool. It relies on external configuration
and operating system conventions.

Guild interfaces with your scripts using standard operating system
conventions (command arguments, environment variables, standard
output, file systems, etc.). This interface is available for any
language, framework, and platform.

Guild performs some magic for Python scripts that rely on global
variables. This is common in Notebooks, examples, and prototypes. The
interface is still external. You don't need to change your code.

### How does Guild save results?

Guild saves all results on a locally mounted file system. Guild does
not use databases.

This has a number of benefits:

- No database installation and maintenance costs
- Access to standard file system tools to read, copy, and archive
  experiments
- Access to standard file and directory diffing tools to compare runs

<div class="col col-md-12 mt-5">
<div class="promo center">
<a class="btn btn-primary cta" href="https://my.guild.ai/start"><img src="/assets/icons/space-rocket-flying-white.svg" height="24"> Get Started with Guild AI</a>
</div>
</div>
