import random


class Laboratory:
    """ Two lists of strings representing lower and upper shelves of a
    Laboratory, with methods to conduct reactions.

    Attributes
    ----------
    lower_shelf: list(array(string))
        Lower shelf of the lab, substances are selected in order of index
    upper_shelf: list(array(string))
        Upper shelf of the lab, substances are selected randomly

    Methods
    -------
    can_react(substance1, substance2)
        Test if two substances can react.
    update_shelves(substance1, substance2_index)
        Return updated shelves by removing substances that have reacted.
    do_a_reaction()
        Conduct a reaction with the first possible substance on lower shelf
    run_full_experiement()
        Modifies the class instance on which the method is applied
        by completing all possible reactions.
    """

    def __init__(self, lower_shelf=[], upper_shelf=[]):
        """ Inits Laboratory with lower_shelf and upper_shelf arguments
        """

        self.lower_shelf = lower_shelf
        self.upper_shelf = upper_shelf

    def can_react(self, substance1, substance2):
        """ Tests if two substances can react.

        Parameters
        ----------
        substance1: str
            Name of a substance, with "anti" suffix or not
        substance2: str
            Name of a substance, with "anti" suffix or not

        Returns
        -------
        boolean
            True if the substances can react, False otherwise
        """

        return ((substance1 == "anti" + substance2)
                or (substance2 == "anti" + substance1))

    def update_shelves(self, substance1, substance2_index):
        """ Updates shelves of the lab instances by removing substances
        passed in argument, one from each shelf. Index for upper shelf is
        required as selection on that shelf is done randomly.

        Parameters
        ----------
        substance1: str
            Name of a substance on the lower shelf, with "anti" suffix or not
        subtance2_index: int
            Index of a substance on the upper shelf

        Return
        ------
        None
        """

        index1 = self.lower_shelf.index(substance1)
        self.lower_shelf = (self.lower_shelf[:index1]
                            + self.lower_shelf[index1+1:])
        self.upper_shelf = (self.upper_shelf[:substance2_index]
                            + self.upper_shelf[substance2_index+1:])
        return

    def do_a_reaction(self):
        """ Conducts a reaction with the first possible substance from
        the lower shelf, and a random substance from the upper shelf
        that can react. This methods updates the class instance.

        Return
        ------
        boolean
            True if a reaction has happened, False otherwise.
        """

        for substance1 in self.lower_shelf:
            possible_targets = ([i for i, target in enumerate(self.upper_shelf)
                                if self.can_react(substance1, target)])
            if not possible_targets:
                continue
            else:
                substance2_index = random.choice(possible_targets)
                self.update_shelves(substance1, substance2_index)
                return True
        return False

    def run_full_experiment(self):
        """ Modifies the class instance on which the method is applied
        by completing all possible reactions.

        Return
        ------
        int
            Count of number of reactions completed.
        """

        count = 0
        while self.do_a_reaction():
            count += 1
        return count
