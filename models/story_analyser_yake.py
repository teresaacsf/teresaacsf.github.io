import yake
doc = """
It was some time after lunch and the day was cloudy and warm, it had a mystical atmosphere going on. From the windows we could see the green mountains with no houses on, the fields with farming machines and some cows here and there.
There were four of us: Me, my brother and other two cousins, we were all around 10 years old. We were bored of playing in the garden area, we wanted to go big, so we had the idea to go on an adventurous trip in the woods around our aunt’s farm. I was leading the crew through the open fields, and we aimed for the forest we had previously seen on the horizon. We surpassed the fences that were keeping us in our aunt’s property and entered the unknown (to us) jungle. Inside the forest we could barely see the sky, it was almost entirely covered by trees. There was mud on the path and rocks and bushes everywhere. It was strangely quiet inside there, no birds singing, no wind blowing, no bees buzzing. Almost as if the forest knew something was wrong.

"""

max_ngram_size = 5

kw_extractor = yake.KeywordExtractor(n=max_ngram_size)
keywords = kw_extractor.extract_keywords(doc)
for kw in keywords:
  print(kw[0])