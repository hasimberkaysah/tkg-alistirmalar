# Hafta 3: Testleri bu dosyaya SİZ yazacaksınız.
#
# Aşağıda örnek olarak bir test var. Yanına her fonksiyon için kendi testlerinizi ekleyin.
# Çalıştırmak için bu klasörde:  python -m pytest -v

import pytest

from alistirma import kargo_ucreti, bilet_fiyati, ortalama


def test_kargo_buyuk_sipariste_ucretsiz():
    assert kargo_ucreti(800) == 0
    assert kargo_ucreti(500) == 0
    assert kargo_ucreti(499) == 50
    assert kargo_ucreti(45) == 50
    assert kargo_ucreti(0) == 0
    assert kargo_ucreti(-10) == "Value Error"


def test_muze_bilet_fiyati():
    assert bilet_fiyati(6) == 0
    assert bilet_fiyati(7) == 50
    assert bilet_fiyati(17) == 50
    assert bilet_fiyati(18) == 100
    assert bilet_fiyati(64) == 100
    assert bilet_fiyati(65) == 60
    assert bilet_fiyati(17) == "Value Error"

def test_not_ortalamasi():
    assert ortalama([10,56]) == 33
    assert ortalama([90,81]) == 85.5
    assert ortalama([]) == "Value Error"
    