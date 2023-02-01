def add_score(subject_score, subject, score):
    subject_score.update({subject:score})    
    return subject_score
def calc_average_score(subject_score):
    sum=0
    for subject in subject_score.keys():
        sum += subject_score[subject]
    return '%.2f' %(sum / len(subject_score))