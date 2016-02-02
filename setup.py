#!/usr/bin/env python3
#
# This python script is intended to setup a gitusr shell script.
# The gitusr shell script is made for managing multiple git hub accounts.
#
# More information can be found at: https://github.com/jeffrutledge/gitusr

import os
import stat

# Path to write shell script to
SCRIPT_PATH = "/usr/local/bin/gitusr"

#####################################################
############# Parts of the Script that do not change
#####################################################
SCRIPT_PART1 =\
"""#!/bin/sh
#
# The gitusr shell script is made for managing multiple git hub accounts.
# Type gitusr -h in the shell for a help message.
# This file may be reconfigure by rerunning the python setup script.
#
# More information can be found at: https://github.com/jeffrutledge/gitusr

while getopts ':gmph' flag; do
    case "$flag" in
      g) globalFlag=true ;;"""

##################################
# email flags
##################################

SCRIPT_PART2 ="""
      h) # Display Help text
          echo "gitusr | Check or Set Git Email"
          echo ""
          echo "Usage: gitusr [options]                 Display git email"
          echo "   or: gitusr [options] [email]         Set git email"
          echo ""
          echo "options:"
          echo "  -h                                    Display this help message"
          echo "  -g                                    Set global email"
          echo "                                          (Otherwise set email of current repository)"
          echo ""
          echo "email:" """

##################################
# help message flag descriptions
##################################

SCRIPT_PART3 ="""
          echo ""
          echo "More information can be found at: https://github.com/jeffrutledge/gitusr"
          exit ;;
      \?) error "Unexpected option $flag" ;;
    esac
  done

  if [ "$globalFlag" = true ] ; then
    git config --global user.email $email
  else
    git config user.email $email
  fi"""
#####################################################
############# End Script Strings
#####################################################

def setup():
  """
  Sets up the gitusr shell script

  Configures the users emails and corresponding flags.
  Then writes the shell script to FOLDER_PATH
  """
  emailFlagTuples = requestSetupConfiguration()

  scriptText = generateScriptText(emailFlagTuples)

  writeExecutableScript(scriptText)

def requestSetupConfiguration():
  """
  Requests user input for flags and emails,
  then returns them as a list of tuples.
  """
  print(\
          '                          gitusr Setup\n'\
        + '----------------------------------------------------------------------\n'
        + 'You will choose which emails you would like to be able to switch to.\n'\
        + 'Each email will have a one letter character flag.\n'\
        + '\n'\
        + 'For example, your work gitHub email might use w.\n'\
        + 'Then you could switch to this email with the command $ gitusr -w\n'\
        + '\n'\
        + 'If you ever forget your flags use -h for a help message.\n'\
        + 'To change your emails, simply run this script again.\n'
        + '----------------------------------------------------------------------')

  emailInput = ''       # Temporarily stores user input for an email
  flagInput = ''        # Temporarily stores user input for a flag
  emailFlagTuples = []  # Stores all Email and flag pairs, is returned

  # Ask for email and flag pairs until user inputs 'done' as an email 
  while True:
    emailInput = requestEmail()

    if emailInput == 'done':
      break

    flagInput = requestFlag(emailInput)
    emailFlagTuples.append((emailInput, flagInput))

  return emailFlagTuples

def requestEmail():
  """
  Request an email input.
  """
  printBreak()
  emailInput = input('Input an email you would like to use (or input done if you are done):\n')
  return emailInput

def requestFlag(emailForFlag):
  """
  Request a flag input.
  """
  printBreak()
  flagInput = input('Input the flag you would like to use for [{}]:'.format(emailForFlag)\
                    +'\n (the flag must be one alpha character '\
                    +'which is not h, g or already used)\n')

  # Make sure the flag is valid
  # one alpha character
  # not used already, or h or g
  while not isValidFlag(flagInput):
    printBreak()
    print('That was not a valid flag. \n'\
          +'A valid flag must be one alpha character that is not h or g,\n'\
          +'or not already be used.\n')
    flagInput = input('Input the flag you would like to use for [{}]:\n'.format(emailForFlag))

  return flagInput

def isValidFlag(flag, usedFlags = ['h', 'g']):
  """
  Takes a string and checks to make sure it is a valid flag.
  A valid flag is one alpha character and is not used already.
  If flag is valid adds it to used flags list.
  By defualt h and g are used flags.
  """
  if flag.isalpha and len(flag) == 1 and flag not in usedFlags:
    usedFlags.append(flag) # Add flag to used flags
    return True
  return False

def printBreak():
  """
  Prints a break to help the user read input requests.
  """
  print('\n\n----------------------------------------------------------------------\n\n')

def generateScriptText(emailFlagTuples):
  """
  Generates the final bash script text,
  using the given emails and flags.
  """
  getoptsFlagsString = 
  emailFlagString = generateEmailFlags(emailFlagTuples)
  helpMessageString = generateHelpMessage(emailFlagTuples)

  #Assemble the full script string
  scriptString = SCRIPT_PART1
  scriptString += emailFlagString
  scriptString += SCRIPT_PART2
  scriptString += helpMessageString
  scriptString += SCRIPT_PART3

  return scriptString

def generate

def generateEmailFlags(emailFlagTuples):
  """
  Takes emailFlagTuples and generates the part of the
  script case statement which accepts email flags.
  """
  emailFlagString = ""

  for emailFlagTuple in emailFlagTuples:
    #add a new line and indent
    emailFlagString += "\n      "
    #add flag character
    emailFlagString += emailFlagTuple[1]
    #close case condition and setup email variable
    emailFlagString += r''') email="\"'''
    #input email address
    emailFlagString += emailFlagTuple[0]
    #end case statement
    emailFlagString += r'''\"" ;;'''

  return emailFlagString

def generateHelpMessage(emailFlagTuples):
  """
  Takes emailFlagTuples and generates the part of the
  script that echos the help message.
  """
  helpMessageString = ""

  for emailFlagTuple in emailFlagTuples:
    #add a new line and indent
    helpMessageString += '''\n          echo "  -'''
    #add flag
    helpMessageString += emailFlagTuple[1]
    #add spacing
    helpMessageString += "                                    Set email to: "
    #add email
    helpMessageString += emailFlagTuple[0]
    #close echo quotes
    helpMessageString += '''"'''

  return helpMessageString

def writeExecutableScript(scriptText):
  """
  Writes and makes executable a script from the given string.
  Writes to SCRIPT_PATH.
  """
  scriptFile = open(SCRIPT_PATH, 'w')
  scriptFile.write(scriptText)

  # Make the script executable
  st = os.stat(SCRIPT_PATH)
  os.chmod(SCRIPT_PATH, st.st_mode | stat.S_IEXEC)

#call setup() on file open
if __name__ == '__main__':
  setup()