#GenAI script
import google.generativeai as genai
import os
class recipeWriter:
    def __init__(self):
        genai.configure(api_key=os.environ["API_KEY"])
        self.model = genai.GenerativeModel("gemini-1.5-flash") #Initialise the Gemini model
        self.contextdata = """instructions('''You are a backend API designed to generate cooking recipes for a website. The workflow is as such:
        Attempt to format the given input into a recipe.ELSE, Reject any input that is not possible to create a recipe from AND Return an error specifying that an invalid input was recieved, formatted correctly:
        error header: "INSTRUCTIONS:"
        error subheader: "Please provide a list of ingredients from which to generate a recipe, and a recipe name."
        error text: "You may also include:"
        error list: "steps you would like to see, quantities, number of servings, serving suggestions"
        Your inputs are ingredients used, the quantities they are used in,and the name of the dish.
        Your outputs are a step-by-step recipe to make the dish using only the ingredients stated in the quantities given..
        The recipe should have an ingredient list, stating each ingredient, how it should be prepared, and what quantity.
        The recipe should have a methods list, stating the steps that need to be taken to successfully make the dish.
        The methods list should be structured so that parts of the dish that are made separately are listed in separate subsections.
        Ingredients list should go first, and ingredients for a subsection should be grouped.
        Methods list should go after, and steps for a subsection should be grouped.
        The input will be formatted as natural text or as a list, and the job of the API is to successfully parse it. If any vital ingredients are omitted, add them yourself.
        The only output should be the completed recipe or error embedded in html tags, but h2 tags should not be used. do not include ```html.''')
        input:{
        """
        #Context data for prompt interpretation and parsing


    def generate(self,text): #Combines context and instructions, and cleans any common formatting problems
        ingredients=text
        print("Debug: Data processing...")
        response = self.model.generate_content(self.contextdata+ingredients)
        print("Done!")
        responsetext=response.text
        responsetext=responsetext.replace("```html","")
        responsetext=responsetext.replace("```","")
        file=open("output.txt", "w")
        file.write(responsetext)
        file.close()
        print(os.path.abspath(os.curdir))
        return(responsetext)





