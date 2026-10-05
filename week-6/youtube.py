def like_dislike(reviews):
    likes = 0
    dislikes = 0
    for review in reviews:
        if review.lower() == "like":
            likes += 1
        elif review.lower() == "dislike":
            dislikes += 1
    print("Likes:", likes)
    print("Dislikes:", dislikes)


opinions = []
for i in range(3):
    opinion = input("Give me your opinion for the video (Like or Dislike): ")
    opinions.append(opinion)

like_dislike(opinions)
