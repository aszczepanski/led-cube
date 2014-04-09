# led-cube

## usage

```
run.py [-h] --effect EFFECT [--output OUT [OUT ...]]

optional arguments:
  -h, --help            show this help message and exit
  --effect EFFECT       execute given effect - one of the following: 'snake'
                        or 'smoke'
  --output OUT [OUT ...]
                        add given output method - one or more of the
                        following: 'serial', 'matplotlib' or 'opengl'

```

## example
Run 'snake' effect, use serial port and show OpenGL visualization:
```
python run.py --effect snake --output serial opengl
```
