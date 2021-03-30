# Passme

Passme is a local password manager written in Python.

## Installation

- Clone the repo

```bash
git clone https://github.com/Pushkarang/passme
```
- Run install script inside passme folder

```bash
./install.sh
```
## Usage

Initialize passme
```bash
passme init
```
Add password
```bash
passme add -k mygmail -p secretpassword
```
Get password
```bash
passme get -k mygmail #Will return secretpassword
```
For more
```bash
passme -h
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)