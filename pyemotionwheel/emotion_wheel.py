# import the necessary packages
from .emotion_node import EmotionNode
from anytree import LevelOrderGroupIter
from anytree import RenderTree
from anytree import search
import pathlib
import json

# define the path to the default emotion wheel JSON tree
base_dir = pathlib.Path(__file__).resolve().parent
DEFAULT_EMO_WHEEL_PATH = base_dir / "emotion_wheel_tree.json"


class EmotionWheel:

    def __init__(self, emo_wheel_path=DEFAULT_EMO_WHEEL_PATH):
        # load the contents of the emotion wheel, then build the tree
        data = json.loads(open(emo_wheel_path).read())
        self.root = self._build_tree(data)

    def all_emotions(self):
        # return all emotion nodes in the tree
        return self.root.descendants

    def primary_emotions(self):
        # all primary emotions are at level one of the tree
        return self._get_nodes_at_level(1)

    def secondary_emotions(self):
        # the secondary emotions are located at level two of the tree
        return self._get_nodes_at_level(2)

    def tertiary_emotions(self):
        # all tertiary emotions are at level three
        return self._get_nodes_at_level(3)

    def find_emotion(self, emotion):
        # search the tree to find the supplied emotion
        return search.find_by_attr(self.root, name="name", value=emotion)

    def _get_nodes_at_level(self, level):
        # loop over all levels of the tree
        for (i, children) in enumerate(LevelOrderGroupIter(self.root)):
            # check to see if the current level of the iterator matches our
            # desired level
            if i == level:
                # return all nodes at this level
                return children

    def _build_tree(self, data, parent=None):
        # instantiate the emotion node
        node = EmotionNode(name=data["name"], parent=parent)

        # loop over any children of the node
        for child_data in data.get("children", []):
            # recursively build the tree
            self._build_tree(child_data, node)

        # return the node
        return node

    def __str__(self):
        # create a string representation for each node in the tree
        lines = ["{}{}".format(pre, str(node))
                 for (pre, _, node) in RenderTree(self.root)]

        # take the lines and join them into the final tree representation
        return "\n".join(lines)
