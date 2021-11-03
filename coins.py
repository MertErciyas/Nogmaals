# name of student: Mert
# number of student: 99058235
# purpose of program: Calculation values
# function of program: Turns value into an amount of comments
# structure of program: 


toPay = int(float(input('Amount to pay: '))* 100) # The amount you need to pay
paid = int(float(input('Paid amount: ')) * 100) # The amount you payed with
change = paid - toPay # The amount you will get back

if change > 0: # If statment for change
  coinValue = 50 # The value for the coin
  
  while change > 0 and coinValue > 0: #
    nrCoins = change // coinValue # Calculations for nrCoins

    if nrCoins > 0: # If statment for nrCoins
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # Print statment for how much coins you need
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # Print statment for how much coins you returned
      change -= nrCoinsReturned * coinValue # This Calculates the change in coin value

# comment on code below:
    if coinValue == 500:
      coinValue = 300
    if coinValue == 300:
      coinValue = 200
    if coinValue == 200:
      coinValue = 50
    if coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: # If statment for if change is good or not
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')