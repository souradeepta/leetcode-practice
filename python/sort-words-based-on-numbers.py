def sort(input):
    words = input.split()
    words_char_array = []
    mapped_list = {}
    for element in words:
        element_break = sorted(list(element))
        words_char_array.append(element_break)
    print(f'{words_char_array}')


input = "outp4ut Thi1s 3an st%ring i2s"
sort(input)
