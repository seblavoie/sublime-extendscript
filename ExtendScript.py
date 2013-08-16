import os
import sys
import fileinput
import re
import shutil
import subprocess
import sublime
import sublime_plugin

class ExtendScriptCommand(sublime_plugin.TextCommand):
    
    def init(self):
        self.currentFile = self.view.file_name()
        self.currentPath = os.path.dirname(self.currentFile)
        self.settings    = sublime.load_settings("ExtendScript.sublime-settings")

    def copyToSoftwareFolder(self, softwarePath):
        # Changing the extension
        scriptFolderPath = self.settings.get(softwarePath + '_path')
        file_name = re.sub(r'.*/(.*)\..*$', r'\1.jsx', self.currentFile)
        self.destination_file = scriptFolderPath + file_name
        
        # Copying the file to desination
        shutil.copyfile(self.currentFile, self.destination_file)


    def compileEsFile(self):
        file_handle = open(self.destination_file, 'r')
        file_string = file_handle.read()
        file_handle.close()

        file_output = ""

        for line in file_string.splitlines():
            file_output = file_output + '\n' + self.makeReplacements(line)
        
        file_handle = open(self.destination_file, 'w')
        file_handle.write(file_output)
        file_handle.close()

    
    def makeReplacements(self, line):
        output = line

        if self.settings.get('compile_includes'):
            if re.match(r'.*#include', line):
                output = self.replaceIncludes(line)

        if self.settings.get('set_debug_false'):
            if re.match(r'.*debug = .*', line):
                output = self.replaceDebug(line)

        return output

    
    def replaceIncludes(self, line):
        path = re.sub(r'.*#include \"(.*)\";?', r'\1', line)
        path = self.currentPath + "/" + path
        with open(os.path.abspath(path)) as f:
            fileContent = f.read()
            
        return fileContent

    
    def replaceDebug(self, line):
        return re.sub(r'debug = true', r'debug = false', line)



class BuildForIndesign(ExtendScriptCommand):
    def run(self, edit):
        self.init()
        self.copyToSoftwareFolder('id')
        self.compileEsFile()

class BuildForIllustrator(ExtendScriptCommand):
    def run(self, edit):
        self.init()
        self.copyToSoftwareFolder('ai')
        self.compileEsFile()

class BuildForPhotoshop(ExtendScriptCommand):
    def run(self, edit):
        self.init()
        self.copyToSoftwareFolder('ps')
        self.compileEsFile()
    
class BuildForAfterEffects(ExtendScriptCommand):
    def run(self, edit):
        self.init()
        self.copyToSoftwareFolder('ae')
        self.compileEsFile()
