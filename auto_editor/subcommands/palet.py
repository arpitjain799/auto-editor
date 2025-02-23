from __future__ import annotations

import sys

from auto_editor.interpreter import Lexer, Parser, env, interpret
from auto_editor.lib.err import MyError


def main(sys_args: list[str] = sys.argv[1:]) -> None:
    if sys_args:
        with open(sys_args[0]) as file:
            program_text = file.read()

        try:
            interpret(env, Parser(Lexer(sys_args[0], program_text)))
        except (MyError, ZeroDivisionError) as e:
            print(f"error: {e}", file=sys.stderr)

    else:
        from .repl import main

        main(sys_args)


if __name__ == "__main__":
    main()
