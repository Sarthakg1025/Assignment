import math


def EucDistance(P1, P2):

    Ans = math.sqrt(
        (P1['StudyHours'] - P2['StudyHours']) ** 2 +
        (P1['Attendance'] - P2['Attendance']) ** 2
    )

    return Ans


def KNNClassifier(k=3):

    border = "-" * 30

    Data = [
        {'StudyHours': 2, 'Attendance': 60, 'Result': 'Fail'},
        {'StudyHours': 5, 'Attendance': 80, 'Result': 'Pass'},
        {'StudyHours': 6, 'Attendance': 85, 'Result': 'Pass'},
        {'StudyHours': 1, 'Attendance': 50, 'Result': 'Fail'}
    ]

    print(border)
    print("KNN Classifier")
    print(border)

    for d in Data:
        print(d)

    print(border)

    # Accept input from user
    StudyHours = float(input("Enter Study Hours: "))
    Attendance = float(input("Enter Attendance: "))

    new_point = {
        'StudyHours': StudyHours,
        'Attendance': Attendance
    }

    print(border)
    print("Distances of all students : ")
    print(border)

    # Calculate distance
    for d in Data:

        d['distance'] = EucDistance(
            d,
            new_point
        )

    for d in Data:
        print(d)

    print(border)

    # Sort according to distance
    sorted_data = sorted(
        Data,
        key=lambda item: item['distance']
    )

    print("Sorted Data : ")
    print(border)

    for d in sorted_data:
        print(d)

    print(border)

    # Select K nearest neighbours
    nearest = sorted_data[:k]

    print("Nearest", k, "students are : ")
    print(border)

    for d in nearest:
        print(d)

    print(border)

    # Voting
    votes = {}

    for neighbours in nearest:

        result = neighbours['Result']

        votes[result] = votes.get(result, 0) + 1

    print("Voting result is : ")
    print(border)

    for d in votes:

        print(
            "Result : ",
            d,
            " Number of votes : ",
            votes[d]
        )

    print(border)

    # Find maximum votes
    iMax = 0
    Name = ""

    for d in votes:

        if votes[d] > iMax:

            iMax = votes[d]
            Name = d

    print("Predicted Result :", Name)

    print(border)

    return Name


def main():

    KNNClassifier(3)


if __name__ == "__main__":
    main()