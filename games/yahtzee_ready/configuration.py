from dice import *

class Configuration:

    configs = [
        "Categoty", "Ones", "Twos", "threes", "Fours", "Fives", "Sixes",
        "Upper Scores", "Upper Bonus(35)",
        "3 of a kind", "4 of a kind", "Full House(25)",
        "Small Straight(30)", "Large Straight(40)", "Yahtzee(50)", "Chance",
        "Lower Scores", "Total"
    ]

    @staticmethod
    def getConfigs():       # 정적 메소드 (객체 없이 사용 가능)
        return Configuration.configs

    # row에 따라 주사위 점수를 계산하여 반환. 
    # 예를 들어, row가 0이면 "Ones"가, 2이면 "Threes"가 채점되어야 함을 의미. 
    # row가 득점위치가 아닌 곳(즉, UpperScore, UpperBonus, LowerScore, Total 등)을 나타내는 경우 -1을 반환.
    @staticmethod
    def score(row, dices):       # 정적 메소드 (객체 없이 사용 가능)
        # TODO: 구현
        result = 0
        if row == 0:
            for i in range(5):
                if dices[i].getRoll() == 1:
                    result += dices[i].getRoll()
        #Twos
        elif row == 1:
            for i in range(5):
                if dices[i].getRoll() == 2:
                    result += dices[i].getRoll()
        #Threes
        elif row == 2:
            for i in range(5):
                if dices[i].getRoll() == 3:
                    result += dices[i].getRoll() 
        #Fours
        elif row == 3:
            for i in range(5):
                if dices[i].getRoll() == 4:
                    result += dices[i].getRoll()
        #Fives
        elif row == 4:
            for i in range(5):
                if dices[i].getRoll() == 5:
                    result += dices[i].getRoll()
        #Sixes
        elif row == 5:
            for i in range(5):
                if dices[i].getRoll() == 6:
                    result += dices[i].getRoll()
        #Three of a kind X X X Y Z
        elif row == 8:
            dices = sorted(dices)
            if dices[0].getRoll() == dices[1].getRoll() and dices[1].getRoll() == dices[2].getRoll():
                for i in range(5):
                    result += dices[i].getRoll()
            elif dices[1].getRoll() == dices[2].getRoll() and dices[2].getRoll() == dices[3].getRoll():
                for i in range(5):
                    result += dices[i].getRoll()
            elif dices[2].getRoll() == dices[3].getRoll() and dices[3].getRoll() == dices[4].getRoll():
                for i in range(5):
                    result += dices[i].getRoll()
            else:
                result = 0
        #Four of a kind X X X X Y
        elif row == 9:
            dices = sorted(dices)
            if dices[0].getRoll() == dices[1].getRoll() and dices[1].getRoll() == dices[2].getRoll() and dices[2].getRoll() == dices[3].getRoll():
                for i in range(5):
                    result += dices[i].getRoll()
            elif dices[1].getRoll() == dices[2].getRoll() and dices[2].getRoll() == dices[3].getRoll() and dices[3].getRoll() == dices[4].getRoll():
                for i in range(5):
                    result += dices[i].getRoll()
            else:
                result = 0
        #Full Hosue X X X Y Y
        elif row == 10:
            dices = sorted(dices)
            if dices[0].getRoll() == dices[1].getRoll() and dices[1].getRoll() == dices[2].getRoll() and dices[3].getRoll() == dices[4].getRoll():
                result = 25
            elif dices[0].getRoll() == dices[1].getRoll() and dices[2].getRoll() == dices[3].getRoll() and dices[3].getRoll() == dices[4].getRoll():
                result = 25
            else:
                result = 0
        #Small Straight 1 2 3 4 ?, ? 1 2 3 4,  1 1 2 3 4, 1 2 2 3 4, 1 2 3 3 4,
        elif row == 11:
            dices = sorted(dices)
            #set에 집어넣고
            sortedDice = set()
            for d in dices:
                sortedDice.add(d.getRoll())
            #set안에 4개의 숫자가 있는지 확인
            getNum = 0
            for num in sortedDice:
                getNum += 1
            #dice라는 리스트 추가
            dice = list()
            #dice에 걸러진 숫자들 넣기
            for num in sortedDice:
                dice.append(num)
            #getNum이 4이고, 리스트 안의 숫자들이 연속되어있다면
            if getNum == 4 and dice[3] == dice[2] + 1 and dice[2] == dice[1] + 1 and dice[1] == dice[0] + 1:
                result = 30
            #result = 30
            # if dices[3].getRoll() == dices[2].getRoll() + 1 and dices[2].getRoll() == dices[1].getRoll() + 1 and dices[1].getRoll() == dices[0].getRoll() + 1:
            #     result = 30
            else:
                result = 0
        #Large Straight 1 2 3 4 5
        elif row == 12:
            dices = sorted(dices)
            if dices[4].getRoll() == dices[3].getRoll() + 1 and dices[3].getRoll() == dices[2].getRoll() + 1 and dices[2].getRoll() == dices[1].getRoll() + 1 and dices[1].getRoll() == dices[0].getRoll() + 1:
                result = 40
            else:
                result = 0
        #Yahtzee
        elif row == 13:
            if dices[0].getRoll() == dices[1].getRoll() and dices[1].getRoll() == dices[2].getRoll() and dices[2].getRoll() == dices[3].getRoll() and dices[3].getRoll() == dices[4].getRoll():
                result = 50
            else:
                result = 0                
        #Chance 
        elif row == 14:
            for i in range(5):
                result += dices[i].getRoll()                                                  
        else:
            result = 0
        return result

