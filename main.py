import yaml
import argparse
import pdb

def get_parser(description, config_name="config.yaml"):
    """
    A function to create parser given default configurations from yaml.
    :param description: description txt to give to argparse
    :param config_name: name of the configuration file
    :return parser: argparse parser
    """
    parser = argparse.ArgumentParser(description=description)
    # Read configuration file for defaults
    parser.add_argument('-c', '--config', type=argparse.FileType(mode='r'), default=config_name)
    # If specified through command line, going to overwrite
    parser.add_argument('-bs', '--batch_size', type=int)
    parser.add_argument('-ne', '--num_epochs', type=int)
    parser.add_argument('-lr', '--learning_rate', type=float)
    parser.add_argument('-mt', '--model_type', type=str)

    return parser

def get_args(parser):
    """
    A function to create args given default values from config file and overwrite if necessary.
    :param parser: argparse parser containing configuration file and command line input
    :return args: arguments
    """
    args = parser.parse_args()
    # Make sure the config exists
    if args.config:
        # Load the default configurations from the yaml file
        defaults = yaml.load(args.config)
        # No need for config argument now, delete
        delattr(args, 'config')
        # Create a dictionary of command line specified arguments
        commandline = args.__dict__
        # Use the default if it's not specified through command line
        for key, value in defaults.items():
            # If the key in yaml exists in commandline
            if key in commandline:
                # But not specified, then use the default
                if commandline[key] is None:
                    commandline[key] = value

    return args


if __name__ == '__main__':
    parser = get_parser("Testing argparse yaml overwrite.", "config.yaml")
    args = get_args(parser)
    print(args)
