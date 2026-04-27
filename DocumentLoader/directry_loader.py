from langchain_community.document_loaders import DirectoryLoader , PyPDFLoader

loader = DirectoryLoader(
    path='Books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
    # iska mtlb yahai ke is folder me jtne bi is extension ki files hai sari fetch krlo
)


docs= loader.load()


print(len(docs))
print(docs[0].page_content)
print(docs[0].metadata)






# docs= loader.lazy_load()

# for document in docs:
#     print(document.metadata)


# load phle puri document ek sath memory me store krta hai fir output deta hai

# lazy_load me ek ek krke memory me store hota hai or ek ek krke output show hota hai