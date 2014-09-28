# coding=utf-8
__author__ = 'F.Marouane'

# Ce module implémente l'ensemble des Exceptions nécessaires et significatives
# pour notre Application


class ObligationAlreadyExists(Exception):
    """
    Exception déclenchée si un actif existe déjà.
    """
    pass


class ObligationNotFound(Exception):
    """
    Exception déclenchée lorsque l'obligation est introuvable.
    """
    pass


class ObligationNonConforme(Exception):
    """
    Cette Exception représente une erreur concernant
    une saisie incorrecte d'un titre Obligataire
    Notamment,
    • D_ech < D_evaluation
    • D_ech < D_jouissance
    • D_ech < D_emission
    • Nominal <= 0
    • Taux Facial <= 0
    • Taux Actuariel <= 0
    """
    pass


class CourbeTauxIndisponible(Exception):
    """
    Cette Exception est déclenchée dans les cas suivants:
    • Si la courbe du jour n'est pas publiée
    • Si la courbe correspondant à la date fournie n'existe pas
    """
    pass


class ObligationATerme(Exception):
    """
    Exception déclenchée dans les cas suivants:
    • Si une Obligation arrive à maturité
    => alors cette dernière doit être transférée vers le cimetière des Obligations
    """
    pass


class ObligationProche(Exception):
    """
    Exception déclenchée quand la maturité d'une obligation approche
    """
    pass


class ObligationAReviser(Exception):
    """
    Exception Déclenchée lors de l'approche de la date de révision
    Exception spécifique aux Obligations Révisables
    """
    pass


class AnniversaireCoupon(Exception):
    """
    Exception déclenchée lors de la tombée d'un coupon
    """
    pass


class BamIndisponible(Exception):
    """
    Exception déclenchée si le site de la BAM ne répond à aucune requête
    """
    pass


class MailNotDefined(Exception):
    """
    Exception déclenchée quand l'adresse mail du destinataire
    ou celle du sender est indéfinie
    """
    pass


class BaseDeDonneeIncorrecte(Exception):
    """
    Exception déclenchée si la base de données est indisponible
    ou les crédentials sont incorrects
    """
    pass


class UserNotFound(Exception):
    """
    Exception Déclenchée si aucun utilisateur ne correspond à celui recherché
    """
    pass