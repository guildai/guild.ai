title: FAQ
navbar_item: yes
hide_sidenav: yes

<div id="get-started-fab"></div>

# Frequently Asked Questions

[TOC]

### What is Guild AI?

Guild AI is an experiment tracking system for machine learning. It's
used by engineers and researchers to run scripts, compare results, and
automate machine learning workflow.

Guild is a light weight, external tool that doesn't require changes to
your code. It runs scripts in written in any language or framework on
Linux, macOS, and Windows.

### When would I use Guild?

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

Guild costs time and effort to adopt. But it's [easy to
start](start.md) and learning Guild features is straight forward and
incremental.

### How is Guild different from other experiment management systems?

Guild AI is unique among the alternatives:

- External tool, not an embedded library
- Requires changes to code
- Requires additional required software or services

This makes Guild easier to use and less complex, without sacrificing
[features](index.md#features).

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

Guild is designed as a traditional build tools. It relies on external
configuration and operating system conventions to perform its work.

For configuration, Guild relies on a TODO --- a human readable file
that tells Guild about your code.

Guild otherwise interfaces with your scripts using standard operating
system conventions (command arguments, environment variables, standard
ouput, file systems, etc.). This interface is available for any
language, framework, and platform, making Guild flexible for a wide
range of applications.

Guild provides a bit of magic for Python scripts that rely on global
variables (commonly used in Notebooks, examples, and
prototypes). However, this interface is still external --- there's no
requirement to change your code to accommodate Guild. It's easily
changed to support command line arguments if you want.

### How does Guild store results?

Guild stores all results on a locally mounted file system. Guild does
not use databases.

This has a number of benefits:

- Zero database install and maintenance costs
- Access to standard file system tools to read, copy, and archive
  experiments
- Access standard file and directory diffing tools to compare runs

Guild uses SQLite to index results for fast lookup. This is how [Guild
Compare](tools/compare.md) and [Guild View](tools/view.md) both
perform quickly. The use of SQLite in this case is a performance
optimization and not how experiments are stored.

### Why doesn't Guild have many GitHub stars?

We don't ask for GitHub stars. If your boss requires a certain number
of stars before he or she approves the use of a quality, useful tool,
we're sorry and good luck!
