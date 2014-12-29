# Is the operating system Windows?
if [ "$OSTYPE" == "msys" ]; then
    DIRECTORY='windows'

# Is the operating system Linux?
else
    DIRECTORY='linux'
fi

echo $DIRECTORY
