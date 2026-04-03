import pytest
from app import bonjour, calculer_remise, calculer_tva


def test_bonjour():
    """Test la fonction bonjour"""
    assert bonjour() == "Bonjour, monde!"


def test_calculer_remise():
    """Test la fonction calculer_remise avec une réduction de 10%"""
    result = calculer_remise(100, 0.10)
    assert result == 90


def test_calculer_tva():
    """Test la fonction calculer_tva avec un taux de 20%"""
    result = calculer_tva(100, 0.20)
    assert result == 120
