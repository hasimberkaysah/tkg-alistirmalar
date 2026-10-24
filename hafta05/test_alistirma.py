# Alıştırma 4: Testleri bu dosyaya SİZ yazacaksınız.
#
# Aşağıda örnek olarak bir test var. Yanına kendi testlerinizi ekleyin.
# Çalıştırmak için bu klasörde:  python -m pytest -v

import pytest

from alistirma import indirim_orani, sepet_toplami, en_pahali_urun


def test_sepet_toplami():
    sepet = [
        {"urun": "çay", "fiyat": 20, "adet": 2},
        {"urun": "simit", "fiyat": 15, "adet": 3},
        {"urun": "tost", "fiyat": 60, "adet": 1},
    ]
    assert sepet_toplami(sepet) == 145

def test_sepet_toplami_bos_sepet():
    assert sepet_toplami([]) == 0

def test_sepet_toplami_tek_urun():
    assert sepet_toplami([{"urun": "çay", "fiyat": 20, "adet": 5}]) == 100

def test_sepet_toplami_sifir():
    sepet = [{"urun": "çay", "fiyat": 20, "adet": 0}]
    with pytest.raises(ValueError):
        sepet_toplami(sepet)

def test_sepet_toplami_adet_negatif():
    sepet = [{"urun": "çay", "fiyat": 20, "adet": -1}]
    with pytest.raises(ValueError):
        sepet_toplami(sepet)

def test_sepet_toplami_gecerli_urunun_yaninda_gecersiz_adet():
    sepet = [
        {"urun": "çay", "fiyat": 20, "adet": 2},
        {"urun": "simit", "fiyat": 15, "adet": 0},
    ]
    with pytest.raises(ValueError):
        sepet_toplami(sepet)


@pytest.mark.parametrize(
    "tutar, beklenen",
    [
        (0, 0),        # alt sınır
        (50, 0),
        (99, 0),       # 100'ün hemen altı
        (100, 5),      # sınır
        (250, 5),
        (499, 5),      # 500'ün hemen altı
        (500, 10),     # sınır
        (750, 10),
        (999, 10),     # 1000'in hemen altı
        (1000, 15),    # sınır
        (5000, 15),
    ],
)

def test_indirim_orani(tutar, beklenen):
    assert indirim_orani(tutar) == beklenen

def test_indirim_orani_negatif_tutar():
    with pytest.raises(ValueError):
        indirim_orani(-1)


def test_en_pahali_urun():
    sepet = [
        {"urun": "çay", "fiyat": 20, "adet": 2},
        {"urun": "tost", "fiyat": 60, "adet": 1},
        {"urun": "simit", "fiyat": 15, "adet": 3},
    ]
    assert en_pahali_urun(sepet) == "tost"

def test_en_pahali_urun_bos_sepet():
    assert en_pahali_urun([]) is None

def test_en_pahali_urun_tek_urun():
    assert en_pahali_urun([{"urun": "çay", "fiyat": 20, "adet": 1}]) == "çay"

def test_en_pahali_urun_esit_fiyatta_ilk_gelen():
    sepet = [
        {"urun": "tost", "fiyat": 60, "adet": 1},
        {"urun": "pizza", "fiyat": 60, "adet": 1},
    ]
    assert en_pahali_urun(sepet) == "tost"


def test_en_pahali_urun_birim_fiyata_bakar_toplama_degil():
    sepet = [
        {"urun": "simit", "fiyat": 15, "adet": 10},
        {"urun": "tost", "fiyat": 60, "adet": 1},
    ]
    assert en_pahali_urun(sepet) == "tost"
 
 
def test_en_pahali_urun_en_pahali_sonda():
    sepet = [
        {"urun": "çay", "fiyat": 20, "adet": 1},
        {"urun": "simit", "fiyat": 15, "adet": 1},
        {"urun": "tost", "fiyat": 60, "adet": 1},
    ]
    assert en_pahali_urun(sepet) == "tost"
 
