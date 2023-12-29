# LetterShifter
Small script to shift the letters of all words in the Spanish dictionary looking for other words that exist in that dictionaty.

# How to Run
1. Build the image:

```
docker build -t letter-shifter .
``` 

2. Run the image
 a) Using Docker Desktop
 or
 b) Using the following command:
 `docker build -t letter-shifter .`

3. Check the output files in Docker Desktop
 Go to `Containers`
 Select the name of the container of this image
 Go to the `Files` tab
 Navigate to `usr/src/app/outputs`