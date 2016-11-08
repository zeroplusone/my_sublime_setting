import sublime
import sublime_plugin
from datetime import datetime, timedelta

"""
This class is my custom plug-in in sublime Text 3.
This 'weekly_report' command is used to create template of weekly report.
"""


class WeeklyReportCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        monday = self.find_monday(datetime.today())
        sunday = monday + timedelta(days=6)
        title = monday.strftime("%Y/%m/%d") + "~" + sunday.strftime("%Y/%m/%d")

        content = self.edit_content(monday, title)
        contents = ""
        for str in content:
            contents += str
            # self.view.insert(edit, 0, str)
        self.view.run_command('insert_snippet', {'contents': contents})

    def find_monday(self, today):
        if today.weekday() > 2:
            return today - timedelta(days=7)
        else:
            return today - timedelta(days=7) - timedelta(days=today.weekday())

    def edit_content(self, monday, title):
        content = []
        content.append("---\n")
        content.append("title:" + title + "\n")
        content.append("notebook: weekly report\n")
        content.append("tags:\n")
        content.append("---\n\n")
        content.append("- [ ] //to-do\n")
        content.append("\n---------\n")

        for i in range(0, 7):
            day = monday + timedelta(days=i)
            content.append("- " + day.strftime("%m/%d") + "\n")
            content.append("    - done\n")

        content.append("\n---------\n")
        content.append("Subject: [IMSLab][Weekly Report] 林佳瑩 " + title + "\n\n")
        content.append("老師：\n這禮拜主要在\n\n")
        content.append("1. .\n")
        content.append("2. .\n")
        content.append("3. .\n")
        content.append("\n**[本週進度]**\n\n")
        content.append("1. .\n")
        content.append("2. .\n")
        content.append("\n**[下週進度]**\n\n")
        content.append("1. .\n")
        content.append("2. .\n")
        content.append("\n**[Meeting Note]**\n\n")
        content.append("- .\n\n")
        content.append("小六\n")
        return content
