import pandas as pd
from Levenshtein_Distance import levenshtein_distance

class SimpleChatBot:
    def __init__(self, filepath):
        self.questions, self.answers = self.load_data(filepath)

    def load_data(self, filepath):
        data = pd.read_csv(filepath)
        questions = data['Q'].tolist()  # 질문열만 뽑아 파이썬 리스트로 저장
        answers = data['A'].tolist()   # 답변열만 뽑아 파이썬 리스트로 저장
        return questions, answers

    def find_best_answer(self, input_sentence):

        min_distance = 99999999  # 초기값을 매우 큰 값으로 설정 (거리가 가장 가까운 질문을 찾기 위함)
        best_match = "" # 가장 유사한 질문을 저장할 변수

        # 입력된 문장과 각 질문 사이의 레벤슈타인 거리를 계산하여 가장 유사한 질문 찾기
        for question in self.questions:
            # 레벤슈타인 거리 계산
            distance = levenshtein_distance(input_sentence, question)
            # 이전에 찾은 항목보다 거리가 작을 경우 해당 질문을 가장 유사한 질문으로 저장
            if distance < min_distance:
                min_distance = distance
                best_match = question

        # print(f"Best match: {best_match}, Distance : {min_distance}")
        best_match_index = self.questions.index(best_match)  # 가장 유사한 질문의 인덱스 찾기
        return self.answers[best_match_index]

# CSV 파일 경로를 지정하세요.
filepath = 'ChatbotData.csv'

# 간단한 챗봇 인스턴스를 생성합니다.
chatbot = SimpleChatBot(filepath)

# '종료'라는 단어가 입력될 때까지 챗봇과의 대화를 반복합니다.
while True:
    input_sentence = input('You: ')
    if input_sentence.lower() == '종료':
        break
    response = chatbot.find_best_answer(input_sentence)
    print('Chatbot:', response)
    
