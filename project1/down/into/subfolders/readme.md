
At first i struggled to find a way to play the sounds in a random way, but then i found a way to do it through the following line of code  :
int which = int(random(4));
    when[which] = 8 * int(random(8)); 
This expression allowed me to have 8 possible values within the number 0 and 63.


Also i had issues with importing files sounds, although they were in  the extension required .wav .  But some of the sounds were too heavy and and error message popped up stating that the classification of the sound format not supported. so i reduced the size of the files and replaced them in the sketch folder.


At first I gave the sounds random names, but i figued later that i need to give them an ascending order in order for the code to be correct. so i reclassified them from (1 to 10)

AudioSample s1;
AudioSample s2;
AudioSample s3; 
AudioSample s4;
AudioSample s5;
AudioSample s6;
AudioSample s7; 
AudioSample s8;
AudioSample s9;
AudioSample s10;

But mostly tutorials have helped me to find a solution to every probelm i have found.  
