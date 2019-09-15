# Rules for Writing Docs

Goals:

- Be direct without losing clarity
- Minimize the number of words in a sentense
- Minimize complexity
- Avoid formalism unless

## Second Person

*Use second person when interacting with user-related tasks.*

Good:

- You configure the project using a Guild File.

Bad:

- We configure the project using a Guild file.

## Auxiliary Verbs

*Avoid using auxiliary verbs like can and may unless the sentence
would be incorrect without their use.*

Good:

- You configure the project using a Guild File.

Bad:

- You can configure the project using a Guild File.

## Use of Next in Steps

*Avoid "next" in steps.*

Good:

- Train the model.

Bad:

- Next, train the model.

## Present Tense

*Unless it would make a statement confusing or incorrect, use present
tense, even when addressing events that are described earlier or
later.*

Good:

- In the previous section, you train a model.

Bad:

- In the previous section, you trained a model.

## Passive Voice

*Avoid passive voice.*

Good:

- The user trains a model.

Bad:

- The model is trained.

## Title Case

*Use title case in titles and headings.*

Good:

- Configure Your Project

Bad:

- Configure your project

## Gerunds

*Avoid the use of gerunds in titles and headings.*

Good:

- Train a Model

Bad:

- Training a Model

## TOC Location

*When using a TOC, insert the TOC immediately following the page
title.*

## TOC Front Matter

*Avoid front matter that appears before the first heading.*

Good:

```
[TOC]

# Heading 1

Intro text.
```

Bad:

```
TOC]

Intro text.

# Heading 1
```

## Superlatives

*Don't use superlatives like great, excellent, amazing.*

Good:

- Tim Peters wrote PEP 20.

Bad:

- Tim Peters wrote the excellent PEP 20.
