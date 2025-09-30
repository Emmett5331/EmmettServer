import argparse
from .core import say, greet, farewell, info, warn, error, current_time, random_number, echo

COMMANDS = {
    "say": say,
    "greet": greet,
    "farewell": farewell,
    "info": info,
    "warn": warn,
    "error": error,
    "time": lambda _: current_time(),
    "random": lambda args: random_number(int(args.min), int(args.max)),
    "echo": lambda args: echo(args.text, int(args.repeat))
}

def main():
    parser = argparse.ArgumentParser(prog="prompthub")
    subparsers = parser.add_subparsers(dest="command")

    # say, greet, farewell, info, warn, error
    for cmd in ["say", "greet", "farewell", "info", "warn", "error"]:
        sub = subparsers.add_parser(cmd)
        sub.add_argument("text", help="Text for the command")
        sub.set_defaults(func=COMMANDS[cmd])

    # time
    sub_time = subparsers.add_parser("time", help="Show current time")
    sub_time.set_defaults(func=lambda _: current_time())

    # random
    sub_rand = subparsers.add_parser("random", help="Generate random number")
    sub_rand.add_argument("--min", default=0, help="Minimum value", required=False)
    sub_rand.add_argument("--max", default=100, help="Maximum value", required=False)
    sub_rand.set_defaults(func=COMMANDS["random"])

    # echo
    sub_echo = subparsers.add_parser("echo", help="Repeat text")
    sub_echo.add_argument("text", help="Text to repeat")
    sub_echo.add_argument("--repeat", default=1, help="Number of times", required=False)
    sub_echo.set_defaults(func=COMMANDS["echo"])

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
