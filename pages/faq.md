title: FAQ
navbar_item: yes
hide_sidenav: yes

<div id="get-started-fab"></div>

# Frequently Asked Questions

[TOC]

## About Guild AI

### What is Guild AI?

Guild AI is software platform used by machine learning engineers to
control and measure machine learning work so that data scientists,
engineers, and product managers can make informed decisions about
model performance and safety.

Refer to the [Guild AI front page](https://guild.ai) for a complete
description, features, and links to documentation.

Guild AI also refers to the company behind the platform. In cases
where we differentiate the software from the company, we use *Guild AI
platform* or *Guild AI software*.

### Is Guild AI open source?

Guild is 100% open source. It's freely available under the [Apache 2.0
->](https://github.com/guildai/guildai/blob/master/LICENSE.txt)
license.

### Is Guild AI affiliated with a closed source platform or vendor?

Guild AI is an independent open source company without ties to a
proprietary platform or cloud.

### What is Guild AI's business model?

Guild AI is an open source company that generates revenue from
services and support around the Guild AI platform. Guild AI supports
companies in the development of controlled machine learning pipelines
for the purpose of building higher performance models that meet the
safety and ethical guidelines defined by the company and regulatory
agencies.

See [Guild AI Services](/services.md) for information on how Guild AI
can support your organization.

### Is it "Guild AI" or "guild.ai"?

When writing Guild AI, use "Guild AI" --- not guild.ai.

guild.ai is used in the logo and is also the product domain. Guild AI,
with a space, is the correct use of the both the product and company
names.

## Using Guild AI

### Guild AI seems magical at times --- can I make it explicit?

*Guild AI lets you explicitly configure all aspects of your project.*

Guild AI is designed to start quickly and easily and to evolve to
support advanced functions as needed. To accomplish this, Guild
supports a number auto-detect features:

- User input interface: *command line arguments* or *global variables*
- User input flag names, types, and descriptions
- Output metrics

All of these features can be controlled using explicit project
configuration.

Refer to [Guild Files](/guildfile.md) for information on configuring
a project.

<!--

### What is Guild AI?

Guild AI is an experiment tracking system for machine learning. It's
used by engineers and researchers to run scripts, compare results, and
automate machine learning workflow.

Guild is a light weight, external tool that doesn't require changes to
your code. It runs scripts in written in any language or framework on
Linux, macOS, and Windows.

### When should I use Guild?

Guild gives you insight into your machine learning work. Use it when
you want to:

- Establish performance baselines for ongoing work and comparison
- Tune hyperparameters
- Simplify reproducibility for yourself and others
- Create an audit trail for explanability and compliance

You can start using Guild at any stage if your project lifecycle. Use
it early to measure progress or after the project stabilizes to tune
hyperparameters and automate reproducibility. When it's time to run in
production, use Guild to track pipeline artifacts.

### How much does Guild cost?

Guild AI is free, both as in beer and liberty. It's available under
the [Apache 2.0
->](https://github.com/guildai/guildai/blob/master/LICENSE.txt)
license.

While Guild costs time and effort to learn, it's [easy to start
with](/start.md) and use features incrementally.

### How is Guild different from other experiment management systems?

- Guild is an external tool, not an embedded library
- Guild is light weight
- Guild does not require you to modify your code
- Guild does not require additional software or systems like databases
  or containers

### Why not just embed a library for experiment tracking?

When you modify your code to support a library, you take on a new set
of requirements. Your code not only relies on the new software, it
relies on the infrastructure and services that software uses:

 - Databases
 - Servers
 - Container management systems
 - Distributed file systems
 - Non-free (closed-source, paid) backend services

Simple changes to your code (e.g. a few decorated functions) baloon
into higher costs:

 - System installation and maintenance
 - Hardware and networking
 - Vendor lock in
 - Runtime complexity
 - Non-portability of your models

Non-portable models have a particularly high host: lost feedback and
contributions from those who find your experiment tracking
requirements onerous.

### How does Guild work without requiring code changes?

Guild is designed as a traditional build tool. It relies on external
configuration and operating system conventions to perform its work.

Guild interfaces with your scripts using standard operating system
conventions (command arguments, environment variables, standard ouput,
file systems, etc.). This interface is available for any language,
framework, and platform, making Guild flexible for a wide range of
applications.

Guild provides some magic for Python scripts that rely on global
variables, which are commonly used in Notebooks, examples, and
prototypes. This interface is still external --- there's no
requirement to change your code. It's easily changed to support
command line arguments if you want.

### How does Guild save results?

Guild saves all results on a locally mounted file system. Guild does
not use databases.

This has a number of benefits:

- No database installation and maintenance costs
- Access to standard file system tools to read, copy, and archive
  experiments
- Access to standard file and directory diffing tools to compare runs

Guild uses SQLite to index results for fast lookup. This is how [Guild
Compare](ref:guild-compare) and [Guild View](ref:guild-view) both
perform quickly.

-->
