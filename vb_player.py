import csv

# Open file  
with open('GISD.csv') as source: 
      
    # Create reader object by passing the file  
    # object to reader method 
    reader_obj = csv.reader(source)

    with open("GISD_refined.csv", "w") as result: 
        writer = csv.writer(result) 
        for r in reader_obj: 
            
            # Use CSV Index to remove a column from CSV 
            #r[3] = r['year'] 
            writer.writerow((r[0], r[1], r[2], r[3], r[17])) 
      
    # Iterate over each row in the csv  
    # file using reader object 
    #for row in reader_obj: 
    #    print(row)



'''
class Player:
    def __init__(self, number, name='Jane Doe', year='Freshman'):
        self.number = number
        self.name = name
        self.year = year
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def average_score(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)


class VolleyballAnalyzer:
    def __init__(self):
        self.players = {}

    def add_player(self, number, name='Jane Doe', year='Freshman'):
        self.players[name] = Player(number, name, year)

    def record_score(self, player_name, score):
        if player_name not in self.players:
            print(f"Player '{player_name}' not found.")
            return
        self.players[player_name].add_score(score)

    def display_average_scores(self):
        print("Average Scores:")
        for name, player in self.players.items():
            avg_score = player.average_score()
            print(f"{name}: {avg_score:.2f}")

# Example usage:
analyzer = VolleyballAnalyzer()

# Add players
analyzer.add_player(0,"Player1","Freshman")
analyzer.add_player(100,"Player2","Senior")

# Record scores
analyzer.record_score("Player1", 25)
analyzer.record_score("Player1", 20)
analyzer.record_score("Player2", 22)
analyzer.record_score("Player2", 24)
#analyzer.record_score("emily",20)

# Display average scores
analyzer.display_average_scores()
'''