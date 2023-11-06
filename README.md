# pyemotionwheel

<!-- TODO: Add featured image -->

IMAGE

`pyemotionwheel` is a Python library that provides a programmatic interface to an emotion wheel, a simple psychological tool for identifying and articulating emotions.

The library models an emotion wheel as a hierarchical tree structure, with primary emotions at its core and more nuanced secondary and tertiary emotions branching out:

<!-- TODO: Add emotion wheel image -->

IMAGE

This tool can be especially beneficial in therapeutic settings, educational environments, and personal development for enhancing emotional intelligence.

<!-- TODO: Generate table of contents -->

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

### Instantiate the emotion wheel

Instantiate an instance of the emotion wheel, then show the tree structure:

```python
>>> from pyemotionwheel import EmotionWheel
>>> wheel = EmotionWheel()
>>> print(wheel)
root
├── Anger
│   ├── Rage
│   │   ├── Hate
│   │   └── Hostile
│   ├── Exasperated
│   │   ├── Agitated
│   │   └── Frustrated
│   ├── Irritable
│   │   ├── Annoyed
│   │   └── Aggravated
│   ├── Envy
│   │   ├── Resentful
│   │   └── Jealous
│   └── Disgust
│       ├── Contempt
│       └── Revolted
├── Sadness
│   ├── Suffering
│   │   ├── Agony
│   │   └── Hurt
│   ├── Despondent
│   │   ├── Depression
│   │   └── Sorrow
│   ├── Disappointed
│   │   ├── Dismayed
│   │   └── Displeased
│   ├── Shameful
│   │   ├── Regretful
│   │   └── Guilty
│   ├── Neglected
│   │   ├── Isolated
│   │   └── Lonely
│   └── Despair
│       ├── Grief
│       └── Powerless
├── Surprise
│   ├── Stunned
│   │   ├── Shocked
│   │   └── Dismayed
│   ├── Confused
│   │   ├── Disillusioned
│   │   └── Perplexed
│   ├── Amazed
│   │   ├── Astonished
│   │   └── Awe-struck
│   ├── Overcome
│   │   ├── Speechless
│   │   └── Astounded
│   └── Moved
│       ├── Stimulated
│       └── Touched
├── Joy
│   ├── Content
│   │   ├── Pleased
│   │   └── Satisfied
│   ├── Happy
│   │   ├── Amused
│   │   └── Delighted
│   ├── Cheerful
│   │   ├── Jovial
│   │   └── Blissful
│   ├── Proud
│   │   ├── Triumphant
│   │   └── Illustrious
│   ├── Optimistic
│   │   ├── Eager
│   │   └── Hopeful
│   ├── Enthusiastic
│   │   ├── Excited
│   │   └── Zeal
│   ├── Elation
│   │   ├── Euphoric
│   │   └── Jubilation
│   └── Enthralled
│       ├── Enchanted
│       └── Rapture
├── Love
│   ├── Affectionate
│   │   ├── Fondness
│   │   └── Romantic
│   ├── Longing
│   │   ├── Sentimental
│   │   └── Attracted
│   ├── Desire
│   │   ├── Passion
│   │   └── Infatuation
│   ├── Tenderness
│   │   ├── Caring
│   │   └── Compassionate
│   └── Peaceful
│       ├── Relieved
│       └── Satisfied
└── Fear
    ├── Sacred
    │   ├── Frightened
    │   └── Helpless
    ├── Terror
    │   ├── Panic
    │   └── Hysterical
    ├── Insecure
    │   ├── Inferior
    │   └── Inadequate
    ├── Nervous
    │   ├── Worried
    │   └── Anxious
    └── Horror
        ├── Mortified
        └── Dread
```

### All emotions

To get _all_ emotions present in the tree, ignoring any hierachical structure:

```python
>>> wheel.all_emotions()
(EmotionNode(name='Anger'),
 EmotionNode(name='Rage'),
 EmotionNode(name='Hate'),
 EmotionNode(name='Hostile'),
 EmotionNode(name='Exasperated'),
 EmotionNode(name='Agitated'),
 EmotionNode(name='Frustrated'),
 EmotionNode(name='Irritable'),
 EmotionNode(name='Annoyed'),
...
```

### Primary emotions

<!-- TODO: Insert image with pointer to primary level -->

IMAGE

Retrieve all primary emotions (i.e., first level of the wheel):

```python
>>> wheel.primary_emotions()
(EmotionNode(name='Anger'),
 EmotionNode(name='Sadness'),
 EmotionNode(name='Surprise'),
 EmotionNode(name='Joy'),
 EmotionNode(name='Love'),
 EmotionNode(name='Fear'))
```

### Secondary emotions

<!-- TODO: Insert image with pointer to primary level -->

IMAGE

Retrieve all secondary eotions (i.e., second level of the wheel):

```python
>>> wheel.secondary_emotions()
(EmotionNode(name='Rage'),
 EmotionNode(name='Exasperated'),
 EmotionNode(name='Irritable'),
 EmotionNode(name='Envy'),
 EmotionNode(name='Disgust'),
 EmotionNode(name='Suffering'),
...
```

### Tertiary emotions

<!-- TODO: Insert image with pointer to primary level -->

IMAGE

Retrieve all tertiery emotions (i.e., third and final level of the wheel):

```python
>>> wheel.tertiary_emotions()
(EmotionNode(name='Hate'),
 EmotionNode(name='Hostile'),
 EmotionNode(name='Agitated'),
 EmotionNode(name='Frustrated'),
 EmotionNode(name='Annoyed'),
...
```

### Find a specific emotion

You can lookup a specific emotion in the wheel by supplying the `name` of the emotion:

```python
>>> wheel.find_emotion("excited")
EmotionNode(name='Excited')
```

<!-- TODO: Section - Project: Building a mini-personal therapist -->

## License

`pyemotionwheel` is released under the MIT License. This means it is free to use, modify, and distribute, including for commercial use, provided the license and copyright notice are preserved.

**Note**: Always remember to adhere to the MIT License when using or modifying `pyemotionwheel`.
