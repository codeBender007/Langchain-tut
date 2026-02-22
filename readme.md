langchain = llamaindex = heystack
ya teeno framework use hote hai model se output lene ke liya.

chatbot or Ai agents me bs yahi difference hai ke aiAgent ke pass tools,reasoning hoti hai tool=calculator

----------------------------

embedding model = Embedding model input ko numbers me convert karta hai, aur ye numbers 
                    meaning ko represent karte hain. or ya numbers relations ke base pr design kre jate hai. jese 
                    king(1)=queen(2) isme ham input me text bhejte hai or output numbers
                    ki form me milta hai jiski wajh se ham sementic search bi krwa skte hai

language model = ya sirf text generate krke deta hai. or iske input me text jata hai to ouput me text
                hi ata hai.


languageModel:
              1) chat models (lkn ab ya famous ho rha hai isme memory or role base system hota hai)
              2) llms (isme memory ni hoti isme act as dr, teacher ya ni hota)


-----------------------------


==>OpenAI ek company hai.Yeh apne AI models ko API ke through use karne deti hai.
==>Hugging Face company nahi, balki ek platform hai jahan thousands of different companies ke AI models milte hain.


------------------------------

langchain (6 components)
1) model (language model , embedding model inke hi code krta hai bs)
2) prompts
3) chains 
4) indexes (doc loader , text splitter , vector store , retriever)
5) memory (1 ques ke bad 2 ques me ai ko yad hi ni hota ke kya ques pujha th isse phle 
            isliya llm api stateless hoti hai.)
            ( 1)coversationBufferMemory , 2)coversationBufferWindowMemory , 3)summerize-base memory
                4) custom memory )
6) agents

-----------------------------------------


Model
langchain me jo model component hai ya componentek trh se code provide krwata hai jiski wajh agr ham koi sa bi model use krenge to hame mostly same hi code likhna hoga jese embedding model , language model

models : ya ke normal train model hote hai ya bi ek trh se engine hi hota hai
chatModel : lkn ya model ko use krke ek acha output generate krke dete hai in dono ko ham engine 
            asssume kr sakte hai

1) llmodel
2) chat Model
3) Embedding Model
 
2 trh se ham model use kr skte hai ek api ke through or dusra model ko download krke 
or jo openai ki api hoti hai wo hmesha paid hi hoti hai

or huggingface me bhot sare model ese hai jinhe ham sirf api ke through use ni kr skte hai. 

ya kjh open source model hai jo huggingface pr milte hai.
SOME OPEN SOURCE MODEL.
1) llama-2-7B/13B/70B   || Meta AI
2) Mixtral-8x7B         || Mistral AI
3) Mistral-7B           || Mistral AI
4) Falcon7B/40B         || TII UAE
5) BLOOM-176B           || Big Science
6) GPT-j-6B             || EleUtherAI

-----------------------------
