def retrieve_brand_guidelines():

    with open("knowledge_base.txt","r") as f:
        guidelines = f.read()

    return guidelines