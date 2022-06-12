import argparse
import logging
import os
import findspark

from datetime import datetime

from asoiaf import ASongOfIceAndFire


logging.basicConfig(
    format='%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s', level='INFO')


logger = logging.getLogger(__name__)

findspark.init()


def read_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c", "--challenge", help="execute challenge for input file.", action="store_true")
    return parser


def run():
    try:
        args = read_args().parse_args()

        logger.info("starts job.")

        if args.challenge:
            c1 = ASongOfIceAndFire()

            c1.run(
                filepath=os.path.join(
                    os.getcwd(), 'data', 'input', 'dataset.csv'),
                output=os.path.join(os.getcwd(), 'data', 'output')
            )

    except Exception as msg:
        logger.error(f"failed: {msg}.")

    logger.info("done.")


if __name__ == "__main__":
    run()
