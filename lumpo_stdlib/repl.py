# REPL for lumpo
import sys
import readline  # optional, for history & tab-completion if available
from lumpo import tokenize, Parser, exec_block, make_global_env

class REPL:
    def __init__(self):
        self.env = make_global_env()
        self.line_no = 0

    def run_line(self, line):
        self.line_no += 1
        try:
            tokens = tokenize(line)
            ast = Parser(tokens).parse()
            for s in ast.stmts:
                exec_stmt(s, self.env)
        except Exception as e:
            print(f"error (line {self.line_no}): {e}")

    def banner(self):
        print("lumpo REPL - type `exit` or Ctrl+D to quit")
        print("type a statement, multi-line blocks end with `}` on its own line")

    def run(self):
        # simple tab‑completion from current env variables
        def completer(text, state):
            opts = [k for k in self.env.vars if k.startswith(text)]
            if state < len(opts):
                return opts[state]
            return None
        readline.set_completer(completer)
        readline.parse_and_bind('tab: complete')
        buffer = ""
        while True:
            try:
                prompt = "··· " if buffer else "λλλ "
                line = input(prompt)
                buffer += line + "\n"
                # simple heuristic: if braces don't balance, keep going
                opens = buffer.count("{")
                closes = buffer.count("}")
                if opens != closes:
                    continue
                self.run_line(buffer)
                buffer = ""
            except (EOFError, KeyboardInterrupt):
                print()
                break
            if buffer.strip() == "exit\n":
                break

if __name__ == "__main__":
    from lumpo import exec_stmt  # import here to avoid circular at top-level
    REPL().run()
