def generate_hashtags(text):

    words = text.split()

    hashtags = []

    for word in words[:5]:

        hashtags.append("#"+word.replace(".","").replace(",",""))

    hashtags.append("#DigitalMarketing")
    hashtags.append("#BusinessGrowth")

    return hashtags


def generate_seo_keywords(text):

    words = text.split()

    keywords = []

    for word in words[:5]:

        keywords.append(f"best {word}")
        keywords.append(f"{word} platform")

    return keywords