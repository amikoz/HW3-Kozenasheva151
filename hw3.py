import re
import urllib.request
import os
import html
def download_page1(pageUrl1):
    try:
        page1 = urllib.request.urlopen(pageUrl1)
        text1 = page1.read().decode('UTF-8')
    except:
        text1 = 'unavailable page'
    return text1


def txt_1(text1):
    regPostTitletxt1 = re.compile(' <b class="regnum_title">REGNUM</b></span>(.*?)</div>', flags=re.DOTALL)
    t1 = regPostTitletxt1.findall(text1)
    if t1:
        txt_1 = t1
        new_text1 = []
        regTag1 = re.compile('<.*?>', flags=re.DOTALL)
        regSpace1 = re.compile('\s{2,}', flags=re.DOTALL)
        for finaltext1 in txt_1:
            clean_t1 = regSpace1.sub("", finaltext1)
            clean_t = regTag1.sub("", clean_t1)
            new_text1.append(clean_t)
            for finaltext1 in new_text1:
                finaltext1.replace("&nbsp;&rarr;&raquo;&mdash;&laquo&ndash;", " ")
        if finaltext1:
            txt_1= html.unescape(finaltext1)
    else:
        txt_2 = 'no text'
    return txt_1

def func1(txt_1):
    n = txt_1.lower()
    n2 = n.replace(',', '')
    n1 = n2.replace('.', '')
    n0 = n1.replace('»', '')
    n3 = n0.replace('«', '')
    n4 = n3.replace('-', '')
    n5 = n4.replace('\n', '')
    n6 = n5.replace(':', '')
    n7 = re.sub(u"[0-9]{1,}", " ", n6)
    m1 = n7.split(" ")
    A = set(m1)
    return A



def download_page2(pageUrl2):
    try:
        page2 = urllib.request.urlopen(pageUrl2)
        text2 = page2.read().decode('UTF-8')
    except:
        text2 = 'unavailable page'
    return text2


def txt_2(text2):
    regPostTitletxt2 = re.compile('<div itemprop="articleBody">(.*?)<div data-type="Incut. By wide" class="b-read-more b-read-more_wide">', flags=re.DOTALL)
    t2 = regPostTitletxt2.findall(text2)
    if t2:
        txt_2= t2
        new_text2 = []
        regTag2 = re.compile('<.*?>', flags=re.DOTALL)
        regSpace2 = re.compile('\s{2,}', flags=re.DOTALL)
        for finaltext2 in txt_2:
            clean_t2 = regSpace2.sub("", finaltext2)
            clean_t2 = regTag2.sub("", clean_t2)
            new_text2.append(clean_t2)
            for finaltext2 in new_text2:
                finaltext2.replace("&nbsp;&rarr;&raquo;&mdash;&laquo&ndash;", " ")
        if finaltext2:
            txt_2 = html.unescape(finaltext2)
    else:
        txt_2 = 'no text'
    return txt_2

def func2(txt_2):
    n2 = txt_2.lower()
    n22 = n2.replace(',', '')
    n12 = n22.replace('.', '')
    n02 = n12.replace('»', '')
    n32 = n02.replace('«', '')
    n42 = n32.replace('-', '')
    n52 = n42.replace('\n', '')
    n62 = n52.replace(':', '')
    n72 = re.sub(u"[0-9]{1,}", " ", n62)
    m2 = n72.split(" ")
    B = set(m2)
    return B

def download_page3(pageUrl3):
    try:
        page3 = urllib.request.urlopen(pageUrl3)
        text3 = page3.read().decode('UTF-8')
    except:
        text3 = 'unavailable page'
    return text3


