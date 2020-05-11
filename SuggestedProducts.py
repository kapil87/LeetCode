class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        word = list(searchWord)
        products = sorted(products)
        string = ''
        output = []
        
        #print(word)
        while word: 
            search_words = []
            letter = word.pop(0)
            string += letter 
            print(string)
            for product in products:
                if len(search_words) < 3: 
                    if product.startswith(string):
                        search_words.append(product)
            output.append(search_words)
            
        return output
