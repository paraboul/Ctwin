import sublime, sublime_plugin, os

class CHeaderEvents(sublime_plugin.EventListener):
#	def on_selection_modified(self, view):
#		win = view.window()
#		view.run_command("clang_goto_def")
#		win.focus_view(view)

	def on_activated(self, view):
		win = view.window()
		if view.file_name() == None:
			return
		header = os.path.splitext(view.file_name())[0] + ".h"
		origin = os.path.splitext(view.file_name())[0] + ".c"
		if  view.file_name() == header or \
			(win.active_view_in_group(1) and \
			win.active_view_in_group(1).file_name() == header):
			return

		view.window().set_layout({
                                "cols": [0.0, 0.5, 1.0],
                                "rows": [0.0, 1.0],
                                "cells": [[0, 0, 1, 1], [1, 0, 2, 1]]
                            })

		if os.path.exists(header):
			def openheader():
				newview = win.open_file(header)
				win.focus_view(view)
				win.set_view_index(newview, 1, 0)

			sublime.set_timeout(openheader, 0)
