import argparse
import logging.config
import discord

import database
from config import SeeBorg4Config
from seeborg4 import SeeBorg4

# Configure the logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)


def main():
    # Parse command-line arguments
    arg_parse = argparse.ArgumentParser(description='SeeBorg4')
    arg_parse.add_argument('-c', '--config', help='YAML config file',
                           required=True)
    args = arg_parse.parse_args()

    # Load configuration
    config = SeeBorg4Config.load_config(args.config)

    # Load database
    database.load(config.database_path())

    try:
        # Instantiate client
        client = discord.Client()

        # Instantiate bot and start it
        bot = SeeBorg4(client, config)
        bot.start()
    finally:
        database.close()


if __name__ == '__main__':
    main()
