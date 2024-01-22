name = input('Enter your name: ')
print('Hello', name, ' How can I help you?')
print('1. I want to know about the weather')
print('2. I want to know about the news')
print('3. I want to know about the stock market')
print('4. I want to know about the sports')
print('5. I want to know about the music')
print('6. Close the application')

while True:
    try:
        choice = int(input('Enter your choice: '))
        if choice == 1:
            print('The weather is 30 degree celsius')
        elif choice == 2:
            print('The news is about the new vaccine')
        elif choice == 3:
            print('The stock market is down by 2%')
        elif choice == 4:
            print('The sports news is about the new player')
        elif choice == 5:
            print('The music is about the new song')
        elif choice == 6:
            print('Thank you for using our application')
            break
        else:
            print('Invalid choice')
    except ValueError:
        print('Invalid choice')