# import the necessary packages
from anytree import RenderTree
from anytree import AnyNode
from pathlib import Path
import json

# define the path to the default emotion wheel JSON tree
base_dir = Path(__file__).resolve().parent
DEFAULT_EMO_WHEEL_PATH = base_dir / "emotion_wheel_tree.json"


class EmotionWheel:

    def __init__(self, emo_wheel_path=DEFAULT_EMO_WHEEL_PATH):
        # load the contents of the emotion wheel, then build the tree
        data = json.loads(open(emo_wheel_path).read())
        self.root = self.build_tree(data)

    def build_tree(self, data, parent=None):
        # instantiate the node
        node = AnyNode(name=data["name"], parent=parent)

        # loop over any children of the node
        for child_data in data.get("children", []):
            # recursively build the tree
            self.build_tree(child_data, node)

        # return the node
        return node

    def __str__(self):
        # return a string representation of the rendered tree
        return str(RenderTree(self.root))
