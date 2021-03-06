from urllib import request

URLS = [
    "https://www.oregonhikers.org/field_guide/Special:Ask?q=[[Category%3AAll%20Season%20Hikes&po=Difficulty%0D%0ADistance%0D%0AElevation%20gain&sort=&order=ASC&limit=50&usersearch=yes",
    "https://www.oregonhikers.org/field_guide/Special:Ask?q=[[Category%3AAlpine%20Hikes&po=Difficulty%0D%0ADistance%0D%0AElevation%20gain&sort=&order=ASC&limit=50&usersearch=yes",
    "https://www.oregonhikers.org/field_guide/Special:Ask?q=[[Category%3ABackpackable%20Hikes&po=Difficulty%0D%0ADistance%0D%0AElevation%20gain&sort=&order=ASC&limit=50&usersearch=yes",
    "https://www.oregonhikers.org/field_guide/Special:Ask?q=[[Category%3ABeach%20Hikes&po=Difficulty%0D%0ADistance%0D%0AElevation%20gain&sort=&order=ASC&limit=50&usersearch=yes",
    "https://www.oregonhikers.org/field_guide/Special:Ask?q=[[Category%3ABushwhacks&po=Difficulty%0D%0ADistance%0D%0AElevation%20gain&sort=&order=ASC&limit=50&usersearch=yes",
    "https://www.oregonhikers.org/field_guide/Special:Ask?q=[[Category%3ACreek%20Hikes&po=Difficulty%0D%0ADistance%0D%0AElevation%20gain&sort=&order=ASC&limit=50&usersearch=yes",
    "https://www.oregonhikers.org/field_guide/Special:Ask?q=[[Category%3ACrowded%20Hikes&po=Difficulty%0D%0ADistance%0D%0AElevation%20gain&sort=&order=ASC&limit=50&usersearch=yes",
    "https://www.oregonhikers.org/field_guide/Special:Ask?q=[[Category%3AExposed%20Hikes&po=Difficulty%0D%0ADistance%0D%0AElevation%20gain&sort=&order=ASC&limit=50&usersearch=yes",
    "https://www.oregonhikers.org/field_guide/Special:Ask?q=[[Category%3AFamily%20Hikes&po=Difficulty%0D%0ADistance%0D%0AElevation%20gain&sort=&order=ASC&limit=50&usersearch=yes",
    "https://www.oregonhikers.org/field_guide/Special:Ask?q=[[Category%3AGlacier%20Hikes&po=Difficulty%0D%0ADistance%0D%0AElevation%20gain&sort=&order=ASC&limit=50&usersearch=yes",
    "https://www.oregonhikers.org/field_guide/Special:Ask?q=[[Category%3AHike%20and%20Bike&po=Difficulty%0D%0ADistance%0D%0AElevation%20gain&sort=&order=ASC&limit=50&usersearch=yes",
    "https://www.oregonhikers.org/field_guide/Special:Ask?q=[[Category%3AHot%20Spring%20Hikes&po=Difficulty%0D%0ADistance%0D%0AElevation%20gain&sort=&order=ASC&limit=50&usersearch=yes",
    "https://www.oregonhikers.org/field_guide/Special:Ask?q=[[Category%3ALake%20Hikes&po=Difficulty%0D%0ADistance%0D%0AElevation%20gain&sort=&order=ASC&limit=50&usersearch=yes",
    "https://www.oregonhikers.org/field_guide/Special:Ask?q=[[Category%3ALookout%20Hikes&po=Difficulty%0D%0ADistance%0D%0AElevation%20gain&sort=&order=ASC&limit=50&usersearch=yes",
    "https://www.oregonhikers.org/field_guide/Special:Ask?q=[[Category%3ALoop%20Hikes&po=Difficulty%0D%0ADistance%0D%0AElevation%20gain&sort=&order=ASC&limit=50&usersearch=yes",
    "https://www.oregonhikers.org/field_guide/Special:Ask?q=[[Category%3ALost%20Hikes&po=Difficulty%0D%0ADistance%0D%0AElevation%20gain&sort=&order=ASC&limit=50&usersearch=yes",
    "https://www.oregonhikers.org/field_guide/Special:Ask?q=[[Category%3AOff%20The%20Beaten%20Track&po=Difficulty%0D%0ADistance%0D%0AElevation%20gain&sort=&order=ASC&limit=50&usersearch=yes",
    "https://www.oregonhikers.org/field_guide/Special:Ask?q=[[Category%3AOff%20Trail&po=Difficulty%0D%0ADistance%0D%0AElevation%20gain&sort=&order=ASC&limit=50&usersearch=yes",
    "https://www.oregonhikers.org/field_guide/Special:Ask?q=[[Category%3AOld%20Growth%20Hikes&po=Difficulty%0D%0ADistance%0D%0AElevation%20gain&sort=&order=ASC&limit=50&usersearch=yes",
    "https://www.oregonhikers.org/field_guide/Special:Ask?q=[[Category%3ARails%20to%20Trails&po=Difficulty%0D%0ADistance%0D%0AElevation%20gain&sort=&order=ASC&limit=50&usersearch=yes",
    "https://www.oregonhikers.org/field_guide/Special:Ask?q=[[Category%3AScrambles&po=Difficulty%0D%0ADistance%0D%0AElevation%20gain&sort=&order=ASC&limit=50&usersearch=yes",
    "https://www.oregonhikers.org/field_guide/Special:Ask?q=[[Category%3ASnowshoe%20Hikes&po=Difficulty%0D%0ADistance%0D%0AElevation%20gain&sort=&order=ASC&limit=50&usersearch=yes",
    "https://www.oregonhikers.org/field_guide/Special:Ask?q=[[Category%3ATraverse%20Hikes&po=Difficulty%0D%0ADistance%0D%0AElevation%20gain&sort=&order=ASC&limit=50&usersearch=yes",
    "https://www.oregonhikers.org/field_guide/Special:Ask?q=[[Category%3AUnmaintained%20Trails&po=Difficulty%0D%0ADistance%0D%0AElevation%20gain&sort=&order=ASC&limit=50&usersearch=yeshttps://www.oregonhikers.org/field_guide/Special:Ask?q=[[Category%3AUniversal%20Access%20Hikes&po=Difficulty%0D%0ADistance%0D%0AElevation%20gain&sort=&order=ASC&limit=50&usersearch=yes",
    "https://www.oregonhikers.org/field_guide/Special:Ask?q=[[Category%3AUrban%20Hikes&po=Difficulty%0D%0ADistance%0D%0AElevation%20gain&sort=&order=ASC&limit=50&usersearch=yes",
    "https://www.oregonhikers.org/field_guide/Special:Ask?q=[[Category%3AViewpoint%20Hikes&po=Difficulty%0D%0ADistance%0D%0AElevation%20gain&sort=&order=ASC&limit=50&usersearch=yes",
    "https://www.oregonhikers.org/field_guide/Special:Ask?q=[[Category%3AVolcanic%20Feature%20Hikes&po=Difficulty%0D%0ADistance%0D%0AElevation%20gain&sort=&order=ASC&limit=50&usersearch=yes",
    "https://www.oregonhikers.org/field_guide/Special:Ask?q=[[Category%3AWaterfall%20Hikes&po=Difficulty%0D%0ADistance%0D%0AElevation%20gain&sort=&order=ASC&limit=50&usersearch=yes",
    "https://www.oregonhikers.org/field_guide/Special:Ask?q=[[Category%3AWilderness%20Hikes&po=Difficulty%0D%0ADistance%0D%0AElevation%20gain&sort=&order=ASC&limit=50&usersearch=yes",
    "https://www.oregonhikers.org/field_guide/Special:Ask?q=[[Category%3AWildflower%20Hikes&po=Difficulty%0D%0ADistance%0D%0AElevation%20gain&sort=&order=ASC&limit=50&usersearch=yes",
    "https://www.oregonhikers.org/field_guide/Special:Ask?q=[[Category%3AWildlife%20Refuge%20Hikes&po=Difficulty%0D%0ADistance%0D%0AElevation%20gain&sort=&order=ASC&limit=50&usersearch=yes",
    "https://www.oregonhikers.org/field_guide/Special:Ask?q=[[Category%3AWildlife%20Viewing%20Hikes&po=Difficulty%0D%0ADistance%0D%0AElevation%20gain&sort=&order=ASC&limit=50&usersearch=yes",
]



def main():
    global URLS
    for URL in URLS:
        try:
            r = request.urlopen(URL)
            bytecode = r.read()
            htmlstr = bytecode.decode()
            print(htmlstr)
        except:
            pass


if __name__=='__main__':
    main()