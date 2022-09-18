import sys
from abc import ABC

import pywikibot
from pywikibot import APISite, Page
from pywikibot.bot import SingleSiteBot
from pywikibot.pagegenerators import PreloadingGenerator

from bots.isbn import treat_isbn, ISBN_BOT_SUMMARY
from bots.link_adjust import treat_links, LINK_ADJUST_BOT_SUMMARY
from utils.config import get_data_path, get_rate_limit
from utils.sites import mgp


def filter_recent_changes(resume_id: int, recent_changes_generator):
    existing_titles = set()
    for item in recent_changes_generator:
        if resume_id is None:
            pywikibot.error("Don't know where to resume. Reading the past 5000 changes")
            resume_id = item['rcid'] - 5000
        page_title = item['title']
        if page_title in existing_titles:
            continue
        if item['rcid'] < resume_id:
            break
        existing_titles.add(page_title)
        yield item


class RecentChangesBot(SingleSiteBot, ABC):
    def __init__(self, bot_name: str, resume_id: int = None, site: APISite = mgp, group_size: int = get_rate_limit(),
                 ns: str = "0", **kwargs):
        super(RecentChangesBot, self).__init__(site=site, **kwargs)
        self.group_size = group_size
        self.resume_file = get_data_path().joinpath(bot_name + "_resume.txt")
        if self.resume_file.exists() and resume_id is None:
            try:
                with open(self.resume_file, "r") as f:
                    resume_id = int(f.read())
            except Exception as e:
                pywikibot.error(e)
        self.gen = filter_recent_changes(resume_id,
                                         site.recentchanges(namespaces=ns, bot=False, redirect=False,
                                                            changetype='edit|new'))
        self._start_ts = pywikibot.Timestamp.now()

    def run(self) -> None:
        self.setup()
        changes = list(self.gen)
        changes.reverse()
        pywikibot.output(f"Patrolling {len(changes)} recently changed pages")
        if len(changes) > 0:
            pywikibot.output(f"Examining pages with rcid from {changes[0]['rcid']} to {changes[-1]['rcid']}")
        gen = PreloadingGenerator((Page(source=self.site, title=item['title']) for item in changes),
                                  groupsize=self.group_size)
        for index, page in enumerate(gen):
            try:
                self.treat(page)
            except Exception as e:
                print(e)
            with open(self.resume_file, "w") as f:
                f.write(str(changes[index]['rcid']))

        last_entry = changes[-1]
        pywikibot.output(f"Last page is titled {last_entry['title']} with rcid {last_entry['rcid']} "
                         f"modified on {last_entry['timestamp']}")
        self.exit()


def patrol_recent_changes():
    bots = {
        'link_adjust': (treat_links, LINK_ADJUST_BOT_SUMMARY),
        'isbn': (treat_isbn, ISBN_BOT_SUMMARY)
    }
    args = sys.argv[2:]
    if len(args) > 0:
        bots = [(k, v) for k, v in bots.items() if k in args]
    pywikibot.output("Running " + ", ".join(bots.keys()))
    assert len(bots) > 0

    def treat_page(page: Page):
        summaries = []
        for func, summary in bots.values():
            text = func(page.text)
            if text != page.text:
                summaries.append(summary)
                page.text = text
        if len(summaries) > 0:
            page.save(summary="；".join(summaries), watch="nochange", minor=True,
                      botflag=True, tags="Bot")

    bot = RecentChangesBot(bot_name="recent_changes")
    bot.treat = treat_page
    bot.run()