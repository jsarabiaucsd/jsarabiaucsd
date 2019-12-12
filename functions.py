import string
import random
import nltk

#All possible inputs and outputs for ucsd_college function

seventh_student_in = ["seventh college", "seventh", "7 college", "7", "7th college", "7th"]  
seventh_student_out = ["Wow, that's not even built yet. Anyways, what is your major?", \
                       "I wonder how long it'll take to be named. Anyways, what is your major?", \
                       "I heard the view will be so nice. Anyways, what is your major?"]

sixth_student_in = ["sixth college", "sixth", "six", "6", "6th", "six college", "6 college", "6th college"]
sixth_student_out = ["Gotta Love those Racoons! Anyways, what is your major?", \
                     "I wonder how long it'll take to be named. Anyways, what is your major?", \
                     "Yay, y'all won Unolympics! #3peat Anyways, what is your major?", \
                     "Camp Snoopy is the best! Anyways, what is your major?", \
                     "Foodworx isn't that bad right? haha. Anyways, what is your major?", \
                     "RIP old Sixth. Anyways, what is your major?", \
                     "The Culture, Art, Technology writing classes are pretty fun! Anyways, what is your major?"]

erc_student_in = ["eleanor roosevelt college", "erc", "er", "roosevelt", "eleanor roosevelt", "eleanor college", \
                  "roosevelt college"]
erc_student_out = ["The Making of the Modern World Writing classes do not sound fun! Anyways, what is your major?", \
                   "Did you know your college was established in 1988. Anyways, what is your major?", \
                   "You must be strong since you are close to Rimac Gym! Anyways, what is your major?"]

warren_student_in = ["earl warren college", "earl warren", "warren", "warren college", "earl", "earl college"]
warren_student_out = ["Did you know your college was established in 1974. Anyways, what is your major?", \
                      "I love the Warren Bear! Anyways, what is your major?", \
                      "The Warren College Writing Program isn't too bad right? haha. Anyways, what is your major?"]

marshall_student_in = ["thurgood marshall college", "thurgood marshall", "marshall", "thurgood", \
                       "marshall college", "thurgood college", "third college", "3rd", "3rd college", "marsh"]
marshall_student_out = ["Did you know your college was established in 1970. Anyways, what is your major?", \
                        "The Dimension of Culture Writing Courses are not too bad, right? haha. Anyways, what is your major?"]

muir_student_in = ["john muir college", "john muir", "john", "muir", "john college", "muir college"]
muir_student_out = ["You're lucky! The Muir College Writing Program is only 2 quarters! Anyways, what is your major?", \
                    "Did you know your college was established in 1967. Anyways, what is your major?", \
                    "Muir is most people's first choice of colleges! Anyways, what is your major?"]

revelle_student_in = ["roger revelle college", "revelle", "revelle college", "roger college", "roger revelle", "rev", \
                      "roger rev"]
revelle_student_out = ["Galbraith Hall is such a nice studying location. Anyways, what is your major?", \
                       "Did you know your college was established in 1964. Anyways, what is your major?", \
                       "The Humanity writing courses are pretty interesting from what I've heard! Anyways, what is your major?", \
                       "I love the Revelle Fountain! Anyways, what is your major?"]


#All possible inputs and outputs for ucsd_major function 

anthropology_in = ["archaeology", "biological anthropology", "sociocultural anthropology", \
                   "climate change", "human solutions", "anthropology"]
anthropology_out = ["Wow, I wish I could learn more about the development of human societies and cultures. Thanks for telling me about your major and college. Bye!", \
                    "I don’t think enough people study Anthropology, so that’s neat! Thanks for telling me about your major and college. Bye!"]

classical_in = ["classical studies", "classical"]
classical_out = ["That’s a classic major! Haha, sorry… Thanks for telling me about your major and college. Bye!", \
                 "A classic choice! Thanks for telling me about your major and college. Bye!", \
                 "I don’t think enough people get a classical major, so that’s neat! Thanks for telling me about your major and college. Bye!"]

