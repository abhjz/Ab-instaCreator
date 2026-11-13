import re,sys
from pathlib import Path

def check(text):
    tags=re.findall(r'(?<!\w)#[\w]+',text,flags=re.UNICODE)
    if len(tags)!=5: raise ValueError(f'Expected exactly 5 hashtags, found {len(tags)}')
    if len({t.casefold() for t in tags})!=5:raise ValueError('Use five distinct hashtags')
    return tags
if __name__=='__main__':
    try: print('OK: '+', '.join(check(Path(sys.argv[1]).read_text())))
    except (ValueError,IndexError) as e:raise SystemExit(str(e))
