import math


def MarvellousEucDistance(P1, P2):

    Ans = math.sqrt(
        (P1['X'] - P2['X']) ** 2 +
        (P1['Y'] - P2['Y']) ** 2
    )

    return Ans


def MarvellousKNNClassifier(k):

    border = "-" * 30

    Data = [
        {'point': 'A', 'X': 1, 'Y': 2, 'label': 'Red'},
        {'point': 'B', 'X': 2, 'Y': 3, 'label': 'Red'},
        {'point': 'C', 'X': 3, 'Y': 1, 'label': 'Blue'},
        {'point': 'D', 'X': 5, 'Y': 6, 'label': 'Blue'},
        #{'point': 'E', 'X': 6, 'Y': 6, 'label': 'Blue'},
        #{'point': 'F', 'X': 3, 'Y': 4, 'label': 'Red'},
        #{'point': 'G', 'X': 3, 'Y': 2, 'label': 'Red'}
    ]

    # Same new point
    new_point = {'X': 6, 'Y': 2}

    print(border)
    print("Marvellous KNN Classifier")
    print(border)

    print("New Point : ", new_point)

    print(border)
    print("Distances of all points : ")
    print(border)

    # Calculate distances
    for d in Data:
        d['distance'] = MarvellousEucDistance(d, new_point)

    for d in Data:
        print(d)

    print(border)

    # Sort distances
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

    print("Nearest", k, "members are : ")
    print(border)

    for d in nearest:
        print(d)

    print(border)

    # Voting
    votes = {}

    for neighbours in nearest:

        label = neighbours['label']

        votes[label] = votes.get(label, 0) + 1

    print("Voting result is : ")
    print(border)

    for d in votes:

        print(
            "Name : ",
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

    print("Final prediction for K =", k, ":", Name)

    print(border)

    return Name


def main():

    print("Prediction Results")
    print("=" * 30)

    Result1 = MarvellousKNNClassifier(1)

    print()

    Result3 = MarvellousKNNClassifier(3)

    print()

    Result5 = MarvellousKNNClassifier(5)

    print()
    print("=" * 30)
    print("Final Prediction Results")
    print("=" * 30)

    print("K = 1 ->", Result1)
    print("K = 3 ->", Result3)
    print("K = 5 ->", Result5)


if __name__ == "__main__":
    main()