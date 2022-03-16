#! Python 3 Shebang Line
# write a code for Random Quiz with Q/A in random fashion, along with the exact answers.
# General Knowledge : First in the World
import random
GK_First_World_MALE = {
          'First Asian to Head the International Cricket Council':'Jagmohan Dalmiya',
          'First man to climb Mount Everest':'Sherpa Tenzing Norgay and Sir Edmund Hillary (29th May, 1953)',
          'First Man to go into Space':'Major Yuri Gagarin (USSR) (1961)',
          'First Man to walk into Space': 'Alexei Leonov (Russia)',
          'First Person to give information about Planets and their motion around the Sun':'Nicolous Copernicus',
          'First Man to compile Encyclopaedia': 'Aspheosis (Athens)',
          'First Person to go on both the Poles (North and South)': 'Ranulph Fiennes',
          'First Man to reach North Pole': 'Robert Peary',
          'First Man to reach South Pole': 'Roald Amundsen',
          'First Man to climb on Mt Everest without Oxygen': 'Phu Dorji Sherpa',
          'First Secretary of United Nation': 'Trygve Lie (Norway)'
}
print(GK_First_World_MALE)

# Generate Questions and Answers .txt files with preliminary header information
for Ques in range(15):
    QuesFile = open(f'GK_FirstMALE_Worldquiz{Ques + 1}.txt', 'w')
    AnsFile = open(f'GK_FirstMALE_Worldquiz_answers{Ques + 1}.txt', 'w')
    QuesFile.write('Name of the Student:\nDate of Exam :\nSchool Name:\n')
    QuesFile.write((' ' * 20) + f' GK_FirstMALE_World Quiz (SET-{Ques + 1})')
    QuesFile.write('\n')

    First_World = list(GK_First_World_MALE.keys())
    random.shuffle(First_World)

    for NumQues in range(1):

        correctAnswer = GK_First_World_MALE[First_World[NumQues]]
        wrongAnswers = list(GK_First_World_MALE.values())
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