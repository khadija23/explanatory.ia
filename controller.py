from retriever.retrieval import Retriever
# Class to manage document embedding and retrieval
class Controller:
    def __init__(self):
        self.retriever =None
        self.query = None
    

    def embed_document(self,file):
        # Embed the document
        if file is not None:
            self.retriever = Retriever()
            # create and add embedding for provided document file
            self.retriever.create_add_and_embeddings(file.name)
            
    def retrieve(self,query):
        #Retrieve the text based on user's query
        texts = self.retriever.retrieve_texts(query)
        return texts