from yt_dlp import YoutubeDL

def youtube_search(query, max_result = 5):
    """search youtube for videos, tutorials, and content by keyword and return titles and urls"""
    try:
        options = {
            "quiet" : True,
            "extract_flat": True,
        }

        search = f"ytsearch{max_result}: {query}"
        print(search)

        with YoutubeDL(options) as yt:
            data = yt.extract_info(search   , download = False)

        results = []
        for v in data["entries"]:
            results.append({
                "🎬 title"    : v.get("title"),
                "🔗 url"      : f"https://youtube.com/watch?v={v.get('id')}",
                "⏱️ duration" : v.get("duration"),
                "👤 channel"  : v.get("channel")
            })

        return results
    except:
        return "> Youtube: data is unavailable."