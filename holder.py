from rag import RAG
import asyncio

class Holder:
    
    def __init__(self, source_path: str):
        
        self.source_path = source_path
        self.build_store(source_path)
        
        self._lock = asyncio.Lock()
    #
    
    def build_store(self, source_path: str):
        
        with open(source_path, "r", encoding="utf-8") as file:
            
            self._store = RAG(file.read())
        #
    #
    
    async def query(self, question: str) -> str:
        
        async with self._lock:
            
            return self._store.query(question)
        #
    #
    
    async def update(self, question: str, answer: str):
        
        async with self._lock:
            
            pass
        #
    #
#