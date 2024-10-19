# TODO Найдите количество книг, которое можно разместить на дискете
information_volume = 1.44
bytes = 1024
kilobytes = 1024
razmer_disket = information_volume * kilobytes * bytes
hranenie = 4
pages = 100
rows = 50
symbols = 25
volume_book = pages * rows * symbols * hranenie
print("Количество книг, помещающихся на дискету:", int(razmer_disket / volume_book))
