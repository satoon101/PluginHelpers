# Set the passed variables
BRANCHNAME=$1

# Validate the given branch name
if [ ! -f $SOURCEPYTHONDIR/src/makefiles/branch/$BRANCHNAME ]; then
    echo Invalid branch '$BRANCHNAME'.
    exit 1
fi

# Store the branch's repo directory
BRANCHDIR=$SOURCEPYTHONDIR/src/hl2sdk/$BRANCHNAME

Create the branch's repo if it doesn't exist
if [ ! -d $BRANCHDIR ]; then
    mkdir -p $BRANCHDIR
    git clone https://github.com/alliedmodders/hl2sdk.git $BRANCHDIR
fi

# Navigate to the branch's repo directory
cd $BRANCHDIR

# Force checkout to checkout the specified branch and remove previous patches
if ! git checkout -f $BRANCHNAME; then
    exit
fi

# Pull any new changes to the branch
if ! git pull; then
    exit
fi

# Store the patches directory for the branch
PATCHDIR=$SOURCEPYTHONDIR/src/patches/$BRANCHNAME

# Copy the patches to the branch
if [ -d $PATCHDIR ]; then
    cd $PATCHDIR
    cp -r * $BRANCHDIR
fi

# Navigate to the main src directory
cd $SOURCEPYTHONDIR/src

# Store the build directory for the branch
BUILDDIR=$SOURCEPYTHONDIR/src/Builds/$BRANCHNAME

# Create the build directory if it doesn't exist
if [ ! -d $BUILDDIR ]; then
    mkdir -p $BUILDDIR
fi

# Create the solution for the build
cmake . -B$BUILDDIR -DBRANCH=$BRANCH

# Build the binaries
cd $BUILDDIR
make clean
make
