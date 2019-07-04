#modules used here -- sys is a very standard one
import sys


def repeat(s, exclaim):
    result = s *3

    if exclaim:
        
        result += "!!!"
    return result
    


def main():
    print( repeat('Woo Hoo ', True) )
    #print('Hello there', sys.argv[1])
    #print repeat("Yay", False)
    s = 'hi'
    print( s[1] )
    print(len(s))
    print( s + ' there')
    pi = 3.14
    text = 'The value of pi is ' + str(pi)
    print(text)
    raw = r'this\t\n and that'
    print(raw)
    multi = """It was the best of times. It was the worst of times."""
    print(multi)
    mood( 90, 'mood' )
    

def mood(speed, mood):
    if speed >= 80:
        print('License and registration please')
        if mood == 'terrible' or speed >= 100:
            print('You have the right to remain silent.')
        elif mood == 'bad' or speed >= 90:
            print("I'm going to have to write you a ticket.")
            write_ticket()
        else:
            print("let's try to keept it under 80 ok")

def write_ticket():
    print("my god! slow down!")


#Standard boiilerplate to call the main() function to begin
if __name__ == '__main__':
    main()