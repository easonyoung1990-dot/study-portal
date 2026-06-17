# -*- coding: utf-8 -*-
"""
生成两份英语期末考前可打印 PDF（放入 papers/）：
  1) 英语期末复习重点_单元梳理_两娃.pdf —— 按单元/板块整理全部复习重点，★必背 ▲高频易错 【新】考前新增
  2) 英语期末冲刺背诵卡_两娃.pdf —— 挑最常错+最高频考点(期末优先)，错题×语法合一，30分钟可背 + 必考作文模板

数据来源（仓库内）：
  data/learning/english_m3m4_kenton.json  （哥哥 M3/M4 知识梳理）
  data/learning/english_errors_kenton_2026-06-16.json （哥哥错题）
  data/learning/lesson_eddey_2026-06-16.json （弟弟老师6.16复习总结）
依赖：PyMuPDF（fitz）。MuPDF 自带 CJK 回退字体，无需额外字体。
注：本脚本是『生产层』工具；PDF 内容均为通用英语知识点+匿名小名，无身份信息。
"""
import fitz, os

KEN = "#2f6fb3"   # 哥哥 青蓝
EDD = "#e8642f"   # 弟弟 珊瑚橙
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "papers")

BASE_CSS = """
* { font-family: sans-serif; }
body { font-size: 10.5pt; line-height: 1.45; color:#222; }
h1 { font-size: 19pt; margin: 0 0 2pt 0; }
h2 { font-size: 14pt; margin: 12pt 0 4pt 0; padding:3pt 8pt; color:#fff; border-radius:6px; }
h3 { font-size: 11.5pt; margin: 8pt 0 2pt 0; }
.sub { color:#666; font-size:9pt; margin:0 0 8pt 0; }
.legend { font-size:9pt; background:#f4f6f8; border:1px solid #dde3e8; border-radius:6px; padding:5pt 8pt; margin:4pt 0 8pt 0; }
.unit { border:1px solid #e3e7ec; border-radius:8px; padding:5pt 9pt; margin:5pt 0; }
.lab { font-weight:bold; color:#444; }
ul { margin:2pt 0 4pt 0; padding-left:16pt; }
li { margin:1pt 0; }
.star { color:#d48806; font-weight:bold; }      /* ★ 必背 */
.tri  { color:#c0392b; font-weight:bold; }       /* ▲ 易错 */
.new  { background:#fff1b8; color:#ad6800; font-weight:bold; border-radius:3px; padding:0 3px; }
.box { border:2px solid; border-radius:8px; padding:6pt 9pt; margin:6pt 0; }
table { border-collapse:collapse; width:100%; margin:3pt 0 6pt 0; font-size:9.5pt; }
td,th { border:1px solid #cdd5dd; padding:3pt 6pt; text-align:left; vertical-align:top; }
th { background:#eef2f6; }
.eg { color:#1a6f3c; }
.k { color:__KEN__; } .e { color:__EDD__; }
.tip { font-size:9pt; color:#555; }
""".replace("__KEN__", KEN).replace("__EDD__", EDD)

def render(html, path, css=BASE_CSS):
    story = fitz.Story(html=html, user_css=css)
    MED = fitz.paper_rect("a4")
    where = MED + (40, 36, -40, -40)
    writer = fitz.DocumentWriter(path)
    more = 1
    while more:
        dev = writer.begin_page(MED)
        more, _ = story.place(where)
        story.draw(dev)
        writer.end_page()
    writer.close()
    d = fitz.open(path)
    n = d.page_count
    d.close()
    return n

S = '<span class="star">★</span>'
T = '<span class="tri">▲</span>'
def NEW(t): return '<span class="new">新·%s</span>' % t

