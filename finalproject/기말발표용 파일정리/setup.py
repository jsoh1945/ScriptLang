from distutils.core import setup, Extension

module_spam = Extension('spam',sources=['spammodule.c'])

setup(
    name='Covipedia',
    version = '1.0',

    py_modules=['mainGUI','Center','gmail_Send','Hosp','LiveCoronaInfoJson'],


    packages=['image','xml','telegram','text'],
    package_data={'image':['*.png'], 'xml':['*.xml'],'telegram':['noti.py','teller.py','LiveCoronaInfoJson.py'], 'text':['*.txt']},

    ext_modules=[module_spam]

)