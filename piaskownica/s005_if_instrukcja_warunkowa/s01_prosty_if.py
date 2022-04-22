value = True

if value:
    print(True)
else:
    print(False)

# Odpowiednik:
#
# if (1) {
#   print(1)
# else {
#    print(0)
# }

value = 'a'

if value == 'a':
    print('a')
elif value == 'b':
    print('b')
elif value == 'c':
    print('b')
else:
    print('Nieoczekiwana wartość lub inna.')

# Odpowiednik:
#
# if (value == "a") {
#   print("a")
# else if (value == "b") {
#    print("b")
# else if (value == "c") {
#    print("b")
# }
# else {
#   print('Nieoczekiwana wartość lub inna.')
# }
#
# Wygląda to na odpowiednik switch.
# switch można kodować inaczej, szybciej i lepiej.