# ========================= PDF 1：单元梳理 =========================
def pdf1():
    h = ['<h1>英语期末复习重点 · 单元梳理</h1>',
         '<p class="sub">两娃通用速查 | 哥哥 Kenton 四下 M3–M4 | 弟弟 Eddey 三下 | 2026-06-16 考前</p>',
         '<div class="legend"><b>图例：</b> <span class="star">★</span> 必背必考 &nbsp; '
         '<span class="tri">▲</span> 高频易错 &nbsp; <span class="new">新·X</span> 考前新强调（最近错题/老师重点）</div>']

    # ---- 哥哥 ----
    h.append('<h2 style="background:%s">哥哥 Kenton · 四年级下 Module 3–4</h2>' % KEN)
    units = [
        ("M3U1 Shapes 形状",
         ["circle 圆形", "square 正方形", "triangle 三角形", "star 星形", "rectangle 长方形",
          "（shape 形状 / count 数 / hungry 饿 / like 像 / side 边）"],
         [f"{S} What shape is it? It's a circle.（询问形状；答句 a 不能省）",
          "How many triangles? 多少个三角形?",
          "A triangle has three sides. 三角形有三条边。"],
         [f"{S} What shape is it? → It's <b>a</b> + 形状（a 不能省）。",
          f"{T} like 两义：①动词『喜欢』 I like dolls. ②介词『像』 He looks like his father."]),
        ("M3U2 Colours 颜色",
         ["sky 天空", "sea 海", "mountain 山", "river 河流",
          "（rainbow 彩虹 / violet 紫罗兰 / outside 在外面 / plant 植物 / plate 盘子）"],
         [f"{S} What colour <b>is</b> the sky? It's blue.",
          f"{S} What colour <b>are</b> the leaves? They're green."],
         [f"{T} is/are 跟单复数：单数 is、复数 are（the leaves→are）。",
          f"{S} like + doing 喜欢做某事；I like sleeping in spring.",
          "区分 orange：颜色『橙色』/ 水果『橘子』。"]),
        ("M3U3 Seasons 季节",
         ["plant a tree 植树", "have a picnic 野餐", "ice-skate 滑冰", "ski 滑雪",
          "（season / ride a bicycle 骑车 / fly a kite 放风筝 / grow 生长 / July 七月）"],
         [f"{S} What season is it? Is it summer? It's warm and rainy.",
          f"{S} We <b>can</b> have picnics in the park.（can+原形）",
          "What's your favourite season?"],
         [f"{T} 可数名词单数不能单独用：have <b>a</b> picnic = have picnics；ride a bicycle = ride bicycles。",
          f"{S} go + doing 去做某事：go skiing / go ice-skating。",
          f"{S} 情态动词 can + 动词原形。"]),
        ("M4U1 My body 身体",
         ["body 身体", "head 头", "shoulder 肩", "arm 手臂", "hand 手", "finger 手指", "leg 腿", "knee 膝", "foot 脚",
          "（myself/yourself / stretch 伸 / raise 举 / stamp 跺 / clap 拍）"],
         [f"{S} I have a big head and a big body.",
          "My nose is small. / These are my eyes.",
          "Can you draw yourself? Raise your hands."],
         [f"{S}{T} 身体部位复数加 -s；<b>只有 foot → feet</b>（{NEW('foot→feet')}）。",
          "Yes, of course. 比 Yes, I can. 语气更肯定。"]),
        ("M4U2 Children's Day 儿童节",
         ["park 公园", "cinema 电影院", "zoo 动物园",
          "（the first of June 6月1日 / photograph 照片 / Singapore / Japan / January / second 第二）"],
         [f"{S} What do you do <b>on</b> Children's Day? I go to the cinema.",
          "Do you have a class party on Children's Day?",
          "In the afternoon, I go to the park <b>with</b> my parents."],
         [f"{S} 时间介词 <b>on</b> + 具体日期/节日：on Children's Day, on Mother's Day。",
          "with sb. 和某人一起。"]),
    ]
    for name, words, sents, gram in units:
        h.append('<div class="unit"><h3 class="k">%s</h3>' % name)
        h.append('<span class="lab">核心词汇：</span>' + " · ".join(words))
        h.append('<div><span class="lab">必背句型：</span><ul>' + "".join(f"<li>{x}</li>" for x in sents) + "</ul></div>")
        h.append('<div><span class="lab">语法点：</span><ul>' + "".join(f"<li>{x}</li>" for x in gram) + "</ul></div></div>")

    # ---- 弟弟 ----
    h.append('<h2 style="background:%s">弟弟 Eddey · 三年级下 期末重点</h2>' % EDD)
    h.append('<div class="unit"><h3 class="e">1) 一般现在时 · 三单（老师反复练，敏感度已高）</h3><ul>'
             f'<li>{S} 只有<b>第三人称 + 单数</b>才在动词加 -s/es：He plays. She goes. Tom likes.</li>'
             f'<li>{T}{NEW("复数不加s")} <b>The boys</b> 虽是第三人称但<b>复数</b> → 动词<b>原形</b>：The boys play.</li>'
             '<li>否定/疑问用 don\'t/doesn\'t、Do/Does + 动词原形：He <b>doesn\'t</b> like… / <b>Does</b> he like…?</li></ul></div>')
    h.append('<div class="unit"><h3 class="e">2) 情态动词 can（独立语法，别和三单/does混）</h3><ul>'
             f'<li>{S} can + 动词原形：I can swim. She can swim.（can 后<b>永不</b>加 s）</li>'
             f'<li>{T}{NEW("can≠does")} can 的疑问/否定<b>不用 does</b>：Can you…? / I can\'t…（不是 Does…can）。</li></ul></div>')
    h.append('<div class="unit"><h3 class="e">3) 句子结构三态（重点熟悉）</h3>'
             '<table><tr><th>句型</th><th>be / 实义动词</th><th>can</th></tr>'
             '<tr><td>肯定</td><td>I am tall. / I like it.</td><td>I can swim.</td></tr>'
             '<tr><td>否定</td><td>I am not… / I don\'t like…</td><td>I can\'t swim.</td></tr>'
             '<tr><td>一般疑问</td><td>Are you…? / Do you like…?</td><td>Can you swim?</td></tr>'
             '<tr><td>简答</td><td>Yes, I am./No, I\'m not. — Yes, I do./No, I don\'t.</td><td>Yes, I can./No, I can\'t.</td></tr></table></div>')
    h.append('<div class="unit"><h3 class="e">4) 名词单复数标志词 + 高频拼写</h3><ul>'
             f'<li>{T} these/those/are → 后面名词用<b>复数</b>（These are apples.）。</li>'
             f'<li>{S}{NEW("拼写")} swimming pool 游泳池 · playground 操场 · English（别写成 Englih）。</li></ul></div>')
    h.append('<div class="unit"><h3 class="e">5) 听力 & 阅读提醒</h3><ul>'
             '<li>听力填词：先<b>结合上下文预测</b>空格内容，再注意语法形式（单复数/三单）。</li>'
             '<li>阅读：要<b>细心</b>，单词照抄别拼错（短文里常有正确答案原词）。</li></ul></div>')
    return "\n".join(h)

