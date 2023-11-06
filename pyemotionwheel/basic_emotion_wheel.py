# import the necessary packages
from .emotion_node import EmotionNode
from anytree import LevelOrderGroupIter
from anytree import RenderTree
from anytree import search
import pathlib
import json

# define the path to the default emotion wheel JSON tree
base_dir = pathlib.Path(__file__).resolve().parent
DEFAULT_EMO_WHEEL_PATH = base_dir / "data" / "emotion_wheel_tree.json"


class BasicEmotionWheel:
    """
    A class for building an interacting with an Emotion/Feeling Wheel, which
    is a hierarchical representation of emotions organized as a tree structure.

    The Emotion Wheel is initialized from the input JSON file that represents
    emotions with parent-child relationships.

    Attributes:
        root (EmotionNode): The root node of the emotion tree.
    """

    def __init__(self, emo_wheel_path=DEFAULT_EMO_WHEEL_PATH):
        """
        Initializes the EmotionWheel by loading the emotion wheel data from
        the specified JSON file, followed by building the tree itself.

        Args:
            emo_wheel_path (pathlib.Path, optional): The input file path to
                the emotion wheel JSON data. Defaults to the emotion wheel
                JSON file included with this package, but you can bring your
                own JSON file as long as you follow the hierarchical structure
                dictated by the original emotion_wheel_tree.json file.
        """
        # load the contents of the emotion wheel, then build the tree
        data = json.loads(open(emo_wheel_path).read())
        self.root = self._build_tree(data)

    def all_emotions(self):
        """
        Get all emotion nodes in the tree.

        Returns:
            list of EmotionNode: All descendant nodes of the root (i.e., all
                emotions in the tree).
        """
        # return all emotion nodes in the tree
        return self.root.descendants

    def primary_emotions(self):
        """
        Retrieve all primary emotions, which are located at the level one of
        the tree.

        Returns:
            list of EmotionNode: All nodes at level one of the tree (i.e.,
                primary emotions).
        """
        # all primary emotions are at level one of the tree
        return self._get_nodes_at_level(1)

    def secondary_emotions(self):
        """
        Retrieve all secondary emotions, which are located at the second level
        of the tree.

        Returns:
             list of EmotionNode: All nodes at level two of the tree (i.e.,
                secondary emotions).
        """
        # the secondary emotions are located at level two of the tree
        return self._get_nodes_at_level(2)

    def tertiary_emotions(self):
        """
        Retrieve all tertiary emotions, which are located at level three
        of the tree.

        Returns:
            list of EmotionNode: All nodes at level three of the tree (i.e.,
                tertiary emotions).
        """
        # all tertiary emotions are at level three
        return self._get_nodes_at_level(3)

    def find_emotion(self, emotion):
        """
        Search the tree to find the EmotionNode with the provided emotion.

        Args:
            emotion (str): The name of the emotion to find.

        Returns:
            EmotionNode: The node corresponding to the emotion if found,
                otherwise, returns None.
        """
        # search the tree to find the supplied emotion, capitalizing the first
        # letter of the emotion (since emotions in the tree are stored with
        # the first letter capitalized, and is thus case-sensitive)
        return search.find_by_attr(
            self.root,
            name="name",
            value=emotion.capitalize()
        )

    def _get_nodes_at_level(self, level):
        """
        Retrieves all nodes at a specified level of the tree.

        Args:
            level (int): The level of the tree, where 0 is the root.

        Returns:
            list of EmotionNode: All nodes at the specified level.
        """
        # loop over all levels of the tree
        for (i, children) in enumerate(LevelOrderGroupIter(self.root)):
            # check to see if the current level of the iterator matches our
            # desired level
            if i == level:
                # return all nodes at this level
                return children

    def _build_tree(self, data, parent=None):
        """
        Recursively builds the emotion tree from the provided data.

        Args:
            data (dict): The JSON data representing the emotion wheel
                hierarchy.
            parent (EmotionNode, optional): The parent node to which this
                node is attached.

        Returns:
            EmotionNode: The root node of the constructed emotion tree.
        """
        # instantiate the emotion node
        node = EmotionNode(name=data["name"], parent=parent)

        # loop over any children of the node
        for child_data in data.get("children", []):
            # recursively build the tree
            self._build_tree(child_data, node)

        # return the node
        return node

    def __str__(self):
        """
        Create a string representation for each node in the tree, and visualize
        the hierarchical structure of the emotion tree itself.

        Returns:
             str: A visual representation of the tree structure.
        """
        # create a string representation for each node in the tree
        lines = ["{}{}".format(pre, str(node))
                 for (pre, _, node) in RenderTree(self.root)]

        # take the lines and join them into the final tree representation
        return "\n".join(lines)
