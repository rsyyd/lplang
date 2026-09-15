# LPLang (Lumpo) v0.7.1

A lightweight, stable, and expressive general-purpose programming language.

LPLang is in active development (pre-1.0). Versions follow honest semantic versioning - `0.x.y` means not yet production-ready.

## Changelog

| Version | What's New |
|---------|-----------|
| `0.1.0` | Core interpreter: let, fn, if, while, for, import, print, list, map, string interpolation |
| `0.2.0` | Developer experience: lumpo fmt, test runner, dev (auto-restart), humanized errors, assert, middleware, route params |
| `0.3.0` | Error handling: try/catch/throw, local imports (.lp), stdlib modules (math, time), const, functional builtins (map/filter/reduce/find/any/all) |
| `0.4.0` | Language completeness: switch/case, break/continue, compound assign (+=/-=/*=//=/%=), block comments, ternary ?:, null-coalescing ??, string methods (starts_with/ends_with/repeat/pad_left/index_of) |
| `0.5.0` | Ergonomics & safety: defer, pipe \|>, arrow functions =>, optional chaining ?., destructuring (arrays/maps) |
| `0.6.0` | Structs, methods, pattern matching, comprehensions (list/map), argument validation, stdlib consolidation |
| `0.6.1` | CLI --version, single version constant, fixed REPL banner |
| `0.6.2` | Better error reporting: line numbers for IndexError/KeyError, precise error location |
| `0.7.0` | Module resolution: import without extension (`import "./lib/util"`), relative imports from cwd, consistent resolver |
| `0.7.1` | **Patch**: keyword/named arguments now work correctly (runtime binding bug fix); validates mixed positional+named, detects duplicates and unknown args |
| `0.8.0` | **Minor**: `--help` flag added; shows usage and available commands |

## Language Features

- `let` / `const` - mutable and read-only variables
- Destructuring: `let [a, b] = list`, `let {name, age} = user`
- Types: number, string, boolean, list, map, null
- String interpolation: `"hello ${name}"`, triple-quote, single-quote strings
- Arrow functions: `x => x * 2` or `(a, b) => a + b`
- Pipe operator: `data |> map(fn) |> filter(fn)` (result becomes first arg)
- Optional chaining: `user?.profile?.name` (always safe for null)
- `defer` - cleanup in LIFO order on function/block exit, even on return/error
- First-class functions, recursion, closures, named/keyword arguments
- Control flow: if/else, while, for..in, break, continue
- `match` with literal patterns, variable binding, struct patterns, multi-statement cases, default
- Structs with field initialization and methods
- List/map comprehensions: `[expr for x in data]`, `{key: value for x in data}`
- switch/case/default (exact match)
- try/catch/throw
- Ternary: `cond ? a : b`
- Null-coalescing: `a ?? "default"`
- Compound assignment: `+= -= *= /= %=`
- Block comments: `/* ... */`
- Integer division: `//`
- 35+ built-in functions

## Standard Library

| Module | Contents |
|--------|----------|
| math | sqrt, pow, floor, ceil, round, abs, min, max |
| time | now, sleep, iso |
| os | platform, cwd, args, path_join/split/ext/stem, is_file/is_dir |
| struct | pack_int, unpack_int, hex_to_bytes, bytes_to_hex |
| http | web server, router, middleware, route params |
| json | stringify, parse |
| db | SQLite (open, execute, query) |
| fs | read, write, exists, mkdir, list_dir |
| crypto | sha256, md5, random_uuid, random_hex |
| env | get, set, has |
| log | debug, info, warning, error, critical |
| html | templating, escape |

## Tooling

- `lumpo run file.lp` - execute program
- `lumpo --help` - show available commands
- `lumpo fmt file.lp` - auto-format source
- `lumpo test [path]` - run tests
- `lumpo dev file.lp` - watch file and auto-restart
- `lumpo repl` - interactive shell (tab-completion)
- Humanized error reporter (snippet + line number)

## Quick Start

```bash
chmod +x lumpo
./lumpo run examples/language_features.lp
./lumpo run examples/error_handling.lp
./lumpo test examples/unit_test.lp
```

## Example

```lplang
import "math"

const PI = 3.14159
let nums = [1, 2, 3, 4, 5]

let evens = filter(nums, fn(x) { return x % 2 == 0 })
print "evens: ${join(evens, ', ')}"

let name = null
print name ?? "anonymous"

let status = 20 >= 18 ? "adult" : "minor"
print status

switch "red" {
    case "red" { print "stop" }
    case "green" { print "go" }
    default { print "broken signal" }
}

try {
    throw "oops"
} catch e {
    print "caught: ${e}"
}
```

## Testing

The test suite has **77 tests** organized by language version/feature:

```bash
python3 -m unittest discover tests -v    # run all tests
```

Test files:
- `test_lplang.py` - core language (12 tests)
- `test_lumpo_v2.py` - v2 features (4 tests)
- `test_v0_2_0.py` - v0.2 (assert, http, middleware, fmt, test command, errors; 6 tests)
- `test_v0_3_0.py` - v0.3 (try/catch/throw, local imports, math, time, functional builtins; 12 tests)
- `test_v0_4_0.py` - v0.4 (switch, compound assign, break/continue, null-coalescing, ternary, strings, range; 12 tests)
- `test_v0_4_1.py` - v0.4.1 (os, struct modules; 2 tests)
- `test_v0_5_0.py` - v0.5 (defer, pipe, arrow, optional chaining, destructuring; 5 tests)
- `test_v0_6_0.py` - v0.6 (structs, methods, match, comprehensions; 12 tests)
- `test_cli_version.py` - CLI --version and --help (3 tests)
- `test_error_reporting.py` - error reporting (5 tests)
- `test_module_resolution.py` - module resolution (5 tests)

All tests pass on v0.7.1.

## Roadmap

| Version | Milestone |
|---------|-----------|
| ✅ 0.1.0 | Core interpreter |
| ✅ 0.2.0 | Developer experience |
| ✅ 0.3.0 | Error handling + stdlib |
| ✅ 0.4.0 | Language completeness (switch, ternary, ??, break/continue) |
| ✅ 0.5.0 | Destructuring, pipe, arrow functions, optional chaining |
| ✅ 0.6.0 | Structs, methods, pattern matching, comprehensions |
| ✅ 0.7.0 | Module resolution (extension-optional imports) |
| ✅ 0.7.1 | Named/keyword arguments (bug fix) |
| ⏳ 0.8.0 | Iterators, enhanced pattern matching, operator overloading |
| ⏳ 0.9.0 | Async/await, event loop |
| ⏳ 1.0.0 | Gradual typing, LSP, production-ready |

## License

MIT - see LICENSE file.
