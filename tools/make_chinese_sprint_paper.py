# -*- coding: utf-8 -*-
"""
哥哥 Kenton · 语文一课一练·增强版（四下 五~八单元 冲刺）。
标准（CLAUDE.md「出题难度与格式标准」）：难度对标《一课一练·增强版》，讲练合一。
- 每板块：【方法点拨】→【例·带解析】→【练：基础→巩固→拔高★】
- 来源：四下五~八单元试卷错题(基础补充卷+5/6单元卷+7/8单元卷)，在错点上加难一档。
- 重点加量：理解性默写、转述句及句式变换。
输出：papers/语文期末冲刺卷_哥哥Kenton.pdf（含末页答案与解析）
依赖：PyMuPDF（自带 CJK 回退字体）。内容均为通用语文知识点+小名，无身份信息。
"""
import fitz, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "papers")

CSS = """
* { font-family: sans-serif; }
body { font-size: 10.8pt; line-height: 1.65; color:#1a1a1a; }
h1 { font-size: 17pt; margin: 0 0 2pt 0; }
.sub { color:#555; font-size:9.3pt; margin:0 0 6pt 0; }
.lead { font-size:9.3pt; color:#444; background:#eef3f9; border:1px solid #d6e3f0; border-radius:6px; padding:5pt 9pt; margin:3pt 0 7pt 0; }
h2 { font-size: 12.5pt; margin: 12pt 0 4pt 0; padding:4pt 9pt; color:#fff; background:#2f6fb3; border-radius:6px; }
h2.ans { background:#7a7a7a; }
.method { background:#fff8e8; border:1px solid #f0dca8; border-radius:6px; padding:5pt 9pt; margin:4pt 0; font-size:9.6pt; }
.method b { color:#a8730a; }
.eg { background:#eef7ef; border:1px solid #cce6d2; border-radius:6px; padding:5pt 9pt; margin:4pt 0; font-size:9.8pt; }
.eg .l { font-weight:bold; color:#1a7f37; }
.q { margin:6pt 0; }
.qn { font-weight:bold; color:#2f6fb3; }
.star { color:#d4380d; font-weight:bold; }
ol { margin:3pt 0; padding-left:20pt; }
li { margin:5pt 0; }
.ans-body { font-size:9.6pt; color:#333; }
.lab { font-weight:bold; color:#b35900; }
"""
L = "＿＿＿＿＿＿＿＿＿＿＿＿"
LL = "＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿"

def render(html, path):
    story = fitz.Story(html=html, user_css=CSS)
    MED = fitz.paper_rect("a4"); where = MED + (40, 36, -40, -40)
    w = fitz.DocumentWriter(path); more = 1
    while more:
        dev = w.begin_page(MED); more, _ = story.place(where); story.draw(dev); w.end_page()
    w.close()
    d = fitz.open(path); n = d.page_count; d.close(); return n

S = '<span class="star">★拔高</span>'
h = []
h.append('<h1>哥哥 Kenton · 语文一课一练 · 增强版</h1>')
h.append('<p class="sub">四年级下 · 五~八单元冲刺 ｜ 讲练合一 · 难度：基础→巩固→拔高★ ｜ 姓名：____ 日期：____ 得分：____</p>')
h.append('<div class="lead">用法：每个板块先看<b>【方法点拨】</b>和<b>【例】</b>，再做<b>【练】</b>（标 ★ 的是拔高题）。先独立做，做完用最后一页<b>「答案与解析」</b>对照订正，错的订正两遍。本卷按《一课一练·增强版》难度，并把你最近的错点加难一档。</div>')

