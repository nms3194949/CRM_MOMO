#!/usr/bin/env python3
"""ShareGo IG 圖卡產生器。用法：python3 _ops/ig/build.py <slug>
讀 _ops/ig/posts/<slug>.json，輸出 ig/<slug>/01.jpg… 與 ig/<slug>/preview.jpg（1080x1350 JPEG）。"""
import json,sys,os,html,asyncio
ROOT=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CSS=open(os.path.join(ROOT,'_ops/ig/slides.css')).read()
def r(s): return s or ''   # 文字允許 <em>、<br>、<b>
def top(n,t): return f'<div class="top"><span class="brand">Share<em>Go</em>｜客帶客</span><span class="pg">{n}/{t}</span></div>' if t>1 else '<div class="top"><span class="brand">Share<em>Go</em>｜客帶客</span><span></span></div>'
def foot(l,rr): return f'<div class="foot"><span>{l}</span><span class="swipe">{rr}</span></div>'
def note(s,d): return f'<div class="sub" style="font-size:36px">{r(s.get("note"))}</div>' if s.get('note') else ''
def slide(s,i,T):
    t=s['type']; last=i==T; mint=s.get('mint', t in('cover','cta'))
    fl=s.get('foot', 'ShareGo 客帶客｜讓熟客幫你帶新客' if last else ('門店 LINE 會員經營筆記' if i==1 else 'crm.momowinwin.com'))
    fr='' if last else ('往左滑 →' if i==1 and T>1 else '→')
    b=''
    if t=='cover':
        b=f'<div class="big">{r(s["title"])}</div>'+(f'<div class="sub">{r(s.get("sub"))}</div>' if s.get('sub') else '')
        if s.get('coupon'): b+=f'<div class="coupon"><b>{s["coupon"][0]}</b><span>{s["coupon"][1]}</span></div>'
        if s.get('tag'): b+=f'<div class="tag">{r(s["tag"])}</div>'
    elif t=='points':
        b=f'<h2>{r(s["h"])}</h2>'+''.join(f'<div class="k"><i>{s.get("icon") or n+1}</i><div><b>{x[0]}</b><span>{x[1]}</span></div></div>' for n,x in enumerate(s['items']))+note(s,0)
    elif t=='wrong':
        b=f'<h2>{r(s["h"])}</h2>'+''.join(f'<div class="x"><b>{x[0]}</b><span>{x[1]}</span></div>' for x in s['items'])+note(s,0)
    elif t=='steps':
        b=f'<h2>{r(s["h"])}</h2>'+''.join(f'<div class="step"><i>{x[0]}</i><div><b>{x[1]}</b><span>{x[2]}</span></div></div>' for x in s['items'])+note(s,0)
    elif t=='table':
        b=f'<h2>{r(s["h"])}</h2><div class="row"><b>{s["head"][0]}</b><b>{s["head"][1]}</b></div>'+''.join(f'<div class="row"><span>{x[0]}</span><span{" class=g" if len(x)>2 and x[2] else ""}>{x[1]}</span></div>' for x in s['rows'])+note(s,0)
    elif t=='check':
        b=f'<h2>{r(s["h"])}</h2>'+''.join(f'<div class="q">{x}</div>' for x in s['items'])+note(s,0)
    elif t=='big':
        b=(f'<div class="pg" style="display:inline-block;margin-top:90px;background:#06c755;font-size:34px;padding:10px 28px">{s["kicker"]}</div>' if s.get('kicker') else '')
        b+=f'<h1 style="margin-top:30px">{r(s["title"])}</h1>'+(f'<div class="sub" style="color:#10201a;font-weight:900;font-size:50px;margin-top:20px">{r(s.get("sub"))}</div>' if s.get('sub') else '')
        b+=f'<div class="sub">{r(s.get("text"))}</div>'+(f'<div class="tag">{r(s["tag"])}</div>' if s.get('tag') else '')
    elif t=='quiz':
        b=f'<h2 style="margin-bottom:36px">{r(s.get("h","選選看"))}</h2><div class="qz">{r(s["q"])}</div>'+''.join(f'<div class="opt"><i>{"ABCD"[n]}</i><span>{x}</span></div>' for n,x in enumerate(s['options']))+note(s,0)
    elif t=='answer':
        b=f'<h2 style="margin-bottom:36px">{r(s.get("h","答案揭曉"))}</h2><div class="ans">{r(s["answer"])}</div><div class="sub" style="margin-top:0">{r(s["text"])}</div>'+note(s,0)
    elif t=='cta':
        b=f'<h2>{r(s["h"])}</h2>'+(f'<div class="sub" style="margin-top:0">{r(s.get("text"))}</div>' if s.get('text') else '')
        if s.get('items'): b+=''.join(f'<div class="step"><i>{x[0]}</i><div><b>{x[1]}</b><span>{x[2]}</span></div></div>' for x in s['items'])
        if s.get('url'): b+=f'<div class="url">{s["url"]}</div>'
        b+=f'<div class="sub" style="font-size:36px">{r(s.get("note","連結在個人檔案。收藏這篇，需要時拿出來對照。"))}</div>'
    else: raise SystemExit('unknown type '+t)
    return f'<section class="s{" mint" if mint else ""}{" single" if T==1 else ""}">{top(i,T)}{b}{foot(fl,fr)}</section>'
