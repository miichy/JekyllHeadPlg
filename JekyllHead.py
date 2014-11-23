import sublime, sublime_plugin
import time

class HeadCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        """test doc"""
        a = time.localtime(time.time())
        b = time.strftime('%Y-%m-%d %H:%M:%S',a)
        self.view.insert(edit, 0, "---\nlayout: post \ntitle:  \ndate: %s \ncategory:  \n---\n" % (b))

class NewCommand(sublime_plugin.WindowCommand):
    def  run(self,commands):
        self.window.new_file()
        window = self.window
        for command in commands:
            command_name = command[0]
            command_args = command[1:]
            window.run_command(command_name,*command_args)