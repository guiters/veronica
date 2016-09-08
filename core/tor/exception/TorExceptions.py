import stem

class TorConnectionException(stem.SocketError):
	pass

class MissingItem(Exception):
	pass