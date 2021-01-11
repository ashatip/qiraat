"""
script to use to remove arabic signs
"""

import re

QURAN = ""

with open("quran_orig.txt", "r") as quran_file:
    QURAN = quran_file.read()


def de_noise(text):
    """
    remove harakat
    https://alraqmiyyat.github.io/2013/01-02.html
    """
    noise = re.compile(""" ّ    | # Tashdid
                       َ    | # Fatha
                       ً    | # Tanwin Fath
                       ُ    | # Damma
                       ٌ    | # Tanwin Damm
                       ِ    | # Kasra
                       ٍ    | # Tanwin Kasr
                       ْ    | # Sukun
                       ۩   | # sajad
                       ۞   | # idk
                       ۗ    | # qaf lam
                       ۙ    | # lam alif
                       ۚ    | # gam
                       ۖ    | # idk
                       ۜ    | # seen
                       ۛ    | # three dots
                       ٰ    | # three dots
                       ـ     # Tatwil/Kashida
                       """, re.VERBOSE)
    text = re.sub(noise, '', text)
    return text


def normalize_arabic(text):
    """
    remove the dots and other stuff
    """
    text = re.sub("[ثبت]", "ٮ", text)
    text = re.sub("[جخ]", "ح", text)
    text = re.sub("ق", "ٯ", text)
    text = re.sub("ف", "ڡ", text)
    text = re.sub("ض", "ص", text)
    text = re.sub("[إأٱآا]", "ا", text)
    text = re.sub("[ئي]", "ى", text)
    text = re.sub("ؤ", "و", text)
    # text = re.sub(r"(\s)ن", r"\1ں", text)
    text = re.sub(r"ن(\s)", r"ں\1", text)
    text = re.sub(r"ن", "ٮ", text)
    text = re.sub("ش", "س", text)
    text = re.sub("ظ", "ط", text)
    text = re.sub("ذ", "د", text)
    text = re.sub("غ", "ع", text)
    text = re.sub("ز", "ر", text)
    text = re.sub("ة", "ه", text)
    text = re.sub("ء", "", text)
    return text


QURAN = de_noise(QURAN)
QURAN = normalize_arabic(QURAN)
with open("quran_skeleton.txt", "w") as quran_write:
    quran_write.write(QURAN)
