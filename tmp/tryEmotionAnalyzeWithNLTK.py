#未動作
import nltk

# ➊辞書のダウンロード
nltk.download('vader_lexicon')
# ➋感情強度分析クラスのインポート
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# ➌インスタンスの生成
vader_analyzer = SentimentIntensityAnalyzeFr()

text = "I am happy."

result = vader_analyzer.polarity_scores(text)
print(text + "\n", result)