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

    return parser

def get_args(parser):
    """
    A function to create args given default values from config file and overwrite if necessary.
    :param parser: argparse parser containing configuration file for default values
    :return args: arguments updated by command line inputs
    """
    args, _ = parser.parse_known_args()
    # Make sure the config exists
    if args.config:
        # Load the default configurations from the yaml file
        defaults = yaml.load(args.config)
        # Unroll what's inside the yaml
        opt_args = [['--' + key] for key, _ in defaults.items()]
        opt_kwargs = [{'dest': key, 'type': type(value), 'default': value} for key, value in defaults.items()]
        # Put the unrolled arguments into parser
        for p_args, p_kwargs in zip(opt_args, opt_kwargs):
            parser.add_argument(*p_args, **p_kwargs)
        args = parser.parse_args()

    return args


if __name__ == '__main__':
    parser = get_parser("Testing argparse yaml overwrite.", "config.yaml")
    args = get_args(parser)
    print(args)
