from ergonsideration.checker import Checker

import psutil

class Rainbow6SiegeStatus(Checker):
	def is_running(self) -> bool:
		return "RainbowSix.exe" in (program.name() for program in psutil.process_iter(attrs=['name']))

	def get_busy_status(self, busy):
		''' I don't want to risk any anti-cheat stuff to see if the user is in a match, so I'll
		just assume you're busy if you're in game.
		'''
		busy.value = True