# ========================= PDF 2：冲刺背诵卡 =========================
def pdf2():
    h = ['<h1>英语期末冲刺背诵卡（30分钟必背）</h1>',
         '<p class="sub">只放最常错+最高频考点 | 期末优先 | 今晚背 → 明天考 | 哥哥 Kenton / 弟弟 Eddey</p>',
         '<div class="legend"><b>用法：</b>先读一遍 → 盖住右栏自测 → 重点记 <span class="tri">▲易错</span> 和 <span class="new">新</span>。</div>']

    # 哥哥 必背卡
    h.append('<h2 style="background:%s">哥哥 Kenton · 必背 6 张语法卡</h2>' % KEN)
    h.append('<div class="box" style="border-color:%s">' % KEN)
    h.append(f'<h3>① {T} 一般现在时 vs 现在进行时（最常错）</h3>'
             '<table><tr><th>看到标志词</th><th>用什么</th><th>例</th></tr>'
             '<tr><td>usually / every day / always</td><td>一般现在时</td><td>He <b>usually watches</b> TV.</td></tr>'
             '<tr><td>now / look! / but now</td><td>现在进行时 be+doing</td><td>Now he <b>is reading</b>.</td></tr></table>'
             f'{NEW("期末卷原题")} My father usually <b>watches</b> TV, but now he <b>is reading</b>.')
    h.append(f'<h3>② {T} 三单 s / Does / doesn\'t</h3><ul>'
             '<li>He/She/Tom + 动词<b>加s</b>：He <b>plays</b>. (不是 He play)</li>'
             f'<li>{NEW("has→have")} 疑问/否定提 <b>Does/doesn\'t</b>，动词<b>还原</b>：<b>Does</b> Alice <b>play</b>? / Eddie <b>doesn\'t have</b>…</li></ul>')
    h.append(f'<h3>③ {T} 名词单复数</h3><ul>'
             f'<li>{NEW("knife→knives")} f/fe 结尾变 ves：knife→knives, leaf→leaves。</li>'
             '<li>foot→feet；a+单数不能省；have <b>picnics</b>（单数不单用）。</li></ul>')
    h.append('<h3>④ 对划线部分提问（选对疑问词）</h3>'
             '<table><tr><th>划线信息</th><th>疑问词</th><th>例</th></tr>'
             '<tr><td>时间</td><td>What time</td><td>What time is it now?</td></tr>'
             '<tr><td>物/东西</td><td>What</td><td>What are these?</td></tr>'
             '<tr><td>方式</td><td>How</td><td>How do you go to school?</td></tr>'
             '<tr><td>正在做</td><td>What…doing</td><td>What are the Lis doing?</td></tr></table>'
             f'{T} 只换划线信息，人称(we/you)别乱改。')
    h.append('<h3>⑤ 固定搭配（背熟直接得分）</h3><ul>'
             '<li>Let\'s + 原形；can + 原形；like/go + doing（like playing / go skiing）。</li>'
             '<li>finish + doing；It\'s time <b>for</b> + 名词；否定句用 <b>any</b>。</li>'
             '<li>play <b>the</b> piano（乐器加the）/ play football（球类不加the）。</li></ul>')
    h.append(f'<h3>⑥ {T} 介词</h3> on Monday · <b>on</b> Children\'s Day(具体日期/节日) · in the morning · at home · with my parents · for + 名词。')
    h.append('</div>')

    # 哥哥 作文
    h.append('<div class="box" style="border-color:%s">' % KEN)
    h.append('<h3 class="k">★ 必考作文模板 A：My week（哥哥曾在此失分，务必背）</h3>'
             '<p class="tip">注意：标题/开头是 <b>My week</b>，不要写 On my week！用一般现在时，星期前用 on，句首大写。</p>'
             '<p class="eg">My week<br>'
             'My week is busy but happy.<br>'
             'From Monday to Friday, I go to school.<br>'
             'On Monday, I play football with my classmates.<br>'
             'On Wednesday, I read books in the library.<br>'
             'On Saturday morning, I do my homework.<br>'
             'On Sunday, I go to the park with my parents.<br>'
             'I love my week!</p>')
    h.append('<h3 class="k">作文模板 B：My favourite season（备用，套 M3U3）</h3>'
             '<p class="eg">My favourite season is summer.<br>'
             'It\'s hot and sunny. The days are long.<br>'
             'I can swim and have picnics in the park.<br>'
             'I can go to the beach and make sandcastles.<br>'
             'I like summer best!</p>')
    h.append('</div>')

    # 弟弟 必背卡
    h.append('<h2 style="background:%s">弟弟 Eddey · 必背 5 张卡</h2>' % EDD)
    h.append('<div class="box" style="border-color:%s">' % EDD)
    h.append(f'<h3>① {S} 一般现在时三单（口诀）</h3>'
             '<p><b>第三人称 + 单数 才加 s</b>；缺一个就不加。</p><ul>'
             '<li>He/She/It/Tom → 加s：She <b>goes</b>. Tom <b>likes</b>.</li>'
             f'<li>{T}{NEW("复数不加s")} <b>The boys</b> 是复数 → 原形：The boys <b>play</b>.</li></ul>')
    h.append(f'<h3>② {T}{NEW("can≠does")} 情态动词 can（别和 does 混）</h3><ul>'
             '<li>can + 原形：I can swim. She can swim.（can 后<b>不加 s</b>）</li>'
             '<li>问/否<b>用 can 自己</b>，<b>不用 does</b>：Can you…? / I can\'t…（错：Does she can…）</li></ul>')
    h.append('<h3>③ 句子三态（盖住自测）</h3>'
             '<table><tr><th></th><th>实义动词</th><th>can</th></tr>'
             '<tr><td>肯定</td><td>I like it.</td><td>I can swim.</td></tr>'
             '<tr><td>否定</td><td>I don\'t like it.</td><td>I can\'t swim.</td></tr>'
             '<tr><td>疑问</td><td>Do you like it?</td><td>Can you swim?</td></tr>'
             '<tr><td>简答</td><td>Yes, I do./No, I don\'t.</td><td>Yes, I can./No, I can\'t.</td></tr></table>')
    h.append(f'<h3>④ {T} 单复数标志词 + 拼写</h3><ul>'
             '<li>these/those/are 后名词用<b>复数</b>：These are books.</li>'
             f'<li>{NEW("拼写")} swimming pool · playground · English（不是 Englih）。</li></ul>')
    h.append('<h3>⑤ 听力/阅读小贴士</h3><ul>'
             '<li>听力填词：先<b>预测</b>再听，注意语法（单复数/三单）。</li>'
             '<li>阅读：<b>细心</b>，照抄短文里的词别拼错。</li></ul>')
    h.append('</div>')

    # 弟弟 作文
    h.append('<div class="box" style="border-color:%s">' % EDD)
    h.append('<h3 class="e">★ 必考作文模板：My day / I can（弟弟背这套句型）</h3>'
             '<p class="tip">用一般现在时；想拼不出的词换成会拼的；记得 I/he 的三单区别。</p>'
             '<p class="eg">Myself<br>'
             'My name is Eddey. I am nine.<br>'
             'I like sports. I can swim and play football.<br>'
             'I go to school from Monday to Friday.<br>'
             'I play in the playground with my friends.<br>'
             'On Sunday, I swim in the swimming pool.<br>'
             'I can\'t cook, but I can ride a bike.<br>'
             'I am a happy boy!</p>')
    h.append('</div>')
    return "\n".join(h)

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    p1 = os.path.join(OUT, "英语期末复习重点_单元梳理_两娃.pdf")
    p2 = os.path.join(OUT, "英语期末冲刺背诵卡_两娃.pdf")
    n1 = render(pdf1(), p1)
    n2 = render(pdf2(), p2)
    print("PDF1:", p1, n1, "页")
    print("PDF2:", p2, n2, "页")
