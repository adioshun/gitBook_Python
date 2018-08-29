# Debuger 

GUI Debuger
```bash
sudo apt-get install python-pudb
python -m pudb.run foo.py
```

> 참고 : [[파이썬] PUDB 콘솔 디버거](http://egloos.zum.com/mcchae/v/10918232)

better-exceptions
```bash
pip install better_exceptions
import better_exceptions
```
> 참고 : https://github.com/Qix-/better-exceptions


#  PDB 

![](https://i.imgur.com/ofC3aqx.png)

import pdb

디버깅 원하는 곳에 `pdb.set_trace()` 추가 

"python -m pdb 파이선파일.py