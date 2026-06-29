from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.document_loaders import CSVLoader

from langchain_chroma import Chroma
from openai import vector_stores

# vector_store = InMemoryVectorStore(embedding=DashScopeEmbeddings())

vector_store = Chroma(
    collection_name="test",
    embedding_function=DashScopeEmbeddings(),
    persist_directory="./chroma_db"
)

# csv_loader = CSVLoader(
#     file_path="./data/info.csv",
#     encoding="utf-8",
#     source_column="source")
#
# csv_documents = csv_loader.load()
#
# # 构建基于内存的向量存储，完成向量的增加、删除、查询
# vector_store.add_documents(
#     documents=csv_documents,
#     ids = ["id" + str(i) for i in range(1, len(csv_documents) +1 )]
# )

# vector_store.delete(["id1", "id2"])

search_result = vector_store.similarity_search(
    "Python是不是简单易学呀",
    3,
    filter={"source": "黑马程序员"}
)

print(search_result)
