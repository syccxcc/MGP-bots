from unittest import TestCase

from bots.link_adjust import process_text_bb, process_text_yt, process_text


class TestLinkAdjust(TestCase):
    def test_process_text_bb(self):
        # 去除t=1和p=1外的所有参数
        url = "https://www.bilibili.com/video/BV1bW4y1q79d?" \
              "spm_id_from=333.851.b_7265636f6d6d656e64.1&" \
              "t=1&vd_source=4283250c27f32cce49b24b0f6e6c149d&p=1"
        self.assertEqual(
            "https://www.bilibili.com/video/BV1bW4y1q79d?t=1&p=1",
            process_text_bb(url))
        # 无更改
        url = "https://www.bilibili.com/video/BV1bW4y1q79d"
        self.assertEqual(url, process_text_bb(url))
        url = "https://www.bilibili.com/video/BV1bW4y1q79d?t=123"
        self.assertEqual(url, process_text_bb(url))
        # 直播
        url = "https://live.bilibili.com/21996804?broadcast_type=0&is_room_feed=1&spm_id_from=333.999.0.0"
        self.assertEqual("https://live.bilibili.com/21996804",
                         process_text_bb(url))
        # 动态
        url = "https://t.bilibili.com/702110621963911221?spm_id_from=444.41.0.0"
        self.assertEqual("https://t.bilibili.com/702110621963911221",
                         process_text_bb(url))
        # 专栏
        url = "https://www.bilibili.com/read/cv3434476?from=search&spm_id_from=333.337.0.0"
        self.assertEqual("https://www.bilibili.com/read/cv3434476",
                         process_text_bb(url))
        # 处理b23.tv
        url = "https://b23.tv/t8BP0j"
        self.assertEqual("https://www.bilibili.com/video/BV1AV411h7jb?p=1",
                         process_text_bb(url))

    def test_process_text_yt(self):
        # 无更改
        url = "https://www.youtube.com/watch?v=k9jAlYmNK5A&t=12s"
        self.assertEqual(url, process_text_yt(url))
        url = "2015年8月31日发布首个[https://www.youtube.com/watch?v=MILDduR_k9c 试听曲]"
        self.assertEqual(url, process_text_yt(url))
        # 展开youtu.be
        url = "https://youtu.be/h-FccHqdLV0?t=81"
        self.assertEqual("https://www.youtube.com/watch?v=h-FccHqdLV0&t=81",
                         process_text_yt(url))
        url = "https://youtu.be/jA8M_oYpODo"
        self.assertEqual("https://www.youtube.com/watch?v=jA8M_oYpODo",
                         process_text_yt(url))
        # YouTube链接的无效参数
        url = "https://www.youtube.com/watch?v=be8wqUqDhFU&feature=youtu.be"
        self.assertEqual("https://www.youtube.com/watch?v=be8wqUqDhFU",
                         process_text_yt(url))

    def test_long(self):
        expected = """**在练自由搏击（{{lj|キックボクシング}}）{{黑幕|本想瘦腿，结果上半身变瘦}}<ref>[https://www.bilibili.com/video/BV1Jz4y1U7BA?p=1 【切片中字】胸部装甲被削弱的爱美社长？]</ref>

母亲：樱井文绘<ref>[https://www.bilibili.com/video/BV1C3411k7s9?p=1]</ref>

相关内容可见[https://www.bilibili.com/video/BV1Yg411y7xN 《深空之眼》拾梦绘卷|最优秀的女仆]

2022年8月19日[[HIKARI FIELD]]宣布将制作国际中文版，并公开了中文版开场动画<ref>{{Cite web|title=《苍之彼方的四重奏EXTRA2》国际中文版制作决定！|url=https://t.bilibili.com/696063187661881477|accessdate=2022-08-19|date=2022-08-19|language=zh}}</ref>，预计于2022年内发售。

<ref>https://www.bilibili.com/video/BV1Us411v78x?t=10&p=1</ref>

2015年8月31日发布首个[https://www.youtube.com/watch?v=MILDduR_k9c 试听曲]

** 4月10日开始与[[佐佐木未来]]、[[伊藤彩沙]]以“'''声优三姐妹 TeamY'''（[https://www.youtube.com/channel/UCtD8UMFAgAUn7sGGPK5IvAA {{lj|声优三姊妹『チームY』}}]）”组合名义Youtuber出道。

PS4上有玩《东方深秘录》。<ref>东方station 特别嘉宾上坂堇 https://www.bilibili.com/video/BV19E41157qu?t=220</ref>

车重1151KG 推重比126kg·m[https://www.bilibili.com/read/cv3434476]

[https://www.bilibili.com/video/BV1Lt4y1L7Je]"""

        original = """**在练自由搏击（{{lj|キックボクシング}}）{{黑幕|本想瘦腿，结果上半身变瘦}}<ref>[https://b23.tv/iMhxQi 【切片中字】胸部装甲被削弱的爱美社长？]</ref>

母亲：樱井文绘<ref>[https://b23.tv/zcklGO]</ref>

相关内容可见[https://www.bilibili.com/video/BV1Yg411y7xN?spm_id_from=444.42.list.card_archive.click 《深空之眼》拾梦绘卷|最优秀的女仆]

2022年8月19日[[HIKARI FIELD]]宣布将制作国际中文版，并公开了中文版开场动画<ref>{{Cite web|title=《苍之彼方的四重奏EXTRA2》国际中文版制作决定！|url=https://t.bilibili.com/696063187661881477?spm_id_from=333.999.0.0|accessdate=2022-08-19|date=2022-08-19|language=zh}}</ref>，预计于2022年内发售。

<ref>https://www.bilibili.com/video/BV1Us411v78x?spm_id_from=333.337.search-card.all.click&vd_source=99b3fa924294d33ca365ef499286ea01&t=10&p=1</ref>

2015年8月31日发布首个[https://www.youtube.com/watch?v=MILDduR_k9c 试听曲]

** 4月10日开始与[[佐佐木未来]]、[[伊藤彩沙]]以“'''声优三姐妹 TeamY'''（[https://www.youtube.com/channel/UCtD8UMFAgAUn7sGGPK5IvAA {{lj|声优三姊妹『チームY』}}]）”组合名义Youtuber出道。

PS4上有玩《东方深秘录》。<ref>东方station 特别嘉宾上坂堇 https://www.bilibili.com/video/BV19E41157qu?t=220</ref>

车重1151KG 推重比126kg·m[https://www.bilibili.com/read/cv3434476?from=search&spm_id_from=333.337.0.0]

[https://www.bilibili.com/video/BV1Lt4y1L7Je/?spm_id_from=333.788.recommend_more_video.-1&vd_source=52e727c44f740afa0d193be4aadcd11c]"""
        self.assertEqual(expected, process_text(original))