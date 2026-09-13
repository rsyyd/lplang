# LPLang (Lumpo) v0.6.2

**Bahasa pemrograman ringan, stabil, dan mudah dipahami.**

LPLang masih dalam tahap pengembangan awal (pre-1.0). Versi mengikuti semantic versioning yang jujur — `0.x.y` berarti belum production-ready.

## Changelog
| Versi | Isi |
|-------|-----|
| `0.1.0` | Interpreter dasar: let, fn, if, while, for, import, print, list, map, string interpolation |
| `0.2.0` | DX: lumpo fmt, test runner, dev (auto-restart), humanized error, assert, middleware, route params |
| `0.3.0` | try/catch/throw, import file lokal .lp, modul math/time, const, functional builtins (map/filter/reduce/find/any/all) |
| `0.4.0` | switch, break/continue, compound assign (+=/-=/*=//=/%=), block comment /* */, ternary ?:, null-coalescing ??, single-quote string, starts_with/ends_with/repeat/pad_left/index_of |
| `0.5.0` | Ergonomi & keamanan resource: `defer`, pipe `|>`, arrow function `=>`, optional chaining `?.`, array/map destructuring |
| `0.6.0` | Struct, method, pattern matching, list/map comprehension, validasi argumen fungsi, dan kompatibilitas modul stdlib |
| `0.6.1` | CLI `--version`, konstanta versi tunggal, perbaikan banner REPL (sebelumnya salah tulis v1.1) |
| `0.6.2` | Error reporting: line number untuk IndexError/KeyError, ekspresi error menunjuk baris yang tepat, message catch bersih dari `(line N)` |

## Fitur Bahasa
- `let` / `const` — variabel mutable & read-only
- Destructuring: `let [a, b] = list`, `let {name, age} = user`
- Tipe: number, string, boolean, list, map, null/none
- String interpolation `\"halo ${nama}\"`, triple-quote, single-quote
- Arrow function: `x => x * 2` atau `(a, b) => a + b`
- Pipe: `data |> map(fn) |> filter(fn)`; hasil menjadi argumen pertama
- Optional chaining: `user?.profile?.name` selalu aman untuk `null`
- `defer` — cleanup LIFO saat block/fungsi selesai, bahkan saat `return`/error
- Fungsi first-class, recursion, closure
- Control flow: if/else, while, for..in, break, continue
- `match` dengan literal, binding variabel, pola struct, blok case, dan default
- Struct, inisialisasi field, dan method
- List/map comprehension: `[expr for x in data]`, `{key: value for x in data}`
- switch/case/default (exact match)
- try/catch/throw
- Ternary `cond ? a : b`
- Null-coalescing `a ?? \"default\"`
- Compound assign `+= -= *= /= %=`
- Block comment `/* ... */`
- Operator `//` (integer division)
- 35+ builtin functions

## Modul Stdlib
| Modul | Isi |
|------|-----|
| math | sqrt, pow, floor, ceil, round, abs, min, max |
| time | now, sleep, iso |
| os | platform, cwd, args, path_join/split/ext/stem, is_file/is_dir |
| struct | pack_int, unpack_int, hex_to_bytes, bytes_to_hex |
| http | Web server + router, middleware, route params |
| json | stringify, parse |
| db | SQLite (open, execute, query) |
| fs | read, write, exists, mkdir, list_dir |
| crypto | sha256, md5, random_uuid, random_hex |
| env | get, set, has |
| log | debug, info, warning, error, critical |
| html | templating & escape |

## Tooling
- `lumpo run file.lp` — jalankan program
- `lumpo fmt file.lp` — auto-format source
- `lumpo test [path]` — test runner
- `lumpo dev file.lp` — file watcher auto-restart
- `lumpo repl` — interactive shell (tab-completion)
- Humanized error reporter (snippet + line number)

## Quick Start
```bash
chmod +x lumpo
./lumpo run examples/fitur_bahasa.lp
./lumpo run examples/error_handling.lp
./lumpo run examples/fitur_v130.lp
./lumpo test examples/unit_test.lp
```

## Contoh
```lplang
import "math"

const PI = 3.14159
let nums = [1, 2, 3, 4, 5]

let genap = filter(nums, fn(x) { return x % 2 == 0 })
print "genap: ${join(genap, ', ')}"

let nama = null
print nama ?? \"anonymous\"

let status = 20 >= 18 ? \"dewasa\" : \"anak\"
print status

switch \"merah\" {
    case \"merah\" { print \"berhenti\" }
    case \"hijau\" { print \"jalan\" }
    default { print \"lampu rusak\" }
}

try {
    throw \"oops\"
} catch e {
    print \"caught: ${e}\"
}
```

## Testing
```bash
python3 tests/test_lplang.py         # core (8 test)
python3 tests/test_lumpo_v2.py       # v2 (4 test)
python3 tests/test_v0_5_0.py         # v0.5 (5 test)
python3 tests/test_v1_1_0.py         # v0.3 (6 test)
python3 tests/test_v1_2_0.py         # v0.3 (12 test)
python3 tests/test_v1_3_0.py         # v0.4 (12 test)
python3 tests/test_v1_3_1.py         # v0.4.1 (2 test)
python3 tests/test_v0_6_0.py         # v0.6 (12 test)
python3 tests/test_cli_version.py    # CLI --version (2 test)
python3 tests/test_error_reporting.py # error reporting (5 test)
```

Total: **68 test**, semua lulus.

## Roadmap
| Versi | Target |
|-------|--------|
| ✅ 0.1.0 | Interpreter dasar |
| ✅ 0.2.0 | Developer experience |
| ✅ 0.3.0 | Error handling + modul |
| ✅ 0.4.0 | Bahasa lengkap (switch, ternary, ??, break/continue) |
| ✅ 0.5.0 | Destructuring, spread operator, arrow fn, enum |
| ✅ 0.6.0 | Struct, method, pattern matching, comprehension |
| ⏩ 0.7.0 | Iterators, enhanced pattern matching, operator overloading |
| ⏩ 0.8.0 | Async/await, event loop |
| ⏩ 1.0.0 | Gradual typing, LSP, production-ready |

## Lisensi
MIT — lihat file `LICENSE`.