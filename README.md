# uniq

This action is created to find out duplicate filenames in source folder.

## Usage

Describe how to use your action here.

### Example workflow

```yaml
name: My Workflow
on: [push]
jobs:
  build:
    name: self test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v1
      - uses: rational-kunal/uniq@alpha
        with:
          PATH: "./src"
```

### Inputs

| Input                                             | Description                                        |
|------------------------------------------------------|-----------------------------------------------|
| `PATH`  | Path to your sorce folder    |


> Template from [jaconbtomlinson/python-continer-action](https://github.com/jacobtomlinson/python-container-action)

> Still updating