science_in = ["biology", "bioinformatics", "ecology", "behavior", "evolution", "human biology", \
              "microbiology molecular", "cell biology", "neurobiology biological sciences", \
              "biochemistry", "evolution", "human biology", "microbiology", "molecular physiology", \
              "neuroscience", "biochemistry", "chemistry", "molecular synthesis", "pharmacological chemistry" \
              "chem", "bio"]

science_out = ["Wow, didn’t know I was speaking with a scientist! Thanks for telling me about your major and college. Bye!", \
               "You must have read a lot of science books. Thanks for telling me about your major and college. Bye!", \
               "I wonder if you’re studying for Medical School. Thanks for telling me about your major and college. Bye!", \
               "I’ve never been too strong in the science field. Thanks for telling me about your major and college. Bye!"]

lang_ling_culture_in = ["chinese", "german", "italian", "japanese", "jewish", "latin", "america", "linguistics", \
                        "english", "literature", "writing", "third world studies",]
lang_ling_culture_out = ["Wow, you must be very cultured! Thanks for telling me about your major and college. Bye!", \
                         "I bet you have high cultural intelligence. Thanks for telling me about your major and college. Bye!", \
                         "Language and Culture is power! You should be proud to be studying your major! Thanks for telling me about your major and college. Bye!"]

cognitive_in = ["cognitive", "cognition","machine learning", "behavioral neuroscience"]
cognitive_out = ["You must not be a big fan of zombies since they eat brains! Thanks for telling me about your major and college. Bye!", \
                 "You must know a lot about the brain. Thanks for telling me about your major and college. Bye!"]

communication_in = ["communication", "communications"]
communication_out = ["You must be good with talking with others. Thanks for telling me about your major and college. Bye!", \
                     "I bet you’re great at networking. Thanks for telling me about your major and college. Bye!"]

computer_in = ["computer" "computer science", "computer sciences bioinformatics", "data science", "comp", "compsci", "comp sci"]
computer_out = ["You must know how to code! Thanks for telling me about your major and college. Bye!", \
                "I hope Python is your favorite coding language! Thanks for telling me about your major and college. Bye!"]

gender_in = ["critical gender", "gender"]
gender_out = ["Gender is a super important topic to study! Thanks for telling me about your major and college. Bye!", \
              "Gender identity and representation is powerful. Thanks for telling me about your major and college. Bye!"]

econ_math_in = ["economics", "econ","economics and mathematics", "management" "mathematics", "statistics", "math", "stats", "real estate"]
econ_math_out = ["You must be good with numbers. Thanks for telling me about your major and college. Bye!", \
                 "You must be good with money. Thanks for telling me about your major and college. Bye!"]

education_in = ["education", "edu"]
education_out = ["Education is power! Thanks for telling me about your major and college. Bye!", \
                 "I see we have a future teacher in the making! Thanks for telling me about your major and college. Bye!"]

engineering_in = ["engineering", "electrical", "bioengineering", "biotechnology", "bioinformatics", "biosystems", \
                  "structural", "nanoengineering", "mechanical"]
engineering_out = ["Didn’t know I was speaking with a future engineer! Thanks for telling me about your major and college. Bye!", \
                   "Engineering, you must have worked hard to make your way to this major"]

environmental_in = ["environmental", "earth", "marine", "oceanic", "atmospheric", "ocean"]
environmental_out = ["Global warming is a real issue. Thanks for telling me about your major and college. Bye!", \
                     "You will be the change to saving our world. Thanks for telling me about your major and college. Bye!"]

creative_arts_in = ["music", "interdisciplinary computing", "dance", "theatre", "visual","criticism", \
                    "interdisciplinary", "media", "design", "studio", "art", "creative"]
creative_arts_out = ["You must be creative! Thanks for telling me about your major and college. Bye!", \
                     "You must be very talented in your field! Thanks for telling me about your major and college. Bye!"]

