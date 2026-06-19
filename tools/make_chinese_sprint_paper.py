# -*- coding: utf-8 -*-
"""
哥哥 Kenton · 语文期末冲刺卷（四下·五~八单元）——按他实际易错点定制。
来源：基础复习补充卷 + 第五六单元卷(9号) + 第七八单元卷(1/2号) 的错题归档。
重点：默写与积累(多)、转述句专项(多)，并把各类错题整合到同一张卷。
输出：papers/语文期末冲刺卷_哥哥Kenton.pdf（含末页参考答案，家长核对）
依赖：PyMuPDF（自带 CJK 回退字体）。内容均为通用语文知识点+小名，无身份信息。
"""
import fitz, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "papers")
INK = "#2f6fb3"  # 哥哥 青蓝

CSS = """
* { font-family: sans-serif; }
body { font-size: 11pt; line-height: 1.7; color:#1a1a1a; }
h1 { font-size: 18pt; margin: 0 0 2pt 0; }
.sub { color:#555; font-size:9.5pt; margin:0 0 8pt 0; }
h2 { font-size: 13pt; margin: 13pt 0 5pt 0; padding:4pt 9pt; color:#fff; background:#2f6fb3; border-radius:6px; }
h2.ans { background:#7a7a7a; }
.tip { font-size:9.5pt; color:#444; background:#eef3f9; border:1px solid #d6e3f0; border-radius:6px; padding:6pt 9pt; margin:4pt 0 8pt 0; }
.q { margin:7pt 0; }
.qn { font-weight:bold; color:#2f6fb3; }
.blank { letter-spacing:2px; }
.sp { display:block; height:2pt; }
.hr { border-bottom:1px solid #bbb; }
ol { margin:3pt 0 3pt 0; padding-left:20pt; }
li { margin:5pt 0; }
.ans-body { font-size:10pt; color:#333; }
.lab { font-weight:bold; color:#b35900; }
.box { border:1px solid #d6e3f0; border-radius:6px; padding:5pt 9pt; margin:5pt 0; }
"""

U = "＿＿＿＿"          # 短填空
UU = "＿＿＿＿＿＿＿＿"   # 长填空
LINE = "＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿"  # 整行

def render(html, path):
    story = fitz.Story(html=html, user_css=CSS)
    MED = fitz.paper_rect("a4"); where = MED + (42, 38, -42, -42)
    w = fitz.DocumentWriter(path); more = 1
    while more:
        dev = w.begin_page(MED); more, _ = story.place(where); story.draw(dev); w.end_page()
    w.close()
    d = fitz.open(path); n = d.page_count; d.close(); return n

h = []
h.append('<h1>哥哥 Kenton · 语文期末冲刺卷</h1>')
h.append('<p class="sub">四年级下 · 五~八单元 ｜ 按你的实际易错点定制（默写·转述句为重点） ｜ 姓名：______ 日期：______ 得分：______</p>')
h.append('<div class="tip">说明：这张卷子把你最近五六七八单元卷子里<b>错过的题型</b>整合到一起，<b>默写和转述句特意多出了一些</b>。先独立做，做完用最后一页的参考答案对照、把错的订正两遍。</div>')

# 一、字音字形
h.append('<h2>一、字音字形（你易错的，先圈再改）</h2>')
h.append('<div class="q"><span class="qn">1.</span> 用「√」选出加点字的正确读音：</div>')
h.append('<ol>'
 '<li>脸颊（jiá ／ xiá）　禁止（jīn ／ jìn）　冲着（chōng ／ chòng）　倔强（juè ／ jué）</li>'
 '<li>刹那间（chà ／ shà）　广为流传（chuán ／ zhuàn）　不见经传（chuán ／ zhuàn）</li>'
 '<li>盛名（chéng ／ shèng）　丝毫不差（chā ／ chà）　负载（zǎi ／ zài）　单于（dān ／ chán）</li>'
 '</ol>')
h.append('<div class="q"><span class="qn">2.</span> 改正下列词语中的错别字，把正确的写在括号里：</div>')
h.append('<ol>'
 '<li>钱坤（　　　）　不解之迷（　　　）　状丽（　　　）　心悦城服（　　　）</li>'
 '<li>维持（　　　对/错）　秩序（　　　对/错）　调遺（　　　）　摧毁（　　　对/错）</li>'
 '</ol>')

