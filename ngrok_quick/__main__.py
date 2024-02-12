import logging
import sys

import click
import ngrok

from time import sleep

logger = logging.getLogger(__name__)


@click.group()
@click.version_option(message='%(version)s')
def cli():
    logging.basicConfig(level=logging.INFO)


@cli.command(name='run', short_help='Run the listener')
def run():
    """Run the ngrok listener and forward to the specified address."""
    from . import main
    try:
        main()
    except Exception as e:
        logger.error('%s: %s', e.__class__.__name__, e)
        sys.exit(1)

    try:
        while True:
            sleep(60)
    except KeyboardInterrupt:
        pass

    ngrok.disconnect()
    sys.exit(0)


if __name__ == '__main__':
    cli()
