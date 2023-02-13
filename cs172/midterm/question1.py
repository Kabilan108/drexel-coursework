# CS 172 - Midterm Question 1 (Zybooks 15.2)
# Purpose: IMplementation of a Gymmember class and its main script
# Author:  Tony Kabilan Okeke (tko35)
# Date:    02.13.2023


class GymMember:

    # Static attribute to count member numbers
    __nextMembershipNumber = 1001

    def __init__(self, name: str, member_type: str='month-to-month'):
        """Class constructor"""
        self.__memberName = name
        self.__membershipType = member_type
        self.__membershipDues = 0.0
        self.__memberNumber = GymMember.getNextMembershipNumber()
        
    def getMemberName(self):
        """Returns the name of the member"""
        return self.__memberName
    
    def getMembershipType(self):
        """Returns the membership type"""
        return self.__membershipType
    
    def getMemberNumber(self):
        """Returns the member number"""
        return self.__memberNumber
    
    def getMembershipDues(self):
        """Returns the membership dues"""
        return self.__membershipDues
    
    def calculateYearlyDues(self):
        """Calculates the membership dues"""
        if self.__membershipType == 'month-to-month':
            self.__membershipDues = 39.99 * 12
        elif self.__membershipType == 'annual':
            self.__membershipDues = 29.99 * 12
    
    def changeMembershipType(self, member_type):
        """Sets the membership type"""
        self.__membershipType = member_type
    
    @staticmethod
    def getNextMembershipNumber():
        """Returns the next available account number should start at 1000"""
        memberNumber = GymMember.__nextMembershipNumber
        GymMember.__nextMembershipNumber += 1
        return memberNumber

if __name__ == '__main__':
    
    member = GymMember('Tony', 'annual')

    member.changeMembershipType('month-to-month')

    member.calculateYearlyDues()

    annualdues = member.getMembershipDues()

    print(f'Member Number: {member.getMemberNumber()}')
    print(f'Member Name: {member.getMemberName()}')
    print(f'Membership Type: {member.getMembershipType()}')
    print(f'Annual Dues: ${annualdues:.2f}')
    print(f'Next Available Membership Number: {GymMember.getNextMembershipNumber()}')
