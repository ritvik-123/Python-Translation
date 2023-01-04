from translate import Translator
translator = Translator(to_lang='ja')
try:
    with open('./Translate.txt') as my_file:
        result = translator.translate(my_file.read())
        print(result)
        with open('./Translate_ja.txt', mode='w') as my_file2:
            my_file2.write('result')
except FileNotFoundError as e:
    print('file not found')
