from trendspy import Trends

def trend_search(query = None):
    """find currently trending topics, google trends data, and popular keywords for any subject"""
    try:
        tr = Trends()
        if query:
            data = tr.interest_over_time([query], timeframe = "today 3-m")

            latest = data[query].tail(5).to_dict()
            result = {}
            for date, value in latest.items():
                result[str(date.date())] = value
            return {
                "🔍 Query"  : query,
                "📈 Trends" : result
            }
        else:
            trending = tr.trending_now(geo = "US")
            results = []
            for t in trending[:10]:
                results.append({
                    "🔥 Keyword" : t.keyword,
                    "📈 Volume"  : t.volume
                })
            return results
    except Exception as e:
        print(e)
        return "> Google Trends: data not found."