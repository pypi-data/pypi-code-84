class Node:
    def __init__(self):
        self.data = 0
        self.next = None

# Function to get the intersection point
# of the given linked lists
def getIntersectionNode( head1, head2):

    curr1 = head1
    curr2 = head2

    # While both the pointers are not equal
    while (curr1 != curr2):

        # If the first pointer is None then
        # set it to point to the head of
        # the second linked list
        if (curr1 == None) :
            curr1 = head2

            # Else point it to the next node
        else:
            curr1 = curr1.next

        # If the second pointer is None then
        # set it to point to the head of
        # the first linked list
        if (curr2 == None):
            curr2 = head1

            # Else point it to the next node
        else:
            curr2 = curr2.next

    # Return the intersection node
    return curr1.data