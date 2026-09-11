#!/usr/bin/env python3
"""Conservative URL checker. Never changes canonical model status."""
import argparse, datetime as dt, json, socket, ssl, sys, time
import urllib.error, urllib.request
from pathlib import Path

GUARDED={401,403,429}

def check(url, timeout):
    req=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0 (compatible; Global-LLM-Atlas/0.1)"})
    try:
        with urllib.request.urlopen(req,timeout=timeout,context=ssl.create_default_context()) as r:
            r.read(2048); code=getattr(r,"status",200)
        return code,"reachable" if 200<=code<400 else "suspect",None
    except urllib.error.HTTPError as e:
        return e.code,"guarded" if e.code in GUARDED else "suspect",str(e)
    except (urllib.error.URLError,socket.timeout,TimeoutError,ssl.SSLError,OSError) as e:
        return None,"suspect",str(e)

def main():
    p=argparse.ArgumentParser(); p.add_argument("--data",default="data/llms.json"); p.add_argument("--report",required=True); p.add_argument("--timeout",type=int,default=15); a=p.parse_args()
    data=json.loads(Path(a.data).read_text(encoding="utf-8")); suspects=[]; guarded=[]
    for e in data["entries"]:
        code,kind,error=check(e["url"],a.timeout); print(f"{kind:10} {str(code):>4} {e['name']}")
        row=(e,code,error)
        (suspects if kind=="suspect" else guarded if kind=="guarded" else []).append(row); time.sleep(.2)
    if not suspects: return 0
    out=["# Automated URL check — human review required\n\n",f"Checked: {dt.datetime.now(dt.timezone.utc).isoformat()}\n\n","> This report does not change canonical status. Browser/semantic review is required.\n\n","| Service | Country | HTTP | Error | URL |\n|---|---|---:|---|---|\n"]
    for e,code,error in suspects: out.append(f"| {e['name']} | {e['country']} | {code or '—'} | {(error or '').replace('|','/')[:140]} | {e['url']} |\n")
    Path(a.report).parent.mkdir(parents=True,exist_ok=True); Path(a.report).write_text(''.join(out),encoding='utf-8'); return 10
if __name__=="__main__": sys.exit(main())
