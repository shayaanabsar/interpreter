num = 0
stdout "Enter a number"
stdin num

switch (num) {
    case 1 {
        stdout "Number is 1"
    }
    case 2 {
        stdout "Number is 2"
    }
    case default {
        stdout "Number is not 1 or 2"
    }
}