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
                * File is not the current view in its window
            '''
            if (path
                and os.path.exists(path) == True
                and file.window() == None):                    
                    file_path += path + '\n'
        
        sublime.set_clipboard(file_path)
