funkcja = '''
x = %d
y = %d
dzialanie = "%s"
if dzialanie == "mnozenie":
    print(10*2)
else:
    if dzialanie == "dzielenie":
        print(10/2)
'''

coMaSieStac = "mnozenie"
x = 10
y = 2

exec(funkcja % (x, y, coMaSieStac))