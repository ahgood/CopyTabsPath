import sublime
import sublime_plugin
import os


class CopyTabsPathCommand(sublime_plugin.WindowCommand):

    def run(self):

        file_path = ''

        for file in self.window.views():

            path = file.file_name()

            '''
            Close the tab if all of the following are true:
                * File still exists
            '''
            if (path
                and os.path.exists(path) == True):                    
                    file_path += path + '\n'
        
        sublime.set_clipboard(file_path)
