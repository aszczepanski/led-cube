# led-cube

## usage

```
usage: run.py [-h] --effect EFFECT [--output OUT [OUT ...]]

optional arguments:
  -h, --help            show this help message and exit
  --effect EFFECT       execute given effect - one of the following: 'snake'
                        or 'smoke'
  --output OUT [OUT ...]
                        add given output method - one or more of the
                        following: 'serial', 'matplotlib' or 'opengl'

```

## example
```
python run.py --effect snake --output serial opengl
```
