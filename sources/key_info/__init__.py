from recordtype import recordtype

fields = ['wif', 'pub', 'balance', 'ntx', 'total_received']

KeyInfo = recordtype("KeyInfo", fields, default=None)
