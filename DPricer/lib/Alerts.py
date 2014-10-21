# coding=utf-8
__author__ = 'F.Marouane'


class Alerts(object):
    """
    Classe qui représente les alertes de l'application.
    """
    _alerts = {}

    def __init__(self):
        pass

    def launch_alerts(self):
        pass

    def create_alert(self):
        pass

    def load_alerts(self):
        pass

    def save_alerts(self):
        pass


class CouponAlert(Alerts):
    """
    Classe qui représente les alertes liées aux futures tombées de coupon.
    """
    def __init__(self):
        pass


class AssetAlert(Alerts):
    """
    Classe qui représente les alertes liées aux futures échéances des actifs.
    """
    def __init__(self):
        pass

    def check_assets(self):
        pass