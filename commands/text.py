from .base import *

class Text(Base):
	def __init__(self):
		self.class_name = "te"

	# te.language
	def language(self) -> str:
		"""
		`te.language`

		The code for the language selected by the player in settings. Possible values:

		`EN`, `PT-BR`, `ZH-CN`, `ZH-TW`, `FR`, `DE`, `RU`, `ES-LA`, `ES-EU`, `JP`, `KR` and `TK`.
		"""
		return str(self.call("language"))
	
	# te.xt
	def xt(self, text:str) -> str:
		"""
		Translates a given English text into the player's selected language. If a translated version is not found, then the input text is returned instead. Alternatively, a text identifier (TID) can be used as input--albeit the exhausting list of TIDs is beyond the scope of this manual.
		"""
		return str(self.call("xt", text))
	
	# te.GetTID
	def GetTID(self, text:str) -> str:
		"""
		`te.GetTID(str)`

		Returns the text identifier (TID) for a given text. The input text is expected in the language selected by the player.
		"""
		return str(self.call("GetTID", text))
	
	# te.ToEnglish
	def ToEnglish(self, text:str) -> str:
		"""
		`te.ToEnglish(str)`

		Translates a given text from the player's selected language into the original English text. If a translated version is not found, then the input text is returned instead.
		"""
		return str(self.call("ToEnglish", text))
	
te = Text()