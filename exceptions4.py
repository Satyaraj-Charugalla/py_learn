#--------------------Extended versions for exceptions--------------------------------
#try and finally
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
# No matter how the try and except run the finnaly statement will be executing