political_in = ["political", "politics","public law"]
political_out = ["Sorry, I don’t want to talk about politics. Thanks for telling me about your major and college. Bye!", \
                 "I’m not good with political topics. Thanks for telling me about your major and college. Bye!"]

philosophy_in = ["philosophy", "phil"]
philosophy_out = ["You must be a philosophical person Thanks for telling me about your major and college. Bye!", \
                  "You must know a lot about the nature of knowledge, life, reality, and purpose. Thanks for telling me about your major and college. Bye!"]

physics_in = ["physics", "physic"]
physics_out = ["I am not good at physics. Thanks for telling me about your major and college. Bye!", \
               "Too many equations for me! Thanks for telling me about your major and college. Bye!"]

psychology_in = ["psychology", "psych"]
psychology_out = ["Wow, do I see a future psychologist in the making? Thanks for telling me about your major and college. Bye!", \
                  "You must be good at analyzing human behavior. Thanks for telling me about your major and college. Bye!"]

health_in = ["health", "global health"]
health_out = ["Health is important! Thanks for telling me about your major and college. Bye!", \
              "The health of our world should be everyone’s priority. Thanks for telling me about your major and college. Bye!"]
 
uncommon_in = ["international", "aerospace", "religion", "sociology", "urban", "ethnic", "history", "human developmental"]
uncommon_out = ["That’s a neat major!. I don’t think enough people study that. Thanks for telling me about your major and college. Bye!" \
                "A very interesting major, I’m sure you’ll get far with that! Thanks for telling me about your major and college. Bye!"]
                    
undeclared_in = ["undeclared", "undecided", "none", "idk", "i do not know", "i do not know yet"]
undeclared_out = ["It’s okay not to know! Thanks for telling me about your college. Bye"]



#Output response if value is unknown
UNKNOWN = ["Oh. I'm not sure how to answer that. Can you try answering my question again?", \
           "Sorry, the person who created me doesn't know how to write good code so I don't know how to answer that. Can you try answering my question again?"]









def end_chat(input_list):
    """Functions from A3 Assignment. If user types out 'quit', 
    the output will return True ending the chatbot function """
    
    if "quit" in input_list:
        output = True 
    else:
        output = False
    return output


def prepare_text(input_string):
    """Functions from A3 Assignment. Will format input text to being 
    all lower case with lower meathod. Input text will also remove punction using 
    remove_punctionation function"""
    
    temp_string = input_string.lower()
    temp_string = remove_punctuation(temp_string)
    out_list = temp_string.split()
    return out_list 


def remove_punctuation(input_string):
    """Functions from A3 Assignment. Will format input to remove punction and return output to 
    variable out_string"""
    
    out_string = ""
    for char in input_string:
        if char not in string.punctuation:
            out_string = out_string + char
    return out_string


def ucsd_college(msg):
    """A function used to check if the users input matches one of the keyword of a college from college variables. 
    If so, it will output a response related to the college. If the user input does not match 
    any of the keywords of one of the college varaibles, it will return a message to try entering a college again."""

    for msg in msg:
        if msg in seventh_student_in:
            response = random.choice(seventh_student_out)
            return response
        elif msg in sixth_student_in:
            response = random.choice(sixth_student_out)
            return response 
        elif msg in erc_student_in:
            response = random.choice(erc_student_out)
            return response 
        elif msg in warren_student_in:
            response = random.choice(warren_student_out)
            return response 
        elif msg in marshall_student_in:
            response = random.choice(marshall_student_out)
            return response
        elif msg in muir_student_in:
            response = random.choice(muir_student_out)
            return response
        elif msg in revelle_student_in:
            response = random.choice(revelle_student_out)
            return response 
        else:
            return "I don't think that's a college here on campus. Can you try typing your college again."

        
