front = "I love Python"
num = 1000000.123456789
back = "times more than R"
#print("{} {} {}".format(front, num, back))
#print(front + ' ' + str(num) + ' ' + back)

#print("%s %f %s" % (front, num, back))



print("%s %d %s" % (front, num, back))
print("%s %i %s" % (front, num, back))
print("%s %u %s" % (front, num, back))
print("%s %.1F %s" % (front, num, back))
print("%s %.1f %s" % (front, num, back))
print("%s %.5f %s" % (front, num, back))
print("%s %s %s" % (front, num, back))


object1 = "Python"
object2 = "R"
base = "I love {} {:,.2f} times more than {}"
print(base.format(object1, num, object2))

base1 = "I love {} {:,.0f} times more than {}"
print(base1.format(object1, num, object2))


