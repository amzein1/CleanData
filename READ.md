#### The main python main3 will be reading files, manipulating the data, and storing the clean files back to a different file. During this process you must check for and catch errors.

#### Provided is a CVS file with a comma delimited file called DirtyNames.csv this file consists of thousands of names that are horribly formatted and must be cleaned up. A clean name is all lower case letters except the first letter which must be capitalized. In addition, some of the names have symbols or other invalid characters, if a name contains an invalid character it should be put in a separate file called InvalidNames.csv. Clean names should be put in CleanNames.csv.

#### A dirty name will consist of a name with randomly placed upper and lowercase letters. For example: joRdaN

#### A clean name should be formatted with and uppercase first letter followed by lowercase letters. However, if a name is hyphenated the name after the hyphen should also start with an upper case letter. For example: Jordan & Pitt-Rivers

#### Invalid names are entries in the list that are not names at all or names that contain invalid symbols. For the purpose of this task a name should be considered valid if it only contains letters a-z, A-Z, or a hyphen. Any other symbols (including spaces and numbers) should put the name in the invalid name list. Examples of invalid names: 123-123-1234, J@ke and John Doe

#### Two python files main.py and aux_module.py should be in the same folder.  
