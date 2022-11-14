import random
def decision_maker():
   yes = 'yes'
   no = 'no'
   percent_level = random.randint(1, 100)
   if percent_level >= 1 and percent_level < 50:
       return no
   elif percent_level > 50 and percent_level <= 100:
       return yes
   elif percent_level == 50:
       return 'roll the dice'

what_to_do = decision_maker()
print(what_to_do)