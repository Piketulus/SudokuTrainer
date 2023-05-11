# Sudoku Trainer

Get the week 6 release [here](https://github.com/Piketulus/ot-harjoitustyo/releases/tag/viikko6)

## Documentation

- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)
- [Changelog](./dokumentaatio/changelog.md)
- [Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)
- [Käyttöohje](./dokumentaatio/kayttoohje.md)
- [Testausdokumentti](./dokumentaatio/testaus.md)

## Set-up

1. Install dependencies with:

```bash
poetry install
```

2. Perform the required initialization with:

```bash
poetry run invoke build
```

3. Start the app with:

```bash
poetry run invoke start
```

## Command line commands

### Running the app

Run the app with:

```bash
poetry run invoke start
```

### Testing

Run tests with:

```bash
poetry run invoke test
```

### Coverage report

Test coverage report can be generated with:

```bash
poetry run invoke coverage-report
```

Report generates to _htmlcov_ directory.

### Pylint

The checks defined by the file .pylintrc can be performed with the command:

```bash
poetry run invoke lint
```
