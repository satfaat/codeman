// JavScript implementation to reverse a string
// using recursion
function reverseString(str) {
    if (str === "") {
    return "";
    } else {
    return reverseString(str.substr(1)) + str.charAt(0);
    }
   }
   str1 = "MUO";
   str2 = "Welcome to MUO";
   str3 = "She sells seashells by the seashore";
   document.write("Input string: <br>");
   document.write(str1 + "<br>");
   document.write(str2 + "<br>");
   document.write(str3 + "<br>");
   str1 = reverseString(str1);
   str2 = reverseString(str2);
   str3 = reverseString(str3);
   document.write("Reversed string: <br>");
   document.write(str1 + "<br>");
   document.write(str2 + "<br>");
   document.write(str3 + "<br>");