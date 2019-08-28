#Guess the song by Shawn Mendes
import random
Songs = ["Act Like You Love Me", "Aftertaste", "Air", "Bad Reputation", "Because I Had You", "Believe", "Bring It Back", "Crazy", "Don't Be A Fool", "Don't Want Your Love", "Fallin' All In You", "Hold On", "Honest", "I Don't Even Know Your Name", "I Know What You Did Last Summer", "If I Can't Have You", "Imagination", "In My Blood", "Kid in Love", "Life Of The Party", "Lights On", "Like This", "Like To Be You", "A Little Too Much", "Lost", "Lost In Japan", "Memories", "Mercy", "Mutual", "Nervous", "Never Be Alone", "No Promises", "One of Those Nights", "Particular Taste", "Patience", "Perfectly Wrong", "Queen", "Roses", "Ruin", "Running Low", "Senorita", "Show You", "Something Big", "Stitches", "There's Nothing Holdin' Me Back", "This Is What It Takes", "Three Empty Words", "Treat You Better", "Under Pressure", "Understand", "Use Somebody", "The Weight", "When You're Ready", "Where Were You in the Morning", "Why", "Youth"]

x = random.choice(Songs)

Guess = input(" guess the Shawn Mendes song")
Guess = str(Guess)

if Guess == x:
    print("Correct")
else:
    print("it was " + str(x))