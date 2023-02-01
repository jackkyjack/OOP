def add_score(subject_score, student, subject, score): 
    if student not in subject_score.keys():
      subject_score.update({student:{subject:score}})
    else:
      subject_score[student].update({subject:score})
    return subject_score
def calc_average_score(subject_score):
    new={}
    average_score=0
    for student in subject_score.keys():
        all = subject_score[student]
        for subject in all.keys():
            average_score += subject_score[student][subject]
    average_score = average_score / len(all)
    new.update({student:'%.2f' %(average_score)})
    return new