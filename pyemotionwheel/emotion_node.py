# import the necessary packages
from anytree import AnyNode


class EmotionNode(AnyNode):

    # provide a type hint for the name of the node
    name: str

    def __init__(self, **kwargs):
        # call teh parent constructor
        super().__init__(**kwargs)

    def __str__(self):
        # return the name of the emotion as the string representation
        return self.name
