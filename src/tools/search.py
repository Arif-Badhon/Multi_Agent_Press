"""
src/tools/search.py
Encapsulates the Tavily search logic for AI agents.
"""
import os
from tavily import TavilyClient

def search_web(query: str, max_results: int = 5) -> str:
    """
    Searches the web using Tavily (optimized for LLMs).
    """
    print(f"\n[Tool] 🔎 Searching for: '{query}'...")
    
    api_key = os.environ.get("TAVILY_API_KEY")
    if not api_key:
        return "Error: TAVILY_API_KEY not found in environment variables."

    try:
        # Initialize client
        client = TavilyClient(api_key=api_key)
        
        # 'search_depth="basic"' is faster/cheaper. Use "advanced" for deep research.
        response = client.search(
            query=query, 
            max_results=max_results,
            include_answer=True, # Tavily tries to answer the question directly
            search_depth="basic"
        )
        
        results = response.get("results", [])
        
        # Tavily also provides a direct AI-generated answer sometimes
        direct_answer = response.get("answer", "")
        
        formatted_output = []
        
        if direct_answer:
            formatted_output.append(f"Direct Answer: {direct_answer}\n")

        for i, res in enumerate(results, 1):
            title = res.get('title', 'No Title')
            url = res.get('url', 'No Link')
            # Tavily gives 'content' which is richer than a standard snippet
            content = res.get('content', 'No Content')
            
            formatted_output.append(
                f"{i}. {title}\n   Source: {url}\n   Content: {content}\n"
            )

        return "\n".join(formatted_output)

    except Exception as e:
        return f"Error performing search: {str(e)}"

if __name__ == "__main__":
    # Test the tool directly
    print(search_web("DeepSeek vs Gemini"))