# Lab, Bölüm 2: Testleri bu dosyaya SİZ yazacaksınız.
#
# Aşağıda örnek olarak bir test var. Yanına her fonksiyon için kendi testlerinizi ekleyin.
# Çalıştırmak için bu klasörde:  python -m pytest test_bolum2.py test_hatali_surumler.py -v

import pytest

from bolum2 import sifre_gucu, otopark_ucreti, yuzde_degisim


def test_kisa_sifre_zayif():
    assert sifre_gucu("abc") == "zayıf"
    assert sifre_gucu("1234567") == "zayıf"
def test_kisa_sifre_orta():
    assert sifre_gucu("12345678") == "orta"
    assert sifre_gucu("1234567890ab") == "orta"
def test_kisa_sifre_orta():
    assert sifre_gucu("1234567890abc") == "güçlü"
def test_kisa_sifre_bos():
    with pytest.raises(ValueError):
        sifre_gucu("")

def test_otopark_ucreti():
    assert otopark_ucreti(15)== 0
    assert otopark_ucreti(60)== 20
    assert otopark_ucreti(180)== 40
def test_otopark_ucreti_negatif():
    with pytest.raises(ValueError):
        otopark_ucreti(-1)


def test_yuzde_degisim():
    assert yuzde_degisim(200,250)==25
    assert yuzde_degisim(100,0) == -100
def test_yuzde_degisim_eski0():
    with pytest.raises(ValueError):
        yuzde_degisim(0,120)



    

    
    

    
