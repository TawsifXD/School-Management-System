 // values to keep track of the number of letters typed, which quote to use. etc. Don't change these values.
 var i = 0,
     a = 0,
     isBackspacing = false,
     isParagraph = false;

 // Typerwrite text content. Use a pipe to indicate the start of the second line "|".  
 var textArray = [
     "What do you call an alligator wearing a vest?|An Investigator",
     "What do you call a fake noodle?|An Impasta",
     "Why shouldn't you write with a broken pencil?|Because it's pointless",
     "Why couldn't the pirate finish the alphabet?|He kept getting lost a C",
     "What's brown and sticky?|A stick",
     "What starts with an E, ends with an E and has one letter in it?|An Envelope",
     "What has four wheels, and flies?|A Garbage truck",
     "What do you call a pig that knows Karate?|Pork Chop",
     "Why did the scarecrow get promoted?|He was out standing in his field.",
     "I have a step ladder|I never knew my real ladder.",
     "What kind of shoes do ninjas wear?|Sneakers"
 ];

 // Speed (in milliseconds) of typing.
 var speedForward = 100, //Typing Speed
     speedWait = 1000, // Wait between typing and backspacing
     speedBetweenLines = 1000, //Wait between first and second lines
     speedBackspace = 25; //Backspace Speed

 //Run the loop
 typeWriter("output", textArray);

 function typeWriter(id, ar) {
     var element = $("#" + id),
         aString = ar[a],
         eHeader = element.children("h1"), //Header element
         eParagraph = element.children("p"); //Subheader element

     // Determine if animation should be typing or backspacing
     if (!isBackspacing) {

         // If full string hasn't yet been typed out, continue typing
         if (i < aString.length) {

             // If character about to be typed is a pipe, switch to second line and continue.
             if (aString.charAt(i) == "|") {
                 isParagraph = true;
                 eHeader.removeClass("cursor");
                 eParagraph.addClass("cursor");
                 i++;
                 setTimeout(function() {
                     typeWriter(id, ar);
                 }, speedBetweenLines);

                 // If character isn't a pipe, continue typing.
             } else {
                 // Type header or subheader depending on whether pipe has been detected
                 if (!isParagraph) {
                     eHeader.text(eHeader.text() + aString.charAt(i));
                 } else {
                     eParagraph.text(eParagraph.text() + aString.charAt(i));
                 }
                 i++;
                 setTimeout(function() {
                     typeWriter(id, ar);
                 }, speedForward);
             }

             // If full string has been typed, switch to backspace mode.
         } else if (i == aString.length) {

             isBackspacing = true;
             setTimeout(function() {
                 typeWriter(id, ar);
             }, speedWait);

         }

         // If backspacing is enabled
     } else {

         // If either the header or the paragraph still has text, continue backspacing
         if (eHeader.text().length > 0 || eParagraph.text().length > 0) {

             // If paragraph still has text, continue erasing, otherwise switch to the header.
             if (eParagraph.text().length > 0) {
                 eParagraph.text(eParagraph.text().substring(0, eParagraph.text().length - 1));
             } else if (eHeader.text().length > 0) {
                 eParagraph.removeClass("cursor");
                 eHeader.addClass("cursor");
                 eHeader.text(eHeader.text().substring(0, eHeader.text().length - 1));
             }
             setTimeout(function() {
                 typeWriter(id, ar);
             }, speedBackspace);

             // If neither head or paragraph still has text, switch to next quote in array and start typing.
         } else {

             isBackspacing = false;
             i = 0;
             isParagraph = false;
             a = (a + 1) % ar.length; //Moves to next position in array, always looping back to 0
             setTimeout(function() {
                 typeWriter(id, ar);
             }, 50);

         }
     }
 }