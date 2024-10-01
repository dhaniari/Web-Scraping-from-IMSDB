# Assuming you have multiple scripts stored in different folders by genre
genres = ['action', 'comedy', 'drama', 'horror']

data_by_genre = {}
for genre in genres:
    with open(f"{genre}_scripts.txt", "r") as f:
        data_by_genre[genre] = f.read()

# Fine-tune your model based on genre
for genre, data in data_by_genre.items():
    # Pass the data through your model for fine-tuning
    print(f"Training on {genre} data")
