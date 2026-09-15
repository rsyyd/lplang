# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.1.0.html).

## [0.8.0] - 2026-09-15

### Added

- `--help` flag to show usage and available commands
- Boolean short-circuit operators: `&&`, `||`, `and`, `or`
- Floor division operator `//` and compound assignment `//=`
- Standard library path resolution fix: `import "mod"` works from symlinked installations (npm, binary installs)
- `.npmignore` for GitHub Packages npm distribution
- `package.json` with `@rsyyd/lplang` package metadata

### Changed

- README rewritten to professional open source standard
- English-only enforcement on all official language surfaces
- All em dashes removed from documentation and source comments
- Test count updated to 85

## [0.7.1] - 2026-09-13

### Fixed

- Keyword/named arguments runtime binding bug
- Mixed positional + named argument validation
- Duplicate and unknown argument detection

## [0.7.0] - 2026-09-12

### Added

- Extension-optional import resolution
- Relative imports from cwd
- Consistent module resolver for multi-file projects
