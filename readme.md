# Pascal's Triangle with Graphical Representation

## Dependencies
```shell
$ pip intall -r requirements.txt
```

## Run
```shell
$ ./main.py | -g, --graph; -d, --debug; -r, --read
```

__Default output path__: 
`
./out/Graph.gv.[png]
`

### `-g, --graph`
Creates a pictorial representation of the current 
Pascal's triangle with `PNG` support by default.

### `-d, --debug`
Prompts the user with the __schema of the graph__ and the time elapsed.

### `-r, --read`
Reads from a local file of type `.gv`.

## Example
Pictorial representation of Pascal's triangle with `PNG` support.

![example][out_example]

<!-- Links and refs -->
[out_example]: ./out/Graph.gv.png