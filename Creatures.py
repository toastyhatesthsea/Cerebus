# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Creature(object):

    def __init__(self):
        raise NotImplementedError("Abstract classes should not be instantiated")

    def __str__(self) -> str:
        raise NotImplementedError("Abstract class methods should not be called")

    def search(self, value: str) -> bool:
        raise NotImplementedError("Abstract class methods should not be called")


class Orthrus(Creature):

    def __init__(self, a_left: Creature, a_right: Creature):
        '''Left or right can be another Orthrus object or Cerebus object or a Head creature object
        or even Empty'''
        self.left = a_left
        self.right = a_right

    def __str__(self) -> str:
        if self.left == None and self.right == None:  # Return empty String is Orthrus Object has no left or right object
            return ""
        else:
            left = ""  # Default left and right strings are empty
            right = ""

            if self.left != None:  # If Left node is not empty, go left
                left = self.left.__str__()
            if self.right != None:  # If Right node is not empty, go right
                right = self.right.__str__()

            return left + " " + right  # Combine the strings and return

    def search(self, value: str) -> bool:
        if (self.left == None and self.right == None):
            # If Orthrus Object contains nothing in Left and Right nodes
            return False
        else:
            left_value = False
            right_value = False
            if self.left != None:
                left_value = self.left.search(value)
            if self.right != None:
                right_value = self.right.search(value)

        return left_value | right_value  # If left or right values are true, return True. Otherwise, return False


class Cerberus(Creature):

    def __init__(self, a_left: Creature, a_middle: Creature, a_right: Creature):
        '''Left or Right or Middle; can be another Orthrus or Cerebus or a Head creature or even Empty'''
        self.left = a_left
        self.middle = a_middle
        self.right = a_right

    def __str__(self) -> str:
        if self.left == None and self.middle == None and self.right == None:
            # Return empty String if Cerebus Object has no left or middle or right object
            return ""
        else:
            left = ""  # Default left, middle and right strings are empty
            middle = ""
            right = ""

            if self.left != None:  # If Left node is not empty
                left = self.left.__str__()
            if self.middle != None:  # If Middle node is not empty
                middle = self.middle.__str__()
            if self.right != None:  # If Right node is not empty
                right = self.right.__str__()

            return left + " " + middle + " " + right  # Combine strings and return

    def search(self, value: str) -> bool:
        if (self.left == None and self.middle == None and self.right == None):
            # If Cerebus Object contains no objects in left, middle, right nodes
            return False
        else:

            left_value = False  # Default Value
            middle_value = False  # Default Value
            right_value = False  # Default Value

            if self.left != None:  # Search left node if not empty
                left_value = self.left.search(value)
            if self.middle != None:  # Search middle node if not empty
                middle_value = self.middle.search(value)
            if self.right != None:  # Search right node if not empty
                right_value = self.right.search(value)

            # If left or middle or right values are true, return True. Otherwise, return False
            return left_value | middle_value | right_value


class Head(Creature):

    def __init__(self, a_name: str):
        self.name = a_name

    def __str__(self) -> str:
        return str(self.name)  # Head has no left or right or middle, simply return the name

    def search(self, value: str) -> bool:
        if value == self.name:
            return True
        else:
            return False


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def main():
    doggy1 = Head("Kane")
    doggy2 = Head("Wolfie")
    doggy3 = Head("Rugal")
    doggy4 = Head("Taker")
    ort1 = Orthrus(doggy1, doggy2)
    ort2 = Orthrus(doggy3, Head("Jeff"))
    cer = Cerberus(ort1, doggy4, ort2)
    cer4 = Cerberus(Orthrus(Head("Starship"), Head("EvilCat")), Head("Treesap"), Head("Butterfly"))
    cer2 = Cerberus(ort1, Head("rawrs"), Orthrus(Head("Lyra"), Head("LovelyLamp")))
    cer3 = Cerberus(ort1, Head("rawrs"), Orthrus(Head("Lyra"), cer))
    cer5 = Cerberus(ort1, Head("rawrs"), Orthrus(None, None))

    print(cer)
    print(cer2)
    print(cer3)
    print(cer5)
    print(cer.search("Drogon"))
    print(cer.search("Rugal"))
    print(cer3.search("Lyra"))
    print(cer4.search("EvilCat"))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Meowmix')
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
