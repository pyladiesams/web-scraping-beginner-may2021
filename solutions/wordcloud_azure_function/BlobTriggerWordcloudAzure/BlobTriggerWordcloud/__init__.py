import logging
import azure.functions as func
import io

from wordcloud import WordCloud, STOPWORDS


def main(myBlob: func.InputStream, inputBlob: bytes, outputBlob: func.Out[bytes]):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myBlob.name}\n"
                 f"Blob Size: {myBlob.length} bytes")

    # Reading input blob 
    logging.info("Getting input file as a list")
    recipe_names_list = inputBlob.replace("\n", " ")

    # Converting list to plain text
    logging.info("Getting input file as a single string")
    recipe_names_text = recipe_names_list.replace('\r', '')
    logging.info(recipe_names_text)

    # Create stopword list:
    stopwords = set(STOPWORDS)
    stopwords.update(['African', 'American', 'British', 'Caribbean', 'Chinese', 'East European',
                    'French', 'Greek', 'Indian', 'Irish', 'Italian', 'Japanese', 'Korean',
                    'Mexican', 'Nordic', 'North African', 'Pakistani', 'Portuguese',
                    'South American', 'Spanish'])

    # Create and generate a word cloud image:
    logging.info("Generating wordcloud of input text")
    word_cloud = WordCloud(stopwords=stopwords, background_color="white").generate(recipe_names_text)

    wordcloud_img = word_cloud.to_image()
    logging.info(type(wordcloud_img))

    # Converting image to bytes object
    img_byte_arr = io.BytesIO()
    wordcloud_img.save(img_byte_arr, format='png')
    logging.info(type(img_byte_arr))



    # Save wordcloud in output file
    logging.info("Saving wordcloud image to output folder")
    outputBlob.set(img_byte_arr.getvalue())
    logging.info("Wordcloud image succesfully saved in output folder")