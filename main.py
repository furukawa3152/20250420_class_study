from openai import OpenAI
import os

# APIキーを使ってOpenAIクライアントを初期化し、質問に回答する基本クラス
class get_openai_response:
    def __init__(self, model: str):
        self.client = OpenAI(api_key=os.environ["API_KEY"])
        self.model = model

    def get_response(self, question: str) -> str:
        # OpenAI API を呼び出し、簡潔な回答を得る
        pass


# 上のクラスを継承し、詳細な回答を返すようにする派生クラス
class DetailedOpenAIResponse(get_openai_response):
    def get_response(self, user_prompt: str) -> str:
        # 簡潔ではなく、詳細な回答を返す
        pass


# 依存性の注入：OpenAI クライアントを外部から注入するベースクラス
class OpenAIResponder:
    def __init__(self, client, model: str):
        self.client = client
        self.model = model

    def get_response(self, user_prompt: str, system_prompt: str) -> str:
        # 任意のシステムプロンプトで API を呼び出す
        pass





# 使用例（メイン処理）
if __name__ == "__main__":
    question = "pythonとは"
    client = OpenAI(api_key=os.environ["API_KEY"])

    # モデル名（例：gpt-4o-mini）
    model_name = "gpt-4o-mini"

    # クラスのインスタンス化
    responder = OpenAIResponder(client, model_name)

    # 質問とシステムプロンプトを設定
    current_question = "Pythonとは何ですか？"
    system_prompt = "日本語で簡潔に説明してください。"

    # レスポンスを取得して表示
    response_text = responder.get_response(current_question, system_prompt)
    print(response_text)