# 二、默写与积累（重点·多题）
h.append('<h2>二、默写与积累（重点 ★，多写几遍记牢）</h2>')
h.append('<div class="tip">提示：注意易错字——<b>乾坤、冰心、玉壶、囊、萤、勤、悲</b>，一个字写错整句不得分。</div>')
h.append('<div class="q"><span class="qn">古诗文默写：</span></div>')
h.append('<ol>')
h.append('<li>《囊萤夜读》：胤恭勤不倦，' + U + '。家贫不常得油，' + LINE + '，以夜继日焉。</li>')
h.append('<li>《芙蓉楼送辛渐》：寒雨连江夜入吴，' + UU + '。洛阳亲友如相问，' + UU + '。</li>')
h.append('<li>《墨梅》：我家洗砚池头树，' + UU + '。不要人夸好颜色，' + UU + '。</li>')
h.append('<li>《长歌行》：百川东到海，' + U + '？少壮不努力，' + UU + '。</li>')
h.append('<li>《塞下曲》：月黑雁飞高，单于夜遁逃。欲将轻骑逐，' + UU + '。</li>')
h.append('<li>《独坐敬亭山》：众鸟高飞尽，' + UU + '。相看两不厌，' + UU + '。</li>')
h.append('<li>治学名联（韩愈）：' + UU + '，学海无涯苦作舟。</li>')
h.append('</ol>')
h.append('<div class="q"><span class="qn">文学常识填空（作者 / 国家）：</span></div>')
h.append('<ol>'
 '<li>《海上日出》——作者（　　　　）；《记金华的双龙洞》——作者（　　　　）。</li>'
 '<li>《海的女儿》《卖火柴的小女孩》——作者（　　　　），（　　　）国人，被称为「　　　　　　」。</li>'
 '<li>《诺曼底号遇难记》——作者（　　　　）；《巨人的花园》——作者（　　　　）。</li>'
 '</ol>')
h.append('<div class="q"><span class="qn">古文字义《囊萤夜读》：</span> 勤（　　）　倦（　　）　通（　　）　贫（　　）　练囊（　　　　）　盛（　　）</div>')

# 三、转述句专项（重点·多题）
h.append('<h2>三、转述句专项（重点 ★，把引述句改成转述句）</h2>')
h.append('<div class="box tip">改转述「三步」：① 冒号、引号 → 逗号；② 引号里的「我/我们」→ 说话人（他/她/名字），「你/你们」→ 听话人；③ 问句、命令、感叹按<b>陈述</b>语气说，意思不变。时间词也要变：<b>今天→那天、明天→第二天</b>。</div>')
h.append('<ol>')
for s in [
 '营参谋长对黄继光说：「我相信你能完成任务。」',
 '老师对小明说：「我教你做这道题。」',
 '妈妈对我说：「你今天要早点回家。」',
 '黄继光坚定地说：「我一定要拿下零号阵地。」',
 '哈尔威船长大声吼道：「大家安静，让妇女先走！」',
 '雨来说：「我们爱自己的祖国。」',
 '小仲马对父亲说：「我要靠自己的努力写作。」',
 '渔夫对桑娜说：「你看着办吧。」',
 '父亲对我说：「我明天带你去看双龙洞。」',
 '同桌对我说：「我把这本书借给你。」',
]:
    h.append('<li>' + s + '<span class="sp"></span>' + LINE + LINE[:18] + '</li>')
h.append('</ol>')

# 四、其他错题精选
h.append('<h2>四、其他错题精选（各类一起练）</h2>')
h.append('<div class="q"><span class="qn">1.</span> 下列句子<b>不是</b>比喻句的一项是（　　）<br>'
 'A. 沉沉的夜雾中冒出一枚黑点，好似一个幽灵，又仿佛一座山峰。<br>'
 'B. 人们透过阴惨惨的薄雾，凝视着那尊黑色的雕像徐徐沉入大海。<br>'
 'C. 子弹像冰雹一样射来。　D. 昆明湖静得像一面镜子。</div>')
h.append('<div class="q"><span class="qn">2.</span> 给加点字选择正确的解释（填序号）：<br>'
 '「奇观」的「观」：①看　②景象　③对事物的认识。（　　）　'
 '「重力」的「重」：①重量大　②程度深　③重复。（　　）</div>')
