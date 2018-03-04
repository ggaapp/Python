import _script_run_utf8
_script_run_utf8.main()

test_text1 = """>오늘은 일요일
>내일은 월요일
>그다음 날은 화요일
>그다음 날은 수요일
>그다음 날은 목요일
>그다음 날은 금요일
>그다음 날은 토요일
>그다음 날은 다시 일요일"""

test_text2 = "오늘은 일요일\n" +\
            "내일은 월요일\n" +\
            "그다음 날은 화요일\n" +\
            "그다음 날은 수요일\n" +\
            "그다음 날은 목요일\n" +\
            "그다음 날은 금요일\n" +\
            "그다음 날은 토요일\n" +\
            "그다음 날은 다시 일요일\n"

def write():
    # f = open('./_pdb/test.txt', 'w', encoding='utf-8')
    # f.write(test_text)
    # f.close()
    with open('./_pdb/test.txt', 'a', encoding='utf-8') as f:
        f.write(test_text1)
    with open('./_pdb/test.txt', 'a', encoding='utf-8') as f:
        f.write(test_text2)
write()
