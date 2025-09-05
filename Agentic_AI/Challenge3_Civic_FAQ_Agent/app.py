
from tools.reader import search_files

def answer_query(q: str):
    q_norm = q.strip().lower()
    # Simple refusal policy examples:
    if any(x in q_norm for x in ["legal advice", "medical", "personal data"]):
        return {
            "answer": "I can't provide that. For safety and accuracy, please contact the appropriate professional or city help line.",
            "citations": [],
            "refused": True
        }
    hits = search_files(q_norm)
    if not hits:
        return {
            "answer": "I don't have that in the provided FAQs. Try rephrasing or ask a staff member.",
            "citations": [],
            "refused": True
        }
    cites = [f"{p} lines {ls[0]}–{ls[1]}" for p,ls,_ in hits]
    snippets = "\n---\n".join(sn for _,_,sn in hits)
    return {
        "answer": f"Here's what I found in the city FAQs:\n\n{snippets}\n\n(Always verify with the city website or helpline.)",
        "citations": cites,
        "refused": False
    }

def main():
    print("Civic Helper (demo). Type a question, or 'quit' to exit.")
    while True:
        q = input("> ")
        if not q or q.strip().lower() == "quit":
            break
        res = answer_query(q)
        print(res["answer"])
        if res["citations"]:
            print("Citations:")
            for c in res["citations"]:
                print(" -", c)

if __name__ == "__main__":
    main()
