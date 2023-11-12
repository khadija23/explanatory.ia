def save(query, qa):
    # Use the get_openai_callback function 
    with get_openai_callback() as cb:
        # Query the qa object with the user's question
        response = qa({"query": query}, return_only_outputs=True)
        
        # Return the answer from the llm's response
        return response["result"]