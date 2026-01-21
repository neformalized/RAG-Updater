import rag
import asyncio

from static import llm

class Holder:
    
    def __init__(self, source_path: str):
        
        self.source_path = source_path
        
        self.build_store()
        
        self._lock = asyncio.Lock()
    #
    
    def build_store(self):
        
        with open(self.source_path, "r", encoding="utf-8") as file:
            
            self._store = rag.RAG(file.read())
        #
    #
    
    async def query(self, question: str) -> str:
        
        async with self._lock:
            
            return self._store.query(question)
        #
    #
    
    async def update(self, question: str, answer: str):
        
        async with self._lock:
            
            with open(self.source_path, "a+", encoding="utf-8") as file:
                
                file.seek(0)
                
                qa_base = file.read()
                
                file.write("\n\n" + llm.generate_qa(qa_base, question, answer))
                
                file.close()
            #
            
            self.build_store()
        #
    #
#