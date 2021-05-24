import logging

import azure.functions as func
import wordcloud

# from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


def main(myBlob: func.InputStream, inputBlob: bytes, outputBlob: func.Out[bytes]):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myBlob.name}\n"
                 f"Blob Size: {myBlob.name} bytes")

    # Reading input blob and Converting list to plain text
    logging.info("Getting input file as a single string")
    recipe_names_text = inputBlob.replace("\n", " ").replace('\r', '')

    # Create and generate a word cloud image:
    word_cloud = wordcloud.WordCloud(background_color="white").generate(recipe_names_text)

    # Save wordcloud in output file
    outputBlob.set(wordcloud.to_file(f"{myBlob.name}.png"))
    # outputBlob.set(recipe_names_text)
