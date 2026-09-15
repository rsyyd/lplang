# LPLang

A general-purpose programming language.

LPLang is in active development. Current version is 0.8.0.

## Installation

```bash
chmod +x lumpo
./lumpo run file.lp
```

## Quick Example

```lplang
let nums = [1, 2, 3, 4, 5]
let doubled = map(nums, x => x * 2)
print doubled  // [2, 4, 6, 8, 10]

let name = null
print name ?? "anonymous"  // anonymous

switch "red" {
    case "red" { print "stop" }
    case "green" { print "go" }
    default { print "unknown" }
}
```

## Language

- Variables: `let` (mutable), `const` (immutable)
- Types: number, string, boolean, list, map, null
- Functions: `fn name(params) { body }` or `x => x + 1`
- Control flow: if/else, while, for..in, break, continue
- Pattern matching: `match` with literals, variables, struct patterns
- Error handling: try/catch/throw, defer
- Operators: ternary `? :`, null-coalescing `??`, pipe `|>`, optional chaining `?.`
- Compound assignment: `+= -= *= /= %= //=`
- Integer division: `//`

### Functions

```lplang
fn add(a, b) {
    return a + b
}

let multiply = (x, y) => x * y

print add(1, 2)       // 3
print multiply(3, 4)  // 12
```

### Named Arguments

```lplang
fn greet(name, greeting) {
    print "${greeting}, ${name}!"
}

greet("World", "Hello")
greet(greeting="Hi", name="World")
```

### Structs

```lplang
struct Point { x, y }

let p = Point { x: 10, y: 20 }
print p.x  // 10
```

### Pattern Matching

```lplang
match value {
    case 0 => print "zero"
    case n => print "got ${n}"
    default => print "other"
}
```

### Comprehensions

```lplang
let squares = [x * x for x in [1, 2, 3, 4, 5]]
let labels = { ("item${x}"): x for x in [1, 2, 3] }
```

## Standard Library

| Module | Functions |
|--------|-----------|
| math | sqrt, pow, floor, ceil, round, abs, min, max |
| time | now, sleep, iso |
| os | platform, cwd, args, path_join, path_split, is_file, is_dir |
| struct | pack_int, unpack_int, hex_to_bytes, bytes_to_hex |
| json | stringify, parse |
| fs | read, write, exists, mkdir, list_dir |
| db | open, execute, query (SQLite) |
| http | server, router, middleware |
| crypto | sha256, md5, random_uuid, random_hex |
| env | get, set, has |
| log | debug, info, warning, error, critical |
| html | template, escape |

```lplang
import "math"
import "fs"

let content = fs.read("file.txt")
print math.sqrt(16)  // 4
```

## CLI Commands

```bash
./lumpo run file.lp       # execute program
./lumpo repl              # interactive shell
./lumpo fmt file.lp       # format source
./lumpo test [path]       # run tests
./lumpo dev file.lp       # watch and restart on changes
./lumpo --help            # show help
./lumpo --version         # show version
```

## Testing

```bash
python3 -m unittest discover tests -v
```

84 tests covering language features, standard library, and CLI.

## Examples

See the `examples/` directory for more:

- `language_features.lp` - core language features
- `error_handling.lp` - try/catch/throw/defer
- `web_server.lp` - HTTP server
- `todo_api.lp` - full application example

## Status

LPLang is pre-1.0. The language and standard library are stable for experimentation but not production use.

## License

MIT
