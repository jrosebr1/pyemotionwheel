# pyemotionwheel

![Basic emotion wheel](assets/emotion_wheel.png)

`pyemotionwheel` is a Python library that provides a programmatic interface to an emotion wheel, a simple psychological tool for identifying and articulating emotions.

The library models an emotion wheel as a hierarchical tree structure, with primary emotions at its core and more nuanced secondary and tertiary emotions branching out.

This tool can be especially beneficial in therapeutic settings, educational environments, and personal development for enhancing emotional intelligence.

<!-- TODO: Generate table of contents -->

## Why does pyemotionwheel exist?

In the realm of psychology, identifying and articulating emotions is an essential step towards understanding and managing them effectively.

**My bond with the emotion wheel is also _deeply personal._**

Surviving a near-death car accident at 13 years old, combined with growing up in a broken home, led to my emotions shutting down to cope with the trauma and ensuing family turmoil.

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

## Building an AI therapist to help with emotional intelligence

As a practical use case of the `pyemotionwheel` package, let's discover how to build a simple AI-assisted therapist who specializes in emotional intelligence.

Our AI therapist will accept an input journal entry, analyze the emotions, and then provide us with practical tools to deepen and move through our feelings.

### Configuring OpenAI

We'll be using OpenAI for this example, so let's be sure to import the required packages (you may also need to install [openai](https://github.com/openai/openai-python) if it's not already on your system):

```python
import openai
import json

openai.api_key = "..."
```

### Using AI to recognize emotions in a journal entry

First, let's create a prompt to recognize emotions in a journal entry:

```python
identify_emotions_prompt_template = """
Act as an expert psychologist who specializes in emotional intelligence.

Your job is to analyze my << JOURNAL ENTRY >> and identify which << EMOTIONS >> are present. These emotions come from my emotion wheel. Any emotions you identify MUST come the << EMOTIONS >> list. If you identify an emotion that is NOT present in the emotion list, use the most similar emotion from the list.

Omit any pre and post-text in your response. Format your response as a JSON list using the << JSON TEMPLATE >>.

<< JOURNAL ENTRY >>
{journal_entry}

<< EMOTIONS >>
{emotion_list}

<< JSON TEMPLATE >>
{
	"emotions": []
}
"""
```

We then have our `journal_entry` string:

``` python
journal_entry = """
Tuesday, November 6th

It's like the whole world just flipped into grayscale. She broke up with me. Right there in the cafeteria, with the buzz of a hundred conversations around us. It felt like someone sucked all the air out of the room. I could barely hear her over the noise in my head, the kind of noise that doesn't have a sound but still screams at you.

I don't get it. Yesterday, we were talking about the band's new song, and she was looking at me with those eyes that made me feel like I was actually somebody. Today, she's handing me back my hoodie like it's some kind of contaminated evidence.

I went through the rest of the day like a ghost. I couldn't focus on the teachers, the lessons, or the homework. It was all just a blur. I kept replaying that moment over and over, looking for some sign, something I missed. Did I say something? Did I not say something? It's like trying to find a piece in a puzzle that just doesn't fit anywhere.

The worst part? The pity looks. Everyone knows. They whisper and steal glances like I'm on display in some twisted museum of heartbreak. I wanted to scream, to tell them all to just shut up, but what's the point? They wouldn't get it. They don't know what it's like to feel everything so deeply that it's like drowning, but instead of fighting for air, you just want to sink.

I can't even escape into music tonight. Every lyric seems like it's mocking me, every chord is a reminder of her. I tried writing something, anything. All that came out were scribbles and scratched-out lines that looked more like the ravings of a madman than any kind of poetry or song.

Mom knocked on my door earlier, asked if I'm okay. I told her I'm fine, just tired. I'm not fine. I'm so far from fine it's like I'm on a different planet. And I'm tired, but not the kind of tired sleep can fix. I'm tired in my bones, in my soul.

I don't know what to do with all this... this rage, this sadness, this... emptiness. She was a part of my day, every day, and now there's just this hole where she used to be. It's like someone carved out a piece of me, and I'm just supposed to go on like everything's normal.

But it's not. Nothing's normal. And the worst part is, tomorrow, I have to get up and do it all over again. Walk the same halls, see the same faces, and pretend like I didn't just get ripped in half.

For now, I'll just sit here in the dark, with my guitar lying next to me, unplayed. Maybe sleep will come, maybe it won't. Maybe I'll wake up and this will all just be some bad dream.

But who am I kidding? This is real, and it's not going anywhere. And neither am I.
"""
```

Note that the above journal entry was generated by ChatGPT using the following prompt:

> Act as an angsty emo teenager who's girlfriend just broke up with him at lunch. Write his journal entry that evening.

Not that ever happened to me or anything...

The final step before submitting the prompt to OpenAI is to fill in the `{journal_entry}` and `{emotion_list}` variables:

```python
emotions_list = [str(e) for e in wheel.all_emotions()]
prompt = identify_emotions_prompt_template.replace(
    "{journal_entry}", journal_entry)
prompt = prompt.replace("{emotion_list}", ",".join(emotions_list))
print(prompt)
```

Note how the `{emotion_list}` is a call to `wheel.all_emotions()`, which returns _all_ emotions from the emotion wheel.

Here is the resulting prompt:

```
Act as an expert psychologist who specializes in emotional intelligence.

Your job is to analyze my << JOURNAL ENTRY >> and identify which << EMOTIONS >> are present. These emotions come from my emotion wheel. Any emotions you identify MUST come the << EMOTIONS >> list. If you identify an emotion that is NOT present in the emotion list, use the most similar emotion from the list.

Omit any pre and post-text in your response. Format your response as a JSON list using the << JSON TEMPLATE >>.

<< JOURNAL ENTRY >>

Tuesday, November 6th

It's like the whole world just flipped into grayscale. She broke up with me. Right there in the cafeteria, with the buzz of a hundred conversations around us. It felt like someone sucked all the air out of the room. I could barely hear her over the noise in my head, the kind of noise that doesn't have a sound but still screams at you.

I don't get it. Yesterday, we were talking about the band's new song, and she was looking at me with those eyes that made me feel like I was actually somebody. Today, she's handing me back my hoodie like it's some kind of contaminated evidence.

I went through the rest of the day like a ghost. I couldn't focus on the teachers, the lessons, or the homework. It was all just a blur. I kept replaying that moment over and over, looking for some sign, something I missed. Did I say something? Did I not say something? It's like trying to find a piece in a puzzle that just doesn't fit anywhere.

The worst part? The pity looks. Everyone knows. They whisper and steal glances like I'm on display in some twisted museum of heartbreak. I wanted to scream, to tell them all to just shut up, but what's the point? They wouldn't get it. They don't know what it's like to feel everything so deeply that it's like drowning, but instead of fighting for air, you just want to sink.

I can't even escape into music tonight. Every lyric seems like it's mocking me, every chord is a reminder of her. I tried writing something, anything. All that came out were scribbles and scratched-out lines that looked more like the ravings of a madman than any kind of poetry or song.

Mom knocked on my door earlier, asked if I'm okay. I told her I'm fine, just tired. I'm not fine. I'm so far from fine it's like I'm on a different planet. And I'm tired, but not the kind of tired sleep can fix. I'm tired in my bones, in my soul.

I don't know what to do with all this... this rage, this sadness, this... emptiness. She was a part of my day, every day, and now there's just this hole where she used to be. It's like someone carved out a piece of me, and I'm just supposed to go on like everything's normal.

But it's not. Nothing's normal. And the worst part is, tomorrow, I have to get up and do it all over again. Walk the same halls, see the same faces, and pretend like I didn't just get ripped in half.

For now, I'll just sit here in the dark, with my guitar lying next to me, unplayed. Maybe sleep will come, maybe it won't. Maybe I'll wake up and this will all just be some bad dream.

But who am I kidding? This is real, and it's not going anywhere. And neither am I.


<< EMOTIONS >>
Anger,Rage,Hate,Hostile,Exasperated,Agitated,Frustrated,Irritable,Annoyed,Aggravated,Envy,Resentful,Jealous,Disgust,Contempt,Revolted,Sadness,Suffering,Agony,Hurt,Despondent,Depression,Sorrow,Disappointed,Dismayed,Displeased,Shameful,Regretful,Guilty,Neglected,Isolated,Lonely,Despair,Grief,Powerless,Surprise,Stunned,Shocked,Dismayed,Confused,Disillusioned,Perplexed,Amazed,Astonished,Awe-struck,Overcome,Speechless,Astounded,Moved,Stimulated,Touched,Joy,Content,Pleased,Satisfied,Happy,Amused,Delighted,Cheerful,Jovial,Blissful,Proud,Triumphant,Illustrious,Optimistic,Eager,Hopeful,Enthusiastic,Excited,Zeal,Elation,Euphoric,Jubilation,Enthralled,Enchanted,Rapture,Love,Affectionate,Fondness,Romantic,Longing,Sentimental,Attracted,Desire,Passion,Infatuation,Tenderness,Caring,Compassionate,Peaceful,Relieved,Satisfied,Fear,Scared,Frightened,Helpless,Terror,Panic,Hysterical,Insecure,Inferior,Inadequate,Nervous,Worried,Anxious,Horror,Mortified,Dread

<< JSON TEMPLATE >>
{
	"emotions": []
}
```

Finally, this we submit the prompt to OpenAI to recognize emotions in the journal entry:

```python
completion = openai.ChatCompletion.create(
    model="gpt-4",
    temperature=0.7,
    messages=[{
        "role": "user",
        "content": prompt
    }]
)
blob = json.loads(completion.choices[0].message.content)
identified_emotions = blob["emotions"]
identified_emotions
```

The `identified_emotions` now includes:

```json
['Sadness',
 'Suffering',
 'Agony',
 'Hurt',
 'Despondent',
 'Depression',
 'Sorrow',
 'Disappointed',
 'Despair',
 'Grief',
 'Powerless',
 'Confused',
 'Disillusioned',
 'Isolated',
 'Lonely',
 'Rage',
 'Frustrated',
 'Annoyed']
```

We now have a list of all emotions identified from the journal entry.

### Using pyemotionwheel to provide context to our AI therapist

At this point, we have a list of emotions identified in the journal.

The next step is to augment these emotions with both:

1. The path from the emotion back to the root
2. The children nodes of the emotion

Once we have this information we can construct a prompt that asks our AI therapist to help us work through our emotions.

Let's get started by extracting the emotion path and children nodes, and inserting them into a dictionary:

```python
emotion_hierarchies = {}

for emotion_name in identified_emotions:
    emotion = wheel.find_emotion(emotion_name)
    emotion_hierarchies[emotion_name] = {
        "path": [str(e) for e in emotion.path[::-1]],
        "children": [str(e) for e in emotion.children],
    }
```

If we inspect the `emotion_hierarchies` dictionary, it will look like:

```python
{'Sadness': {'path': ['Sadness', 'root'],
  'children': ['Suffering',
   'Despondent',
   'Disappointed',
   'Shameful',
   'Neglected',
   'Despair']},
 'Suffering': {'path': ['Suffering', 'Sadness', 'root'],
  'children': ['Agony', 'Hurt']},
 'Agony': {'path': ['Agony', 'Suffering', 'Sadness', 'root'], 'children': []},
 'Hurt': {'path': ['Hurt', 'Suffering', 'Sadness', 'root'], 'children': []},
 'Despondent': {'path': ['Despondent', 'Sadness', 'root'],
  'children': ['Depression', 'Sorrow']},
 'Depression': {'path': ['Depression', 'Despondent', 'Sadness', 'root'],
  'children': []},
 'Sorrow': {'path': ['Sorrow', 'Despondent', 'Sadness', 'root'],
  'children': []},
 'Disappointed': {'path': ['Disappointed', 'Sadness', 'root'],
  'children': ['Dismayed', 'Displeased']},
 'Despair': {'path': ['Despair', 'Sadness', 'root'],
  'children': ['Grief', 'Powerless']},
 'Grief': {'path': ['Grief', 'Despair', 'Sadness', 'root'], 'children': []},
 'Powerless': {'path': ['Powerless', 'Despair', 'Sadness', 'root'],
  'children': []},
 'Confused': {'path': ['Confused', 'Surprise', 'root'],
  'children': ['Disillusioned', 'Perplexed']},
 'Disillusioned': {'path': ['Disillusioned', 'Confused', 'Surprise', 'root'],
  'children': []},
 'Isolated': {'path': ['Isolated', 'Neglected', 'Sadness', 'root'],
  'children': []},
 'Lonely': {'path': ['Lonely', 'Neglected', 'Sadness', 'root'],
  'children': []},
 'Rage': {'path': ['Rage', 'Anger', 'root'], 'children': ['Hate', 'Hostile']},
 'Frustrated': {'path': ['Frustrated', 'Exasperated', 'Anger', 'root'],
  'children': []},
 'Annoyed': {'path': ['Annoyed', 'Irritable', 'Anger', 'root'],
  'children': []}}
```

### Prompting our AI therapist to help us work through our emotions

Given our `emotion_hierarchies`, let's see how oru AI therapist can help us deepen our emotional intelligence.

To start, let's create an emotional intelligence prompt:

```python
eq_prompt_template = """
Below I have included the emotion wheel hierarchy for each of the << IDENTIFIED EMOTIONS >> in my << JOURNAL ENTRY >>.

Using your expert knowledge as a psychologist and therapist to help me:

1. Use emotional intelligence to trace my emotions back to the root
2. Deepen my emotions and move through the children nodes, ideally finding release in the depening

Be specific in your advice, and show your thinking step-by-step. Use the tone and style of an empathetic, caring therapist.

Format your response as Markdown, omitting any pre or post text.

<< JOURNAL ENTRY >>
{journal_entry}

<< IDENTIFIED EMOTIONS >>
{identified_emotions}
"""
```

We'll then fill in the prompt:

```python
prompt = eq_prompt_template.replace("{journal_entry}", journal_entry)
prompt = prompt.replace("{identified_emotions}",
                        json.dumps(emotion_hierarchies))
```

The resulting `prompt` now looks like:

```
Below I have included the emotion wheel hierarchy for each of the << IDENTIFIED EMOTIONS >> in my << JOURNAL ENTRY >>.

Using your expert knowledge as a psychologist and therapist to help me:

1. Use emotional intelligence to trace my emotions back to the root
2. Deepen my emotions and move through the children nodes, ideally finding release in the depening

Be specific in your advice, and show your thinking step-by-step. Use the tone and style of an empathetic, caring therapist.

Format your response as Markdown, omitting any pre or post text.

<< JOURNAL ENTRY >>

Tuesday, November 6th

It's like the whole world just flipped into grayscale. She broke up with me. Right there in the cafeteria, with the buzz of a hundred conversations around us. It felt like someone sucked all the air out of the room. I could barely hear her over the noise in my head, the kind of noise that doesn't have a sound but still screams at you.

I don't get it. Yesterday, we were talking about the band's new song, and she was looking at me with those eyes that made me feel like I was actually somebody. Today, she's handing me back my hoodie like it's some kind of contaminated evidence.

I went through the rest of the day like a ghost. I couldn't focus on the teachers, the lessons, or the homework. It was all just a blur. I kept replaying that moment over and over, looking for some sign, something I missed. Did I say something? Did I not say something? It's like trying to find a piece in a puzzle that just doesn't fit anywhere.

The worst part? The pity looks. Everyone knows. They whisper and steal glances like I'm on display in some twisted museum of heartbreak. I wanted to scream, to tell them all to just shut up, but what's the point? They wouldn't get it. They don't know what it's like to feel everything so deeply that it's like drowning, but instead of fighting for air, you just want to sink.

I can't even escape into music tonight. Every lyric seems like it's mocking me, every chord is a reminder of her. I tried writing something, anything. All that came out were scribbles and scratched-out lines that looked more like the ravings of a madman than any kind of poetry or song.

Mom knocked on my door earlier, asked if I'm okay. I told her I'm fine, just tired. I'm not fine. I'm so far from fine it's like I'm on a different planet. And I'm tired, but not the kind of tired sleep can fix. I'm tired in my bones, in my soul.

I don't know what to do with all this... this rage, this sadness, this... emptiness. She was a part of my day, every day, and now there's just this hole where she used to be. It's like someone carved out a piece of me, and I'm just supposed to go on like everything's normal.

But it's not. Nothing's normal. And the worst part is, tomorrow, I have to get up and do it all over again. Walk the same halls, see the same faces, and pretend like I didn't just get ripped in half.

For now, I'll just sit here in the dark, with my guitar lying next to me, unplayed. Maybe sleep will come, maybe it won't. Maybe I'll wake up and this will all just be some bad dream.

But who am I kidding? This is real, and it's not going anywhere. And neither am I.


<< IDENTIFIED EMOTIONS >>
{"Sadness": {"path": ["Sadness", "root"], "children": ["Suffering", "Despondent", "Disappointed", "Shameful", "Neglected", "Despair"]}, "Suffering": {"path": ["Suffering", "Sadness", "root"], "children": ["Agony", "Hurt"]}, "Agony": {"path": ["Agony", "Suffering", "Sadness", "root"], "children": []}, "Hurt": {"path": ["Hurt", "Suffering", "Sadness", "root"], "children": []}, "Despondent": {"path": ["Despondent", "Sadness", "root"], "children": ["Depression", "Sorrow"]}, "Depression": {"path": ["Depression", "Despondent", "Sadness", "root"], "children": []}, "Sorrow": {"path": ["Sorrow", "Despondent", "Sadness", "root"], "children": []}, "Disappointed": {"path": ["Disappointed", "Sadness", "root"], "children": ["Dismayed", "Displeased"]}, "Despair": {"path": ["Despair", "Sadness", "root"], "children": ["Grief", "Powerless"]}, "Grief": {"path": ["Grief", "Despair", "Sadness", "root"], "children": []}, "Powerless": {"path": ["Powerless", "Despair", "Sadness", "root"], "children": []}, "Confused": {"path": ["Confused", "Surprise", "root"], "children": ["Disillusioned", "Perplexed"]}, "Disillusioned": {"path": ["Disillusioned", "Confused", "Surprise", "root"], "children": []}, "Isolated": {"path": ["Isolated", "Neglected", "Sadness", "root"], "children": []}, "Lonely": {"path": ["Lonely", "Neglected", "Sadness", "root"], "children": []}, "Rage": {"path": ["Rage", "Anger", "root"], "children": ["Hate", "Hostile"]}, "Frustrated": {"path": ["Frustrated", "Exasperated", "Anger", "root"], "children": []}, "Annoyed": {"path": ["Annoyed", "Irritable", "Anger", "root"], "children": []}}
```

The emotional intelligence prompt can now be submitted to OpenAI:

```python
completion = openai.ChatCompletion.create(
    model="gpt-4",
    temperature=0.7,
    messages=[{
        "role": "user",
        "content": prompt
    }]
)
response = completion.choices[0].message.content
```

Let's see what our AI therapist has to say:

```
# Understanding and Navigating Emotions

It's clear from your journal entry that you're going through a significant emotional upheaval. It's important to remember that all emotions, even the challenging ones, are valid and part of the human experience. Let's try to understand and navigate these emotions together, tracing them back to their roots and exploring their depths.

## Identifying the Root Emotions

Considering the emotions identified from your journal entry, we can see that your primary emotional experiences revolve around:
- **Sadness** 
- **Surprise**
- **Anger**

Sadness is the most prevalent, with several child emotions identified. This is understandable given the breakup you've experienced. The surprise seems to stem from the unexpectedness of the situation, and the anger could be a reaction to the perceived unfairness and frustration associated with it.

## Tracing Back to the Root

Let's trace these emotions back to their roots:

1. **Sadness**: Rooted in the pain of the breakup, the loss of the relationship, and the void left behind.
2. **Surprise**: Rooted in the unexpectedness of the breakup, the sudden change in your relationship status.
3. **Anger**: Rooted in the perceived unfairness of the situation, the abruptness of the change, and the lack of control over the situation.

## Deepening into Child Emotions

Next, let's deepen into the child emotions and explore them:

1. **Sadness**: You've expressed multiple child emotions of sadness such as suffering, despondent, disappointed, despair, and feeling neglected. It's important to allow yourself to feel these emotions and understand that it's okay to not be okay. 

   - For example, your feelings of **despair** might include grief and feeling powerless. You can try to address these by allowing yourself to grieve the loss of the relationship and accepting that certain things are beyond your control.

2. **Surprise**: You're feeling confused and disillusioned. This is a natural response to an unexpected event. Take some time to process what happened, and remember, it's okay to not have all the answers right now.

3. **Anger**: You've expressed feeling rage, frustration, and annoyance. These are strong emotions that can be challenging to manage. Try to channel this anger into something productive or calming, like writing music or spending time in nature.

## Finding Release

Finally, let's try to find a release for these emotions:

- **Expression**: Writing in your journal is a great start. You might also find it therapeutic to express your feelings through music, even if the songs are sad or angry at first.

- **Acceptance**: Acceptance doesn't mean that you're okay with what happened, but rather that you acknowledge your feelings and your current situation. This is the first step towards healing.

- **Self-Care**: Take care of your physical health. Eat well, exercise, and get enough sleep. Physical health greatly impacts emotional health.

- **Support**: Reach out to supportive friends or family members. You don't have to go through this alone. If you feel comfortable, you might also consider seeking guidance from a counselor or therapist.

Remember, it's okay to feel these emotions. Allow yourself to feel them, understand them, and then let them guide you towards healing.
```

Not bad given our super basic prompting!

Involving an expert psychologist to help rewrite the prompts would likely yield better advice from our AI therapist.

## License

`pyemotionwheel` is released under the MIT License. This means it is free to use, modify, and distribute, including for commercial use, provided the license and copyright notice are preserved.
