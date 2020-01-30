tags: concept

# Batches

[TOC]

## Overview

## Optimizers

## Batch Files

A batch file is a data file that contains one or more sets of flag
values for use in an operation. Batch files may be defined using
various formats:

- CSV format -- first line defines flag names and each subsequent line
  contains associated flag values for a run
- JSON format -- encoded list of objects representing flag values for a run
- YAML format -- encoded list of mappings representing flag values for
  a run

Batch files are specified using an argument in the format ``@PATH`` to
the [run](cmd:run) command. Guild starts a run for each set of flags
defined in each specified batch files.

Consider this CSV file:

``` csv
learing-rate,batch-size
0.1,100
0.1,1000
0.01,100
0.01,1000
```

^ `batch.csv`

The following command would generate four runs, one for each set of
flag values defined in `batch.csv`:

``` command
guild run train @batch.csv
```

Here's is an equivalent batch file using the JSON format:

``` json
[
  {"learning-rate": 0.1, "batch-size": 100 },
  {"learning-rate": 0.1, "batch-size": 1000 },
  {"learning-rate": 0.01, "batch-size": 100 },
  {"learning-rate": 0.01, "batch-size": 1000 }
]
```

^ `batch.json`

And in YAML format:

``` yaml
- learning-rate: 0.1
  batch-size: 100
- learning-rate: 0.1
  batch-size: 1000
- learning-rate: 0.01
  batch-size: 100
- learning-rate: 0.01
  batch-size: 1000
```

^ `batch.yml`
