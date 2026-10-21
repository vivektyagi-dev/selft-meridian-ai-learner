from rag.llm import get_llm, extract_text; 
r = get_llm().invoke('Reply with exactly: hello'); 
print(type(r.content).__name__, repr(extract_text(r.content)))