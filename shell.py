import nexBASIC

while True:
    text = input('nexBASIC > ')
    result, error = nexBASIC.run(text)

    if error: print(error.as_string())
    else: print(result)