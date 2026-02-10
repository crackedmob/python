# MATCH STATEMENT
# this is like a switch case, but in python
# match expression:
#   case x :
#       code block
#   case y:
#        code block
#   case z:
#       code block

day = 8
match day:
    case 1:
        print("monday")
    case 2:
        print('tuesday')
    case 3:
        print('wednesday')
    case 4:
        print('thursday')
    case 5:
        print('friday')
    case 6:
        print('saturday')
    case 7:
        print('sunday')
    case _:  # default value, when no case matches
        print('no sunch day exists')


# combining values
# we can do that using pipe character | as an or operator
# in the case evaluation to check for more than one value match in one case
day = 5
match day:
    case 1 | 2 | 3 | 4 | 5 :
        print("weekday")
    case 6 | 7 :
        print('weekend')
    case _ :
        print("not a valid day")


# if statements as guards
day = 5
month = 5
match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("weekday in april")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("weekday in may")
    case 6 | 7 if month == 4:
        print('weekend in april')
    case 6 | 7 if month == 5:
        print('weekend in may')
    case _ :
        print("not a valid day")