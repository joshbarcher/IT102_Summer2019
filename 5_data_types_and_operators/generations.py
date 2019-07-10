# this example will give us an idea about
# the importance of logical operators (and,
# or, not) and how we use them

born = int(input("What year were you born? "))

if born >= 1945 and born <= 1964:
    print("You are a baby boomer!")
elif born >= 1965 and born <= 1979:
    print("You are from generation X")
elif born >= 1980 and born <= 1994:
    print("You are a millennial")
elif born >= 1995:
    print("You're from generation Z")
else:
    print("I'm not sure what generation you're from")
    print("But you're awesome!")

if 1945 <= born < 1990:
    print("Hello")