h.append('<div class="q"><span class="qn">3.</span> 照样子，写一组<b>连续的动作</b>（用上 3~4 个动词）。<br>'
 '例：他勇敢地抓住窗框，两只脚有力地踩着车厢，攀上了窗口。<br>'
 '我：' + LINE + LINE + '</div>')
h.append('<div class="q"><span class="qn">4.</span> 判断对错（对「√」错「×」）：<br>'
 '（1）哈尔威船长用自己的生命，履行了一个做人之道。（　　）<br>'
 '（2）《巨人的花园》告诉我们：一个人犯了错，应该及时改正。（　　）<br>'
 '（3）「子弹像冰雹一样射来」运用了打比方，写出子弹又多又猛。（　　）</div>')
h.append('<div class="q"><span class="qn">5.</span> 阅读答题（人物品质题，按点答）：<b>小仲马是个怎样的人？请结合短文内容写一写。</b><br>'
 '<span style="color:#555;font-size:9.5pt">点拨：先写品质词（如：自强自立、不靠父亲、坚持不懈），再举短文里的一件事做依据，至少写两点。</span><br>'
 + LINE + LINE + LINE[:14] + '</div>')

# 五、参考答案
h.append('<h2 class="ans">五、参考答案（家长核对用）</h2>')
h.append('<div class="ans-body">')
h.append('<p><span class="lab">一、字音字形</span><br>'
 '1. 脸颊jiá｜禁止jìn｜冲着chòng｜倔强jué｜刹那chà｜广为流传chuán｜不见经传zhuàn｜盛名shèng｜丝毫不差chà｜负载zài｜单于chán。<br>'
 '2. 乾坤｜不解之谜｜壮丽｜心悦诚服｜维持(对)｜秩序(对)｜调遣｜摧毁(对)。</p>')
h.append('<p><span class="lab">二、默写与积累</span><br>'
 '1. 博学多通；夏月则练囊盛数十萤火以照书。<br>'
 '2. 平明送客楚山孤；一片冰心在玉壶。<br>'
 '3. 朵朵花开淡墨痕；只留清气满乾坤。<br>'
 '4. 何时复西归；老大徒伤悲。<br>'
 '5. 大雪满弓刀。<br>'
 '6. 孤云独去闲；只有敬亭山。<br>'
 '7. 书山有路勤为径。<br>'
 '文学常识：巴金；叶圣陶；安徒生，丹麦，世界童话（之王）；雨果；王尔德。<br>'
 '古文字义：勤=勤勉；倦=疲倦；通=通晓；贫=贫穷；练囊=白绢做的口袋；盛=装。</p>')
h.append('<p><span class="lab">三、转述句</span>（意思对即可，重点看人称/标点/语气）<br>'
 '1. 营参谋长对黄继光说，他相信黄继光能完成任务。<br>'
 '2. 老师对小明说，他教小明做这道题。<br>'
 '3. 妈妈对我说，我那天要早点回家。<br>'
 '4. 黄继光坚定地说，他一定要拿下零号阵地。<br>'
 '5. 哈尔威船长大声吼道，让大家安静，让妇女先走。<br>'
 '6. 雨来说，他们爱自己的祖国。<br>'
 '7. 小仲马对父亲说，他要靠自己的努力写作。<br>'
 '8. 渔夫对桑娜说，让她看着办。<br>'
 '9. 父亲对我说，他第二天带我去看双龙洞。<br>'
 '10. 同桌对我说，他把那本书借给我。</p>')
h.append('<p><span class="lab">四、其他</span><br>'
 '1. B（B 是「凝视雕像」无比喻）。　2. ②；①。　3. 连续动作言之成理即可（动词≥3、通顺）。<br>'
 '4.（1）√　（2）√　（3）√。　5. 品质词+事例，至少两点（如：自强自立——用笔名投稿不靠父亲名气；坚持不懈——面对多次退稿仍坚持创作）。</p>')
h.append('</div>')

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    p = os.path.join(OUT, "语文期末冲刺卷_哥哥Kenton.pdf")
    n = render("\n".join(h), p)
    print("生成:", p, n, "页")
