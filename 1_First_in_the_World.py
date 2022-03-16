#! Python 3 Shebang Line
# write a code for Random Quiz with Q/A in random fashion, along with the exact answers.
# General Knowledge : First in the World
import random
GK_First_World = {
          'First Radio Telescope Satellite launched into Space': 'HALCA (Japan)',
          'First country to use Glass':' Egypt and Mesopotamia',
          'First country to make Map':'The Greeks',
          'First Spaceship landed on Mars':'Viking-I (July 1976)',
          'World’s First Multipurpose River Valley Project' :'Tennessee River Valley Project (USA)',
          'First Space Shuttle Launched':'Columbia (April 1981)',
          "First Rocket to go near the Sun": "Helius ‘B’",
          'First Country to make written Constitution': 'The USA',
          'First Country to start Underground Metro Rail': 'Britain',
          'First Unmanned Mission on the Moon' :'LUNA-9',
          'First Spacecraft to carry man on the Moon': 'Apollo - 11',
          'First Country to do Artificial Satellite Experiment': 'Russia',
          'Country to give Voting Right to Women': 'New Zealand',
          'First Country to appoint Lokpal': 'Sweden',
          'First Country to imposed Carbon Tax': 'New Zealand'
}
#print(GK_First_World)

# Generate Questions and Answers .txt files with preliminary header information
for Ques in range(15):
    QuesFile = open(f'GK_First_Worldquiz{Ques + 1}.txt', 'w')
    AnsFile = open(f'GK_First_Worldquiz_answers{Ques + 1}.txt', 'w')
    QuesFile.write('Name of the Student:\nDate of Exam :\nSchool Name:\n')
    QuesFile.write((' ' * 20) + f' GK_First_World Quiz (SET-{Ques + 1})')
    QuesFile.write('\n')

    First_World = list(GK_First_World.keys())
    random.shuffle(First_World)

    for NumQues in range(1):

        correctAnswer = GK_First_World[First_World[NumQues]]
        wrongAnswers = list(GK_First_World.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)


    for NumQues in range(1):
        QuesFile.write(f'{NumQues + 1}.{First_World[NumQues]}?\n')
    for i in range(4):
        QuesFile.write(f"{'ABCD'[i]}. {answerOptions[i]}\n")
        QuesFile.write('\n')
        AnsFile.write(f"{NumQues + 1}.{'ABCD'[answerOptions.index(correctAnswer)]}")
    QuesFile.close()
    AnsFile.close()