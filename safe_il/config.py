import argparse


class AttrDict(dict):
    """Convert loaded Yaml dictionary into to attribute dictionary for
    dot-notation access"""
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self


def get_base_parser():
    """Argument parser to load most basic training configuration"""
    parser = argparse.ArgumentParser(
        description='Description')

    # Util
    parser.add_argument('-c', '--config',
                        type=str,
                        default='',
                        help='Predefined config')

    parser.add_argument('-r', '--resume',
                        type=str,
                        default='',
                        help='Path to checkpoint directory (must be valid \
                        PyTorch full checkpoint, with optimizer/loss/epochs \
                        also saved) (default = Empty).')

    parser.add_argument('-d', '--data_dir',
                        type=str,
                        required=True,
                        help='Path to data directory.')

    # Logging
    parser.add_argument('--log_dir',
                        type=str,
                        default='logs/',
                        help='Path to log directory.')

    parser.add_argument('--exp_name',
                        type=str,
                        default='safeq',
                        help='Name to use for prefix.')

    parser.add_argument('--model_name',
                        type=str,
                        default='model',
                        help='Name to use when saving model .pth file.')

    parser.add_argument('--tag',
                        type=str,
                        default='basic',
                        help='Name to use when saving model .pth file.')

    parser.add_argument('--eval_interval',
                        type=int,
                        default=5,
                        help='How many epochs before evaluating')

    # HyperParameters
    parser.add_argument('--seed', type=int, default=523, help='Seed for RNG.')

    parser.add_argument('--epochs',
                        type=int,
                        default=500,
                        help='Total number of epochs.')

    parser.add_argument('--batch_size',
                        type=int,
                        default=64,
                        help='Batch Size')

    return parser


def get_plot_parser():
    """Argument parser to load model to plot visuals"""
    parser = argparse.ArgumentParser(
        description='Plotting')

    parser.add_argument('--log_dir',
                        type=str,
                        default='logs/',
                        required=True,
                        help='Path to log directory.')

    parser.add_argument('--filename',
                        type=str,
                        default='fig.png',
                        help='Filename to save as')

    return parser
