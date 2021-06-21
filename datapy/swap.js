<script>
// Function to swap two numbers
// using a temporary variable
function swapNums(num1, num2) {
// Printing numbers before swapping
 document.write("Before Swapping: <br>");
 document.write("num1: " + num1 + ", num2: " + num2 + "<br>");
// Swapping with the help of a
// temporary variable "temp"
 let temp = num1;
 num1 = num2;
 num2 = temp;
// Printing numbers after swapping
 document.write("After Swapping: <br>");
 document.write("num1: " + num1 + ", num2: " + num2 + "<br>");
}
// Driver Code
swapNums(80, 50);
</script>