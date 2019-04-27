from argparse import ArgumentParser
# The below try/except is only to satisfy Submitty: Submitty seems to
# uninstall the package before running pytest, the former import doesn't
# work when the test is running. The latter doesn't work with Submitty's
# own test of the 'abracadabra' entry point. Worth noting the latter works
# fine for install and pytest on my system.
try:
    from alchemist.laboratory import Laboratory
except:
    from laboratory import Laboratory
import yaml


def process():
    parser = ArgumentParser(description=
                            "Show results of reactions / number of reactions")
    parser.add_argument('laboratory')
    parser.add_argument('--reactions', '-r', action="store_true")
    arguments = parser.parse_args()
    if arguments.laboratory:
        with open(arguments.laboratory, "r") as data:
            shelves = yaml.load(data)
        mylab = Laboratory(shelves["lower"], shelves["upper"])
        count = mylab.run_full_experiment()
        if arguments.reactions:
            print(count)
        else:
            print("lower: {} \nupper: {}".format(mylab.lower_shelf,
                  mylab.upper_shelf))

if __name__ == "__main__":
    process()
