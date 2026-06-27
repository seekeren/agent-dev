from langchain_community.embeddings import DashScopeEmbeddings

embed_model = DashScopeEmbeddings()

print(embed_model.embed_query("我喜欢你"))
print(embed_model.embed_documents(["我喜欢你", "我稀饭你", "晚上吃什么"]))
