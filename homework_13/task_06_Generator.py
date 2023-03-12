#Cпособ решения через yield , без использования интераторов
def generate_words(text):
    for word in text.split():
        yield word

text = "Vsem privet rebyata kak vashi dela"
for word in generate_words(text):
    print(word)

if __name__ == '__main__':
    assert generate_words('poka rebyta ahaha')
    assert generate_words('poka rebyta , ahaha')
    assert not generate_words('poka rebyta ahaha')