# 板块一 字音字形
h.append('<h2>一、字音字形</h2>')
h.append('<div class="method"><b>【方法点拨】</b>① 多音字"音随义变"：传 chuán(流传)/zhuàn(经传)；盛 shèng(盛名)/chéng(盛饭)；差 chà(不差)/chā(差别)/chāi(出差)；载 zài(负载)/zǎi(记载)。② 形近同音字看部首与意思：乾坤(乾 qián，与天地有关)≠钱；谜(言字旁，谜语)≠迷。</div>')
h.append('<div class="eg"><span class="l">【例】</span>"丝毫不差"的"差"读（　）。<b>解析：</b>"不差"指没有差别，读 chà。</div>')
h.append('<div class="q"><span class="qn">1.（基础）</span>用「√」选读音：脸颊(jiá／xiá)　刹那(chà／shà)　倔强(jué／juè)　单于(dān／chán)</div>')
h.append('<div class="q"><span class="qn">2.（巩固）</span>下列加点字注音<b>全对</b>的一组是（　）<br>'
 'A. 脸颊(xiá)　刹那(chà)　　B. 倔强(juè)　单于(chán)<br>'
 'C. 负载(zǎi)　盛名(chéng)　D. 广为流传(chuán)　不见经传(zhuàn)</div>')
h.append('<div class="q"><span class="qn">3.（' + S + '）</span>给加点字注音，并写出"差"的<b>三个</b>读音各组一词：<br>'
 '成绩相差(　)很大，可他答得丝毫不差(　)。　"差"：chà（　　　）／ chā（　　　）／ chāi（　　　）</div>')

# 板块二 词语·积累运用
h.append('<h2>二、词语 · 积累运用</h2>')
h.append('<div class="method"><b>【方法点拨】</b>近义词辨析看"程度＋搭配"；成语先解语素义；改错别字抓形近/同音字。关联词先判关系（假设/因果/转折/条件）。</div>')
h.append('<div class="q"><span class="qn">1.（基础）</span>改正词语中的错别字：钱坤(　　)　不解之迷(　　)　状丽(　　)　心悦城服(　　)</div>')
h.append('<div class="q"><span class="qn">2.（巩固）</span>选词填空（焦躁不安／心急如焚）：<br>'
 '①离交卷只剩两分钟，他还有一题没写，____。　②等不到孩子的消息，妈妈在屋里走来走去，____。</div>')
h.append('<div class="q"><span class="qn">3.（巩固）</span>填关联词：①（　　）明天下雨，运动会（　　）改期。　②（　　）他平时肯下功夫，（　　）成绩一直名列前茅。</div>')
h.append('<div class="q"><span class="qn">4.（' + S + '）</span>从"囊萤夜读、悬梁刺股、程门立雪"中选一个，写一句话用上它（要体现成语的意思）：<br>' + LL + '</div>')

# 板块三 古诗文·理解性默写（重点）
h.append('<h2>三、古诗文 · 理解性默写（重点 ★加量）</h2>')
h.append('<div class="method"><b>【方法点拨】</b>理解性默写＝按"提示语境"填句，不是单纯背诵——先抓诗的<b>主旨句/诗眼</b>，再对应提示。写完逐字检查易错字：<b>乾坤、冰心、玉壶、萤、练囊、悲</b>。</div>')
h.append('<div class="eg"><span class="l">【例】</span>《墨梅》中借梅花表明自己不慕虚名、只求高洁的诗句是：____，____。<b>解析：</b>不要人夸好颜色，只留清气满乾坤。</div>')
h.append('<div class="q"><span class="qn">按提示填写诗句：</span></div>')
h.append('<ol>'
 '<li>《芙蓉楼送辛渐》中表明诗人坚守高洁节操、不为世俗所染的句子：____，____。</li>'
 '<li>《囊萤夜读》中写车胤想办法借光、夜以继日读书的句子：____，____。</li>'
 '<li>《长歌行》中劝人珍惜时间、奋发努力的句子：____，____。</li>'
 '<li>《塞下曲》中表现将士顶风冒雪、英勇追敌的句子：____，____。</li>'
 '<li>《独坐敬亭山》中以山为伴、写出诗人孤独又超脱的句子：____，____。</li>'
 '<li>治学名联（韩愈）：____，学海无涯苦作舟。</li>'
 '<li>古文字义《囊萤夜读》：勤(　　)　倦(　　)　通(　　)　贫(　　)　练囊(　　　)　盛(　　)</li>'
 '<li>文学常识：《海上日出》—(　　)；《记金华的双龙洞》—(　　)；《诺曼底号遇难记》—(　　)；《海的女儿》—(　　)，是(　)国人，被称"____"。</li>'
 '<li>（' + S + '）"读书求学"主题——再写一句你知道的、与"勤奋读书"有关的诗句或名言：____。</li>'
 '</ol>')

