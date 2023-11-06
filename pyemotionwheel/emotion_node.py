# import the necessary packages
from anytree import AnyNode


class EmotionNode(AnyNode):
    """
    A class representing a node in an EmotionTree, extending the AnyNode
    class.

    This node is used to represent an emotion in a hierarchical structure,
    with the possibility of having parent-child relationships to represent
    complex emotional compositions.

    Attributes:
        name (str): The human-readable name of the emotion.
    """

    # provide a type hint for the name of the node
    name: str

    def __init__(self, **kwargs):
        """
        Initializes a new instance of EmotionNode.

        This constructor initializes the EmotionNode with the provided keyword
        arguments. The `name` of the node (i.e., the human-readable name of
        the emotion) is expected to be among the `kwargs`.

        Args:
            **kwargs: Arbitrary keyword arguments. The `name` keyword is
                expected to be in this list of arguments.
        """
        # call the parent constructor
        super().__init__(**kwargs)

    def __str__(self):
        """
        Return the human-readable string representation of the EmotionNode.

        The string representation of an EmotionNode is its name (i.e., amused,
        delighted, angry, agitated, etc.).

        Returns:
            str: The name of the emotion.
        """
        # return the name of the emotion as the string representation
        return self.name
