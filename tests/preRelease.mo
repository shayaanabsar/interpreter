names = ["Person 1", "Person 2", "Person 3", "Person 4", ""]
volunteers = ["shop", "n", "pier", "painting", "shop", ""]
joiningDays = [10, 1, 28, 17, 3, 0]
joiningMonths = [1, 3, 5, 5, 2, 0]
joiningYears = [2000, 2015, 1998, 1983, 2018, 0]
paidFees = [True, True, False, True, False, False]


firstName = ""
lastName = ""
volunteer = ""

stdout "Enter your first name:"
stdin firstName

stdout "Enter your last name:"
stdin lastName

stdout "Would you like to volunteer (y/n)?:"
stdin volunteer

while (volunteer != "y" && volunteer != "n") {
    stdout "Invalid!"
    stdout "Would you like to volunteer (y/n)?:"
    stdin volunteer
}

if (volunteer == "y") {
    stdout "Where would you like to volunteer?"
    stdout "Enter 'pier' for pier entrance."
    stdout "Enter 'shop' for gift shop"
    stdout "Enter 'painting' for painting and decorating."

    stdout "Where would you like to volunteer?"
    stdin volunteer

    while (volunteer != "pier" && volunteer != "shop" && volunteer != "painting") {
        stdout "Invalid!"
        stdout "Where would you like to volunteer?"
        stdin volunteer
    }
}

joiningDay = 0
joiningMonth = 0
joiningYear = 0

stdout "What was the joining year?:"
stdin joiningYear

stdout "What was the joining month (as a number)?:"
stdin joiningMonth

while (joiningMonth < 1 || joiningMonth > 12) {
    stdout "Invalid!"
    stdout "What was the joining month (as a number)?:"
    stdin joiningMonth
}

stdout "What was the joining day?:"
stdin joiningDay

maxDays = 0
if (joiningMonth == 9 || joiningMonth == 4 || joiningMonth == 6 || joiningMonth == 11) {
    maxDays = 30
}
else {
    if (joiningMonth == 2) {
        if (joiningYear % 100 == 0) {
            if (joiningYear % 400 == 0) {
                maxDays = 29
            }
        }
        else {
            if (joiningYear % 4 == 0){
                maxDays = 29
            }
            else {
                maxDays = 28
            }
        }
    }
    else {
        maxDays = 31
    }
}

while (joiningDay < 1 || joiningDay > maxDays) {
    stdout "Invalid!"
    stdout "What was the joining day?:"
    stdin joiningDay
}

paid = ""
stdout "Have you paid the $75 fee? (y/n):"
stdin paid

while (paid != "y" && paid != "n") {
    stdout "Invalid!"
    stdout "Have you paid the $75 fee? (y/n):"
    stdin paid
}

func convertToBoolean(string) {
    switch string {
        case "y" {
            return True
        }
        case "n" {
            return False
        }
    }
}

paid = convertToBoolean(paid)

names[4] = firstName + " " + lastName
volunteers[4] = volunteer
joiningDays[4] = joiningDay
joiningMonths[4] = joiningMonth
joiningYears[4] = joiningYear
paidFees[4] = paid

stdout "Select from the following:"
stdout "Enter 'volunteers' view all who have chosen to work as volunteers"
stdout "Enter 'pier' to view volunteers who have chosen to work at the pier gate."
stdout "Enter 'shop' to view the volunteers who have chosen to work at the shop."
stdout "Enter 'painting' to view the volunteers who have chosen to work with painting and decorating."
stdout "Enter 'expired' to view the members whose memberships have expired."
stdout "Enter 'not paid' to view the members who haven't yet paid their $75 fee."


choice = ""
stdout "Enter your choice:"
stdin choice

while (choice != "volunteers" && choice != "pier" && choice != "shop" && choice != "painting" && choice != "expired" && choice != "not paid") {
    stdout "Invalid!"
    stdout "Enter your choice:"
    stdin choice
}

i = 0

if (choice == "pier" || choice == "shop" || choice == "painting") {
    while (i < 5) {
        if (volunteers[i] == choice) {
            stdout names[i]
        }
        i = i + 1
    }
}
if (choice == "expired") {
    while (i < 5) {
        if (joiningYears[i] < 2022) {
            stdout names[i]
        }
        i = i + 1
    }
}

if (choice == "not paid") {
    while (i < 5) {
        if (!(paidFees[i])) {
            stdout names[i]
        }
         i = i + 1
    }
}

if (choice == "volunteers") {
    while (i < 5) {
        if (volunteers[i] != "n") {
            stdout names[i]
        }
        i = i + 1
    }
}