# 板块四 句子·转述句及句式变换（重点）
h.append('<h2>四、句子 · 转述句及句式变换（重点 ★加量）</h2>')
h.append('<div class="method"><b>【方法点拨】</b>① <b>改转述三步</b>：冒号引号→逗号；"我/我们"→说话人，"你/你们"→听话人；问句/命令/感叹改成<b>陈述</b>语气、意思不变。② <b>进阶</b>：指示词也要变——今天→那天、明天→第二天、这→那、来→去。③ <b>反问改陈述</b>：去掉"难道…吗/怎么…呢"，意思反过来说。</div>')
h.append('<div class="eg"><span class="l">【例】</span>父亲对我说："我明天带你去看双龙洞。"→ 父亲对我说，他第二天带我去看双龙洞。<b>解析：</b>我→他、你→我、明天→第二天。</div>')
h.append('<div class="q"><span class="qn">按要求改写句子：</span></div>')
h.append('<ol>'
 '<li>营参谋长对黄继光说："我相信你能完成任务。"（改转述句）<br>' + LL + '</li>'
 '<li>妈妈对我说："你今天要把作业做完。"（改转述句，注意时间词）<br>' + LL + '</li>'
 '<li>哈尔威船长大声吼道："大家安静，让妇女先走！"（改转述句）<br>' + LL + '</li>'
 '<li>渔夫对桑娜说："你看着办吧。"（改转述句）<br>' + LL + '</li>'
 '<li>小仲马对父亲说："我要靠自己的努力写作。"（改转述句）<br>' + LL + '</li>'
 '<li>（反问改陈述）这么重的箱子，难道一个人搬得动吗？<br>' + LL + '</li>'
 '<li>（反问改陈述）我们怎么能忘记英雄的牺牲呢？<br>' + LL + '</li>'
 '<li>（' + S + '：陈述改反问）我们应该珍惜今天的幸福生活。<br>' + LL + '</li>'
 '<li>（' + S + '：缩句）英勇的黄继光顽强地爬向敌人的火力点。<br>' + LL + '</li>'
 '</ol>')

# 板块五 阅读理解（课外·梯度设问）
h.append('<h2>五、阅读理解（课外短文 · 梯度设问）</h2>')
h.append('<div class="method"><b>【方法点拨】</b>先读题再读文、回原文圈证据；<b>概括</b>用"谁＋做什么＋结果"；<b>赏析</b>点明修辞/写法＋作用；<b>开放题</b>＝观点＋理由＋联系自己。</div>')
h.append('<div class="eg"><b>萤囊苦读</b><br>'
 '　　东晋的车胤，小时候家里穷，买不起灯油。一个夏夜，他看见院子里点点流萤一闪一闪，忽然想到：把萤火虫装进口袋，不就有了一盏"灯"吗？于是他捉来几十只萤火虫，装进白绢做的小口袋里，借着那微弱的光读书，夜以继日。后来，车胤成了博学多才的人。<u>一只小小的萤火虫，照亮的不只是书页，更是一个不肯向困难低头的少年。</u></div>')
h.append('<ol>'
 '<li>（基础·词句）"夜以继日"在文中的意思是：____。</li>'
 '<li>（巩固·概括）用一句话概括短文的主要内容：____。</li>'
 '<li>（巩固·赏析）画线句好在哪里？请简要说一说：____。</li>'
 '<li>（' + S + '·开放）读了车胤的故事，结合你自己的学习，说说你受到的启发：<br>' + LL + '</li>'
 '</ol>')

