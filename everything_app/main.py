"""Command line entry point for Everything App."""

import argparse
from . import EverythingApp


def main() -> None:
    parser = argparse.ArgumentParser(description="Personal Everything App")
    parser.add_argument(
        "--config", default="config.json", help="Path to configuration file"
    )
    args = parser.parse_args()

    app = EverythingApp(config_path=args.config)
    app.start()

    # This is just a demo loop
    print("Welcome! Type 'exit' to quit.")
    while True:
        cmd = input("app> ").strip()
        if cmd == "exit":
            break
        elif cmd == "notes":
            note = input("note> ")
            app.modules["notes"].add(note)
        elif cmd == "timer":
            seconds = int(input("seconds> "))
            app.modules["timers"].start_timer(seconds)
        else:
            print("Unknown command")


if __name__ == "__main__":
    main()