def ucsd_major(msg):
    """A function used to check if the users input matches one of the keyword of a major variables.
    If so, it will output a response related to the major variables. If the user input does not match 
    any of the keywords of the major variables. It will return a message to try entering a major again."""

    for msg in msg:
        if msg in anthropology_in:
            major_response = random.choice(anthropology_out)
            return major_response
        elif msg in classical_in:
            major_response = random.choice(classical_out)
            return major_response
        elif msg in science_in:
            major_response = random.choice(science_out)
            return major_response
        elif msg in lang_ling_culture_in:
            major_response = random.choice(lang_ling_culture_out)
            return lang_ling_culture_out
        elif msg in cognitive_in:
            major_response = random.choice(cognitive_out)
            return cognitive_out
        elif msg in communication_in:
            major_response = random.choice(communication_out)
            return major_response
        elif msg in computer_in:
            major_response = random.choice(computer_out)
            return major_response
        elif msg in gender_in:
            major_response = random.choice(gender_out)
            return major_response
        elif msg in econ_math_in:
            major_response = random.choice(econ_math_out)
            return major_response
        elif msg in education_in:
            major_response = random.choice(education_out)
            return major_response
        elif msg in engineering_in:
            major_response = random.choice(education_out)
            return major_response
        elif msg in environmental_in:
            major_response = random.choice(environmental_out)
            return major_response
        elif msg in creative_arts_in:
            major_response = random.choice(creative_arts_out)
            return major_response
        elif msg in political_in:
            major_response = random.choice(political_out)
            return major_response
        elif msg in philosophy_in:
            major_response = random.choice(philosophy_out)
            return major_response
        elif msg in physics_in:
            major_response = random.choice(physics_out)
            return major_response
        elif msg in psychology_in:
            major_response = random.choice(psychology_out)
            return major_response
        elif msg in health_in:
            major_response = random.choice(health_out)
            return major_response
        elif msg in uncommon_in:
            major_response = random.choice(uncommon_out)
            return major_response
        elif msg in undeclared_in:
            major_response = random.choice(undeclared_out)
            return major_response
        else:
            return "I don't recognize that major. Can you try typing out your major again?"

        
def ucsd_student_chat(): 
    """A function to allow my chatbot to run. This chatbot will make a comment about a person's college and major at UCSD 
    by looking at keywords within both college variables and major variables looking for certain inputs to output a 
    specific response"""
    
    chat = True
    said_college = False
    said_major = False
    greeted = False
    
    while chat:

        # Get a message from the user. 
        msg = input('INPUT :\t')
        out_msg = None


        # Prepare the input message to adjust to lower case and remove punctuation 
        msg = prepare_text(msg)

        # Check for an end msg 
        if end_chat(msg):
            out_msg = "Hope to talk to you again! Bye!"
            chat = False

        #   Here, we will check for a series of topics that we have designed to answer to
        if not out_msg:

            # Initialize to collect a list of possible outputs
            outs = []

            # Output as first message regardless of what message is inputted
            if not greeted:
                outs = ["Hello :) What college you are in at UCSD. If you do not want to talk to me, type 'quit'"]
                greeted = True
            
            #Will check if college is inputted by user. If not, it will ask for the question again
            elif (not said_college) and greeted:
                false_resp = "I don't think that's a college here on campus. Can you try typing your college again."
                curr_response = ucsd_college(msg)
                if curr_response != false_resp and (curr_response is not None):
                    said_college = True
                outs.append(curr_response)
            
            #Will check if major is inputted by user. If not, it will ask for the question again. If so, it ends chat
            elif (not said_major) and said_college:
                college_resp = ucsd_major(msg)
                false_college = "I don't recognize that major. Can you try typing out your major again?" 
                if college_resp != false_college and (college_resp is not None):
                    said_major = True
                    chat = False
                outs.append(college_resp)
            

            options = list(filter(None, outs))
            if options:
                out_msg = random.choice(options)
        

        #If input is not recongized, it will output a response from unknown variable
        if not out_msg:
            out_msg = random.choice(UNKNOWN)

        print('OUTPUT:', out_msg)