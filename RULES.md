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

If the statement is made from the perspective of Guild authors, use
*we*. For example:

- We recommend that you define the package first.

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

## Past, Present, and Future Tense

*When referring to something that obviously occurred in the past, use
past tense.*

*Otherwise, use present tense, even when an event will occur in the
future.*

Good:

- In the previous section, you trained a model.
- In the next section, you train a model.
- (at the end of the section) In this section, you trained a model.
- (at the start of the section) In this section, you train a model.

Bad:

- In the previous section, you train a model.
- In the next section, you will train a model.

If an expression using present tense is confusing, use future.

Good:

- Your results will differ

Bad:

- Your results differ

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

## Referencing commands

Avoid "the `cmd` command" or "the command `cmd`" in favor simply of
"`cmd`". Avoid starting a sentence with a command.

Good:

- Use `cmd` to do something.

- When you run `cmd`, Guild does something.

- On `cmd`, Guild does something.

Bad:

- Use the `cmd` command to do something.

- `cmd` does something.
