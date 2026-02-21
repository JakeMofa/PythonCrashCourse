favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'golang',
}

freinds = ['phil', 'sarah']

for name in favorite_languages.keys():
    if name in freinds:
        language = favorite_languages[name].title()
        print(f' hello! you are very welcome {name} you are invited to study {language}')
    else:
        print(f'hello  thank you for coming {name}')
        
        
## or you could have put the print(f'hi {name} in the beginning')