# 板块六 语言运用·小练笔
h.append('<h2>六、语言运用 · 小练笔</h2>')
h.append('<div class="method"><b>【方法点拨】</b>写连续动作按"先…接着…然后…最后"的顺序，动词要准确；人物描写可加一个比喻让画面更生动。</div>')
h.append('<div class="q"><span class="qn">1.（巩固·仿写）</span>照样子写一组<b>连续动作</b>（用上 4 个以上动词）。例：他抓住窗框，踩着车厢，攀上了窗口。<br>我：' + LL + '</div>')
h.append('<div class="q"><span class="qn">2.（' + S + '·小练笔，50字内）</span>用上<b>两个连续动作</b>和<b>一个比喻</b>，写"妈妈下班回家"的一个小片段：<br>' + LL + LL + '</div>')

# 答案与解析
h.append('<h2 class="ans">答案与解析（家长核对用）</h2>')
h.append('<div class="ans-body">')
h.append('<p><span class="lab">一、字音字形</span><br>'
 '1. jiá／chà／jué／chán。　2. <b>D</b>（A 颊 jiá、B 倔 jué、C 载 zài 盛 shèng 均错）。　'
 '3. 相差 chā、不差 chà；"差"：chà(差不多／不差)、chā(差别／差距)、chāi(出差／差遣)。</p>')
h.append('<p><span class="lab">二、词语·积累运用</span><br>'
 '1. 乾坤／不解之谜／壮丽／心悦诚服。　2. ①心急如焚 ②焦躁不安（①程度更急、火烧火燎；②侧重坐立不安）。　'
 '3. ①如果…就… ②因为…所以…。　4. 言之成理即可（须体现成语意思，如"他像车胤囊萤夜读那样刻苦"）。</p>')
h.append('<p><span class="lab">三、理解性默写</span>（错一字即不得分）<br>'
 '1. 洛阳亲友如相问，一片冰心在玉壶。　2. 夏月则练囊盛数十萤火以照书，以夜继日焉。　'
 '3. 少壮不努力，老大徒伤悲。　4. 欲将轻骑逐，大雪满弓刀。　5. 相看两不厌，只有敬亭山。　'
 '6. 书山有路勤为径。　7. 勤=勤勉；倦=疲倦；通=通晓；贫=贫穷；练囊=白绢做的口袋；盛=装。　'
 '8. 巴金；叶圣陶；雨果；安徒生，丹麦，"世界童话之王"。　9. 开放（如：读书破万卷，下笔如有神／书山有路勤为径）。</p>')
h.append('<p><span class="lab">四、句式变换</span>（意思对、人称/标点/语气对即可）<br>'
 '1. 营参谋长对黄继光说，他相信黄继光能完成任务。　2. 妈妈对我说，我那天要把作业做完。　'
 '3. 哈尔威船长大声吼道，让大家安静，让妇女先走。　4. 渔夫对桑娜说，让她看着办。　'
 '5. 小仲马对父亲说，他要靠自己的努力写作。　6. 这么重的箱子，一个人搬不动。　'
 '7. 我们不能忘记英雄的牺牲。　8. 我们怎么能不珍惜今天的幸福生活呢？　9. 黄继光爬向火力点。</p>')
h.append('<p><span class="lab">五、阅读</span><br>'
 '1. 日夜不停（连着白天黑夜地读）。　2. 车胤幼时家贫，借萤火虫的微光夜以继日地读书，终成博学之人。　'
 '3. 用"不只是…更是…"递进，由"照亮书页"升华到"照亮不肯向困难低头的少年"，点明并赞扬车胤刻苦不屈的精神。　4. 开放（观点+理由+联系自己，言之成理）。</p>')
h.append('<p><span class="lab">六、语言运用</span><br>'
 '1. 动词≥4、顺序连贯即可。　2. 含两个连续动作+一个比喻、通顺即可。</p>')
h.append('</div>')

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    p = os.path.join(OUT, "语文期末冲刺卷_哥哥Kenton.pdf")
    n = render("\n".join(h), p)
    print("生成:", p, n, "页")
