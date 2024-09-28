def som(**kwargs):
    hi, name, number = kwargs.values()
    feedback = kwargs.get('feedback', 'TBD')

    print(feedback)

som(hi="hello", name='jona', number=344, feedback="Its ok man")
