# pyemotionwheel

<!-- TODO: Add featured image -->

IMAGE

`pyemotionwheel` is a Python library that provides a programmatic interface to an emotion wheel, a simple psychological tool for identifying and articulating emotions.

The library models an emotion wheel as a hierarchical tree structure, with primary emotions at its core and more nuanced secondary and tertiary emotions branching out:

<!-- TODO: Add emotion wheel image -->

IMAGE

This tool can be especially beneficial in therapeutic settings, educational environments, and personal development for enhancing emotional intelligence.

## Why does pyemotionwheel exist?

In the realm of psychology, identifying and articulating emotions is an essential step towards understanding and managing them effectively.

**My bond with the emotion wheel is also _deeply personal._**

I grew up in a broken home. Surviving a near-detal car accident at 13 years old, led to an emotional shutdown to cope with the trauma and ensuing family turmoil.

Two decades later, I began to unlock those surpressed emotions.

**The emotion wheel, a seemingly simple tool, proved crucial for me to identify and express my feelings, enhancing my emotional literacy.**

As a developer, I felt called to create an open source implementaiton of the emotion wheel that myself and other programmers can utilize in their own projects.

## Installation

You can install `pyemotionwheel` and its dependencies using `pip`:

```shell
$ pip install pyemotionwheel anytree
```

The only dependency is [anytree](https://anytree.readthedocs.io/en/latest/), a simple, lightweight implementation of a [Tree](https://en.wikipedia.org/wiki/Tree_(data_structure)) data structure. Since an emotion wheel is effectively just a hierarchical representation of emotions, a Tree data structure can naturally be used.

## Usage

Here's how to utilize each of the public methods in the `EmotionWheel` class.

### All emotions

To get _all_ emotions present in the wheel:

...

### Primary emotions

Retrieve all primary emotions (i.e., first level of the wheel):

...

### Secondary emotions

Retrieve all secondary eotions (i.e., second level of the wheel):

...

### Tertiary emotions

Retrieve all tertiery emotions (i.e., third and final level of the wheel):

...

### Find a specific emotion

You can lookup a specific emotion in the wheel by supplying the `name` of the emotion:

...

### Common implementation patterns

...

## License

`pyemotionwheel` is released under the MIT License. This means it is free to use, modify, and distribute, including for commercial use, provided the license and copyright notice are preserved.

**Note**: Always remember to adhere to the MIT License when using or modifying `pyemotionwheel`.
