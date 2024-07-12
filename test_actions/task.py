#!/usr/bin/env python
import argparse
import os
from datetime import datetime


def main(filename):
    now = datetime.now()
    formatted_date_time = now.strftime("%Y-%m-%d-%H-%M")
    print(formatted_date_time)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    outfile_path = os.path.join(script_dir, filename)
    with open(outfile_path, "w") as file:
        file.write(formatted_date_time)
        file.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", type=str,
                        help="name of output file")
    args = parser.parse_args()

    main(output=args.output)
