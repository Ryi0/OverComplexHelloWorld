def hello_world():
    print("Hello World!")


def greet(greet_wrd, pers, date):
    message = greet_wrd + ' ' + pers + "! How are you doing on the beautiful evening of the: " + date + "?"
    return message


myVar = {
    'greet': "Hello",
    "name": "John Doe"
}
GreetingWord = 'Hello'
myDate = {
    'GreetingDay': 27,
    'GreetingDateAsFloat': 0.03272024
}


def merge_persnirs_with_date(pers, date):
    date_and_pers = [
        pers,
        date
    ]
    return date_and_pers


print(myVar.get('greet'))


# greet(myVar)


def format_date_from_float(date_as_float):
    assert isinstance(date_as_float, float), "is not float"
    date_array = []
    date_as_str = str(date_as_float).split("0.")[1]
    formated_date = []
    for ch in date_as_str:
        date_array.append(ch)
    for index, numb_ch in enumerate(date_array[:-1]):
        tmp_ch = (date_array[index] + date_array[index + 1])
        if index % 2 == 0:
            formated_date.append(tmp_ch)
            if index == 4:
                formated_date.pop()
                tmp_ch = tmp_ch + date_array[index + 2] + date_array[index + 3]
                formated_date.append(tmp_ch)
                break
    tmpRet = "/".join(formated_date)
    return tmpRet


pers_date = merge_persnirs_with_date(myVar.get('name'), format_date_from_float(myDate.get('GreetingDateAsFloat')))
print(format_date_from_float(myDate.get('GreetingDateAsFloat')))
print(greet(GreetingWord, pers_date[0], pers_date[1]))
