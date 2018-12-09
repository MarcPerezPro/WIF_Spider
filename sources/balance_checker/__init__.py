from blockchain import blockexplorer as be
import logging
from pycoin.encoding import is_valid_wif
from pycoin.key.key_from_text import key_from_text
from sources.key_info import KeyInfo


class BalanceChecker:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def is_valid(self, wif):
        if is_valid_wif(wif):
            self.logger.info("Valid WIF: " + wif)
            return True
        else:
            self.logger.debug("Invalid WIF: " + wif)
            return False

    def get_key_info(self, wif):
        info = KeyInfo(wif=wif, pub=key_from_text(wif).address())

        bal = be.get_balance(info.pub)[info.pub]
        info.balance = bal.final_balance
        info.ntx = bal.n_tx
        info.total_received = bal.total_received

        self.logger.info("Got Key Info: " + str(info))
        return info
