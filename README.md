# copy_files
Программа, которая умеет копировать текстовый файл.
В качестве аргументов она принимает имя файла-источника и имя файла-приемника.
Кроме того, в аргументах может быть указаны опция «--upper» для приведения всех символов файла к верхнему регистру, а также опция «--lines N» для копирования только первых N строк.
N может быть числом, превышающим количество строк в файле. Необходимо корректно обработать эту ситуацию.

Формат ввода
python3 ﬁle_copy.py --upper --lines 10 source.txt destination.txt
Примечания
Проверка валидности аргументов не требуется. Если целевой файл не существует, то его нужно создать, если существует – перезаписать.
В программе необходимо обязательно использовать библиотеку  
a
r
g
p
a
r
s
e
 .

В данной задаче под строкой понимается последовательность символов, которая заканчивается символом перевода строки — \n.