def txt_3(text3):
    regPostTitletxt3 = re.compile('<div class="b-text clearfix js-topic__text" itemprop="articleBody">(.*?)<aside class="b-inline-topics-box b-box_floated b-inline-topics-box_wide b-box_left">', flags=re.DOTALL)
    t3 = regPostTitletxt3.findall(text3)
    if t3:
        txt_3 = t3
        new_text3 = []
        regTag3 = re.compile('<.*?>', flags=re.DOTALL)
        regSpace3 = re.compile('\s{2,}', flags=re.DOTALL)
        for finaltext3 in txt_3:
            clean_t3 = regSpace3.sub("", finaltext3)
            clean_t3 = regTag3.sub("", clean_t3)
            new_text3.append(clean_t3)
            for finaltext3 in new_text3:
                finaltext3.replace("&nbsp;&rarr;&raquo;&mdash;&laquo&ndash;", " ")
        if finaltext3:
            txt_3 = html.unescape(finaltext3)
    else:
        txt_3 = 'no text'
    return txt_3

def func3(txt_3):
    n3 = txt_3.lower()
    n23 = n3.replace(',', '')
    n13 = n23.replace('.', '')
    n03 = n13.replace('»', '')
    n33 = n03.replace('«', '')
    n43 = n33.replace('-', '')
    n53 = n43.replace('\n', '')
    n63 = n53.replace(':', '')
    n73 = re.sub(u"[0-9]{1,}", " ", n63)
    m3 = n73.split(" ")
    C = set(m3)
    return C


def download_page4(pageUrl4):
    try:
        page4 = urllib.request.urlopen(pageUrl4)
        text4 = page4.read().decode('UTF-8')
    except:
        text4 = 'unavailable page'
    return text4


def txt_4(text4):
    regPostTitletxt4 = re.compile('<p class="lid">(.*?)<p><div class="article__incut">', flags=re.DOTALL)
    t4 = regPostTitletxt4.findall(text4)
    if t4:
        txt_4 = t4
        new_text4 = []
        regTag4 = re.compile('<.*?>', flags=re.DOTALL)
        regSpace4 = re.compile('\s{2,}', flags=re.DOTALL)
        for finaltext4 in txt_4:
            clean_t4 = regSpace4.sub("", finaltext4)
            clean_t4 = regTag4.sub("", clean_t4)
            new_text4.append(clean_t4)
            for finaltext4 in new_text4:
                finaltext4.replace("&nbsp;&rarr;&raquo;&mdash;&laquo&ndash;", " ")
        if finaltext4:
            txt_4 = html.unescape(finaltext4)
    else:
        txt_4 = 'no text'
    return txt_4

def func4(txt_4):
    n4 = txt_4.lower()
    n24 = n4.replace(',', '')
    n14 = n24.replace('.', '')
    n04 = n14.replace('»', '')
    n34 = n04.replace('«', '')
    n44 = n34.replace('-', '')
    n54 = n44.replace('\n', '')
    n64 = n54.replace(':', '')
    n74 = re.sub(u"[0-9]{1,}", " ", n64)
    m4 = n74.split(" ")
    D = set(m4)
    return D

def intersec(A, B, C, D):
    inter1 = A.intersection(B)
    inter2 = inter1.intersection(C)
    inter = inter2.intersection(D)
    print('Пересечение множеств: ', inter)
   
def symmdif(A, B, C, D):
    sd1 = A.symmetric_difference(B)
    sd2 = sd1.symmetric_difference(C)
    sd = sd2.symmetric_difference(D)
    print('Симметрическая разность множeств: ', sd)


   
def main():
    pageUrl1 = 'https://regnum.ru/news/innovatio/2211264.html'
    text1 = download_page1(pageUrl1)
    g1 = txt_1(text1)
    b1 = func1(g1)
    pageUrl2 = 'https://rg.ru/2016/11/29/na-marse-obnaruzhen-labirint.html'
    text2 = download_page2(pageUrl2)
    g2 = txt_2(text2)
    b2 = func2(g2)
    pageUrl3 = 'https://lenta.ru/news/2016/11/29/mars/'
    text3 = download_page3(pageUrl3)
    g3 = txt_3(text3)
    b3 = func3(g3)
    pageUrl4 = 'http://www.mk.ru/science/2016/11/29/tainstvennyy-labirint-na-marse-privlek-vnimanie-planetologov.html'
    text4 = download_page4(pageUrl4)
    g4 = txt_4(text4)
    b4 = func4(g4)
    intersec(b1, b2, b3, b4)
    symmdif(b1, b2, b3, b4)

    
if __name__ == '__main__':
    main()
