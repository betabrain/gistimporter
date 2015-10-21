# gistimporter
An importer for Python 3.x to allow import modules from gists.

## Install
You can install `gistimporter` from PyPi:

```
# pip install gistimporter
```

## Usage
Import the library and use `gistimporter.addgist()` to add your [gist URLs](https://gist.github.com/delapuente/528fca98f42c5236ce1d), after you can import modules normally:

```python
import gistimporter
gistimporter.addgist('https://gist.github.com/delapuente/528fca98f42c5236ce1d')

import git
import fuzzyfy
```
