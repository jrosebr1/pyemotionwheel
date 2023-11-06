# pyemotionwheel

![Basic emotion wheel](assets/emotion_wheel.png)

`pyemotionwheel` is a Python library that provides a programmatic interface to an emotion wheel, a simple psychological tool for identifying and articulating emotions.

The library models an emotion wheel as a hierarchical tree structure, with primary emotions at its core and more nuanced secondary and tertiary emotions branching out.

This tool can be especially beneficial in therapeutic settings, educational environments, and personal development for enhancing emotional intelligence.

## Why does pyemotionwheel exist?

In the realm of psychology, identifying and articulating emotions is an essential step towards understanding and managing them effectively.

**My bond with the emotion wheel is also _deeply personal._**

Surviving a near-fatal car accident at 13 years old, combined with growing up in a broken home, led to my emotions shutting down to cope with the trauma and ensuing family turmoil.

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

Here's how to utilize each of the public methods in the `EmotionWheel` class, along with a few common use patterns.

### Instantiate the emotion wheel

Instantiate an instance of the emotion wheel, then show the tree structure:

```python
>> > from pyemotionwheel import BasicEmotionWheel
>> > wheel = BasicEmotionWheel()
>> > print(wheel)
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
│   │   └── Awe - struck
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

### Get the path of an EmotionNode back to the root

We can better understand the composition of an emotion by tracing it back to its root:

```python
>>> compassionate = wheel.find_emotion("Compassionate")
>>> compassionate.path[::-1]
(EmotionNode(name='Compassionate'),
 EmotionNode(name='Tenderness'),
 EmotionNode(name='Love'),
 EmotionNode(name='root'))
```

The tertiary emotion, _"Compassionate"_, consists of _"Tenderness"_ as the secondary emotion, and finally _"Love"_ as the primary emotion.

### Get all children of an EmotionNode

To understand how a parent emotion can be decomposed into its potential child emotions, we can inspect the `children` of a given `EmotionNode`:

```python
>>> nervous = wheel.find_emotion("Nervous")
>>> nervous.children
(EmotionNode(name='Worried'), EmotionNode(name='Anxious'))
```

The _"Nervous"_ secondary emotion has two associated tertiary emotions: _"Worried"_ and _"Anxious"_.

## Future work

- Create a sunburst-like visualization for the `BasicEmotionWheel` class. Something similar to [plotly's implementation](https://plotly.com/python/sunburst-charts/) would be great, but maybe use matplotlib instead?
- Implement a `PlutchikEmotionWheel` class, based on the work of [Robert Plutchik](https://en.wikipedia.org/wiki/Robert_Plutchik). [@alfonsosemeraro](https://github.com/alfonsosemeraro) has a [fantastic implementation](https://github.com/alfonsosemeraro/pyplutchik) that can likely be extended for my particular uses.

## License

`pyemotionwheel` is released under the MIT License. This means it is free to use, modify, and distribute, including for commercial use, provided the license and copyright notice are preserved.
