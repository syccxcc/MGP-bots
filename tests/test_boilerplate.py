import re
from unittest import TestCase

from bots.boilerplate import treat_boilerplate


class TestBoilerplate(TestCase):
    def test_keep(self):
        strings = ['<!-- 一些注释 -->', """|相关作品     = <!--如果使用默认配色，保留这里的注释。
|标题颜色     = 
|左栏颜色     = 
|标题字体颜色 = -->
}}""",
                   "aa<!--]]-->aa"]
        for s in strings:
            self.assertEqual(s,
                             treat_boilerplate(s))

    def test_boilerplate(self):
        original = "|图片说明=<!-- 写在图片下方的注释，可不写。 -->啊"
        self.assertEqual("|图片说明=啊",
                         treat_boilerplate(original))

    def test_long(self):
        original = """{{不完整}}

{{人物信息
|image=Eculilia.jpeg
|图片说明=<!-- 写在图片下方的注释，可不写。 -->
|本名=尤珂莉莉娅
|别号=境界的魔物、{{黑幕|门酱}}
|发色=紫
|瞳色=黄
|身高=<!-- 請输入一个整数，单位为CM 例如，输入“145”而不是“145厘米”、“145CM” -->
|体重=<!-- 請输入一个整数，单位为KG 例如，输入“49”而不是“49千克”、“49KG” -->
|三围=<!-- 格式为B:XX W:XX  H:XX  -->
|年龄=<!-- 請输入X岁中的“X” -->
|生日=<!-- X月X日 用了本行就删去下面一行 用了本行就删去下面一行 用了本行就删去下面一行-->
|特殊生日=<!--仅用于人物具有特殊生日的情况下使用，例如角色的世界是古代或者异世界等格里高利历不适用的情况，填写这一项目就不需要填写生日项目。 用了本行就删去上面一行 用了本行就删去上面一行 用了本行就删去上面一行-->
|星座=<!--請使用{{Astrology}}模板-->
|血型=<!--填入类似于“B”这样的文字。-->
|声优=<!-- 输入声优名，会自动生成链接和分类。 用了本行就删去下面一行 用了本行就删去下面一行 用了本行就删去下面一行-->
|多位声优=<!-- 如果该角色有多位声优配音，填写这一项目就不需要填写声优项目，不过需要自己添加分类，作内链。 用了本行就删去上面一行 用了本行就删去上面一行 用了本行就删去上面一行-->
|萌点=巨乳，弱娇，傲娇，异味癖，青肌
|出身地区=不明
|活动范围=魔物之国帕尔革多
|所属团体=<!-- 故事中人物的主要所属团体 -->
|个人状态={{黑幕|长住于隐之里阿斯法雷}}
|相关人士=同伴：尤珂丽丝，熟人：修格拉纳
}}

<!-- 上面模版中不使用的项目，只留空即可，请不要把项目删掉。 -->

'''尤珂莉莉娅'''是由[[はきか]]所创作的游戏'''《[[SEQUEL系列]]》'''的'''《[[SEQUEL blight]]》'''及其衍生作品的登场角色。

<!-- 编辑前可以参照其他类似条目作参考，完成后请将所有在“<! --  -- >”的文字删去，包括符号和这句话，你可以透过【显示预览】观看编辑的排版效果 -->

== 简介 ==
在游戏中，莉莉娅是魔物之国的故事的主要NPC，线索人物。

在魔物之国故事的引子中，主角一行人在卡德纳宅邸的地下探索时无意发现了莉莉娅忘记关闭的境界之门。进入境界之后与莉莉娅邂逅。但随后莉莉娅立刻便逃走了。

魔物之国故事开始后，莉莉娅利用境界之门传送到海文，将男主角绑架。但是随后拉比众人赶来闯入境界之门，最终所有人被传送到‘隐之里阿斯法雷’。

明白自己实力无法和主角组对抗的莉莉娅识趣的逃走了，在主角众在外寻找传送剑时再度返回阿斯法雷，但是不想正好撞到枪口上。被阿妮萨制服并且关进了监狱。直到后来确定安全才被释放。

身为法拉克斯，莉莉娅对玛娜的需求量相当巨大，打开境界之门需要消耗大量的玛娜，远距离传送对玛娜的需求更是苛刻。从帕尔革多传送到贝蕾特里亚已经消耗了相当的玛娜的莉莉娅，被关没多久就出现了衰弱症状，所幸有男主角贡献了部分玛娜维持住了生命。此后便长期待在阿斯法雷的家中。

莉莉娅有着纯粹的，十分温婉的个性。在被问及‘既然是魔物的话为什么不去抢夺玛娜’的时候。她回答道：“因为我太弱小，而且……我不想做伤人性命的事情。”可以看出莉莉娅实际上是十分柔弱，需要有人关怀和保护的。而过去很久以前……她的那位守护者便离她而去了……

身为法拉克斯走到哪里都会被关注，因此莉莉娅的活动范围基本仅限于阿斯法雷附近地区。不过在魔物之国的事件结束之后，也曾到贝蕾特里亚观光。{{黑幕|并且遭到了抖S里欧涅的调教}}

虽然乍一看上去是非常睿智的魔物，但是意外地会在某些时候{{黑幕|H的时候}}展露出笨拙的一面

{{黑幕|但是在第二作的时候，虽然前面有很多铺垫但是后面仅仅只是开了个传送门救了一次太子就再没戏份，在第三作甚至没被提起过一次，所以被戏称为门酱}}

== 能力 ==

境界：身为境界的魔物法拉克斯，莉莉娅拥有改变时间和空间，链接境界的能力，开启境界之门传送只是其中之一，她还可以把一个小范围的空间内物体与境界进行置换。从而‘创造’一个只属于她的个人空间。另外，传送剑的起源正是法拉克斯的能力。

== 经历 ==
在古老的时代，莉莉娅便与她的同伴尤珂丽丝一起在各个时代中旅行。

但是，她们二人被人类捕获，提取并且利用能力，制造出了现代的传送剑。强大的丽丝代替了莉莉娅被抽取了力量，弱小的莉莉娅则被扔在一边。

两人逃亡之后，继续漂流于各个时代的各个世界。最终终于碰到了唯一善待她们的人类——梅萨。

但是，此时的丽丝，已经由于失去了过多的力量，生命力开始急速消减。最终由于衰弱而撒手人寰。

弱小的莉莉娅，因为自己的弱小而活到现在，但是她一直带着内疚而活着。‘废物活得长又有什么用。’她自嘲的这句话是如此的令人心疼。

为了拯救丽丝，莉莉娅需要大量的玛娜，而在发现了一个无限的玛娜源泉之后，她便开始了她的计划，但是……？

<!--== 萌战 ==-->
== 游戏 ==
{{Hide|标题=SEQUEL blight|内容=境界的魔物尤珂莉莉娅

情报：

HP：108000   SP：8000

攻击力：460   魔攻力：480

防御力：360   魔防力：380

速度：250   运气：340



境界的魔物，于漂流地带遭遇

尤珂莉莉娅虽然渐渐获得玛娜，取回了力量。
但应该还是不足以让她回到过去的。
现在的她要么就是获得了什么别的力量，要么就是让连她自己都不知道的潜在能力暴走起来了。

魔物之国剧情的最终Boss
在游戏中，是相当强大的魔物，会施放各种牵制性技能和异常状态。



}}

{{SEQUEL blight}}


== 注释与外部链接 ==
<references />

https://twitter.com/hakika_

[[Category:SEQUEL系列]]
[[Category:BOSS]]

[[Category:SEQUEL系列]]
[[Category:BOSS]]
"""
        r = "<!--[^-<]+(<! ?--[^-<]+-- ?>)?[^-<]+-->"
        self.assertEqual(re.sub(r, "", re.sub(r, "", original)),
                         treat_boilerplate(original))