async def main(slug):
    p=json.load(open(os.path.join(ROOT,'_ops/ig/posts',slug+'.json')))
    S=p['slides'];T=len(S)
    doc=f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>'+''.join(slide(s,i+1,T) for i,s in enumerate(S))+'</body></html>'
    out=os.path.join(ROOT,'ig',slug);os.makedirs(out,exist_ok=True)
    hp=os.path.join('/tmp',slug+'.html');open(hp,'w').write(doc)
    from playwright.async_api import async_playwright
    async with async_playwright() as pw:
        kw={'args':['--no-sandbox']}
        if os.path.exists('/usr/bin/google-chrome'): kw['executable_path']='/usr/bin/google-chrome'
        b=await pw.chromium.launch(**kw);pg=await b.new_page(viewport={'width':1080,'height':1350})
        await pg.goto('file://'+hp);await pg.wait_for_timeout(400)
        # 檢查文字是否超出版面
        over=await pg.evaluate('''()=>[...document.querySelectorAll('section.s')].map((s,i)=>{const f=s.querySelector('.foot').getBoundingClientRect().top;let m=0;s.querySelectorAll('h1,h2,.sub,.k,.x,.step,.row,.q,.opt,.qz,.ans,.tag,.url,.big,.mock').forEach(e=>{m=Math.max(m,e.getBoundingClientRect().bottom)});return m>f-20?i+1:0}).filter(Boolean)''')
        files=[]
        for i,s in enumerate(await pg.query_selector_all('section.s')):
            fp=os.path.join(out,f'{i+1:02d}.jpg');await s.screenshot(path=fp,type='jpeg',quality=90);files.append(fp)
        await b.close()

    # 限時動態圖（1080x1920）：新貼文預告，貼文封面縮圖＋引導去主頁
    kick=p.get('story_kicker') or ('今晚的互動題，你選哪個？' if any(s['type']=='quiz' for s in S) else '今晚新貼文')
    tip=p.get('story_tip') or (f'到主頁看完整 {T} 張 →' if T>1 else '到主頁看完整內容 →')
    sh=f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}
    .st{{width:1080px;height:1920px;background:#e8f6ee;position:relative;overflow:hidden;font-family:"Noto Sans CJK TC",sans-serif}}
    .st .hd{{position:absolute;top:260px;left:0;right:0;text-align:center}}
    .st .bd{{display:inline-block;background:#06c755;color:#fff;font-weight:900;font-size:46px;border-radius:999px;padding:14px 40px}}
    .st .br{{font-size:40px;font-weight:900;margin-bottom:28px}}.st .br em{{font-style:normal;color:#e0a800}}
    .st img{{position:absolute;left:150px;top:500px;width:780px;height:975px;border:10px solid #fff;border-radius:32px;box-shadow:0 30px 70px rgba(16,32,26,.25);transform:rotate(-2deg)}}
    .st .ft{{position:absolute;top:1530px;left:0;right:0;text-align:center}}
    .st .ft b{{display:inline-block;background:#ffd23f;color:#1d1a08;font-size:48px;font-weight:900;border-radius:20px;padding:20px 44px}}
    </style></head><body><div class="st"><div class="hd"><div class="br">Share<em>Go</em>｜客帶客</div><span class="bd">{kick}</span></div>
    <img src="file://{files[0]}"><div class="ft"><b>{tip}</b></div></div></body></html>"""
    sp=os.path.join('/tmp',slug+'-story.html');open(sp,'w').write(sh)
    async with async_playwright() as pw:
        b=await pw.chromium.launch(**kw);pg=await b.new_page(viewport={'width':1080,'height':1920})
        await pg.goto('file://'+sp);await pg.wait_for_timeout(400)
        await pg.screenshot(path=os.path.join(out,'story.jpg'),type='jpeg',quality=90);await b.close()
    from PIL import Image
    ims=[Image.open(f).resize((360,450)) for f in files];c=Image.new('RGB',(370*len(ims)+5,460),'white')
    for i,im in enumerate(ims): c.paste(im,(5+370*i,5))
    c.save(os.path.join(out,'preview.jpg'),quality=80)
    print(json.dumps({'slug':slug,'slides':T,'overflow_slides':over,'story_url':f'https://crm.momowinwin.com/ig/{slug}/story.jpg','urls':[f'https://crm.momowinwin.com/ig/{slug}/{i+1:02d}.jpg' for i in range(T)]},ensure_ascii=False))
    if over: sys.exit(2)
asyncio.run(main(sys.argv[1]))
