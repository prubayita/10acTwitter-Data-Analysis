from textblob import TextBlob

# Feedback1= "#Pelosi \n#Taipei \n#taiwan\n#XiJinping \n#China \nOn a verge of another war https://t.co/DuqDiSnWcd",
Feedback1 =  "a verge of another war"
blob1 = TextBlob(Feedback1)
print(blob1.sentiment)