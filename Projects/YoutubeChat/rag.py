# hame har process ko invoke function se run krna pad rha hai isse code bhot slow chl rha hai 
# isliya hame sare process ko alag alag run na krke un sabki (chain) bna lena chahia 

from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint , HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from youtube_transcript_api import YouTubeTranscriptApi , TranscriptsDisabled
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel , RunnablePassthrough , RunnableLambda
from langchain_core.output_parsers import StrOutputParser

load_dotenv()



# process = huggingface ke model ka setup krna 
llm1 = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-1B-Instruct",
    task='texxt-generation'
)
model = ChatHuggingFace(llm=llm1)
# ********************************


# please get those video id which video on description 

# video_id = 'LPZh9BOjkQs' #tut video 
# video_id='X0btK9X0Xnk' #langchain 
# video_id='TJAfLE39ZZ8' #song

# process1 = fetch subtitle from youtube that is document
video_id='Gfr50f6ZBvo' #podcast
# video_id='TtPXvEcE11E' #react js
try:
    api = YouTubeTranscriptApi()
    transcript_list = api.fetch(
        video_id,
        languages=['en', 'hi']
    )
    transcript = " ".join(chunk.text for chunk in transcript_list)
    # print("video document")
    # print(transcript)

except TranscriptsDisabled:
    print("No Captions available for this video")
# ****************************


# process2 =  for creating chunk split text 
splitter = RecursiveCharacterTextSplitter(chunk_size=1000 , chunk_overlap=200)
chunks = splitter.create_documents([transcript])
# ******************************


# process3 = isme ham chunks ko vector chunks me convert krrhe hai.
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
# ********************

# process4 = FAISS is db for storing vector chunks isme ham vector ko store kr rhe hai
vectorstore = FAISS.from_documents(chunks , embeddings)
# print(vectorstore)
# print(len(chunks))
# print(chunks[0])
# *****************************


# process5 = ya hai retriever isse ham vector store se most relavant chunk find krenge.
retriever = vectorstore.as_retriever(search_type='similarity' , search_kwargs={'k':4})
# asn = retriever.invoke("Proper React Setup with Vite")
# print(asn)
# *********************************


# process6 = augmentation mtlb prompt bnana (MRC+query) || Prompt engineering (Optimized for Llama-3.2-1B)
prompt = PromptTemplate(
    template="""<|begin_of_text|><|start_header_id|>system<|end_header_id|>
You are a helpful AI assistant. Analyze the provided context of a video transcript and answer the user's question.
- Rely only on the clear facts mentioned in the context.
- Keep your answer concise and direct.
- If the context doesn't mention the topic at all, only then say "I don't know".<|eot_id|><|start_header_id|>user<|end_header_id|>

Here is the context (transcript segments):
{context}

Question: {question}<|eot_id|><|start_header_id|>assistant<|end_header_id|>""",
    input_variables=['context', 'question']
)
question = "is the topic of nuclear fusion discussed in this video? if yes then what was discussed"
# question = "How can we set up TypeScript with React using Vite?"
# ****************************

# process7 = most relavant chunks(MRC) with string isme sab hat gya metadata wagera sab
def formate_docs(retriver):
    retrieved_docs = retriever.invoke(question)
    context_text = "\n\n".join(docs.page_content for docs in retrieved_docs)
    # print(context_text)
    return context_text
# ***********************

# create chain 
parallel_chain = RunnableParallel({
    'context' : retriever | RunnableLambda(formate_docs),
    'question' : RunnablePassthrough()
})

parser = StrOutputParser()

rag_chain = parallel_chain | prompt | model | parser
# ***************************************


# process8 = create prompt (query + MRC)
# final_prompt = prompt.invoke({'context':context_text , 'question':question})
final_prompt = rag_chain.invoke('can you summarize the video')
# ************************


# process9 = generation
result = model.invoke(final_prompt)
print("****************************************")
print(result.content)
