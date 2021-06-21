<script>
function countCharactersCategory(s) {
 var totalSpecialCharacters = 0, totalDigits = 0, totalVowels = 0, totalConsonants = 0;
for (var i = 0; i < s.length; i++) {
 var c = s[i];
// Alphabets family
 if ( (c >= "a" && c <= "z") || (c >= "A" && c <= "Z") ) {
 // Converting character to lower case
 c = c.toLowerCase();
// Vowels
 if (c == "a" || c == "e" || c == "i" || c == "o" || c == "u") {
 totalVowels++;
 }
 // Consonants
 else {
 totalConsonants++;
 }
 }
 // Digits family
 else if (c >= "0" && c <= "9") {
 totalDigits++;
 }
 // Special characters family
 else {
 totalSpecialCharacters++;
 }
 }
 document.write("Total no. of vowels in the given string: " + totalVowels + "<br>");
 document.write("Total no. of consonants in the given string: " + totalConsonants + "<br>");
 document.write("Total no. of digits in the given string: " + totalDigits + "<br>");
 document.write("Total no. of special characters in the given string: " + totalSpecialCharacters + "<br>");
}
// Test case: 1
var s1 = "Welcome 2 #MUO";
document.write("Input string: " + s1 + "<br>");
countCharactersCategory(s1);
// Test case: 2
var s2 = "This Is @ InpuT String 2";
document.write("Input string: " + s2 + "<br>");
countCharactersCategory(s2);
</script>