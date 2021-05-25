
# An introduction to Web Scraping with Python and Azure Functions
### Level: Beginner 
### Presentation: [Presentation slides](workshop/Workshop_presentation.pdf)

## Workshop description
During the workshop you will learn how to implement a web scraper using Scrapy, store the output in a Blob storage on Azure, and use an Azure function to generate a wordcloud of the text obtained.

## Requirements
Python version: 3.8.5

You can check the required python libraries to run this project [here](solutions/requirements.txt)

#### Tools:
* Source-code editor: Visual Studio Code
* To test our function: Microsoft Azure Storage Explorer
* Azure account: You can create one with 12 months of free service for free [here](https://azure.microsoft.com/en-us/free/)
* The [Azure Functions Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=windows%2Ccsharp%2Cbash#install-the-azure-functions-core-tools) version 3.x
* The [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) for Visual Studio Code
The [Azure Functions extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions) for Visual Studio Code
* The [Azurite extension](https://marketplace.visualstudio.com/items?itemName=Azurite.azurite) for testing functions in Visual Studio Code

## Usage
* Clone the repository
* Start Visual Studio Code and navigate to the solutions folder
#### scrapy_workshop_pyladies
* To put our spider to work, go to the project’s top level directory and run:

```python
scrapy crawl cuisines
```

#### wordcloud_azure_function
##### BlobTrigger - Python

The `BlobTrigger` makes it incredibly easy to react to new Blobs inside of Azure Blob Storage. This sample demonstrates a simple use case of processing data from a given Blob using Python.

##### How it works

For a `BlobTrigger` to work, you provide a path which dictates where the blobs are located inside your container, and can also help restrict the types of blobs you wish to return. For instance, you can set the path to `samples/{name}.png` to restrict the trigger to only the samples path and only blobs with ".png" at the end of their name.

##### Learn more

[Azure Blob storage trigger for Azure Functions](https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob-trigger?tabs=csharp)

## Video record
Will be available within 1-2 weeks after the event

## Credits
This workshop was set up by @pyladiesams and @danielamiranda
