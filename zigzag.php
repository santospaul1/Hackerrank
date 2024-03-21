<?php
$_fp = fopen("php://stdin", "r");
/* Enter your code here. Read input from STDIN. Print output to STDOUT */
function findZigZagSequence($a, $n) {
    // Sort the array in ascending order
    sort($a);

    // Swap the middle element with the last element for base case
    $mid = floor(($n - 1) / 2);
    $temp = $a[$mid];
    $a[$mid] = $a[$n - 1];
    $a[$n - 1] = $temp;

    // Create two pointers for zig-zagging
    $st = $mid + 1;
    $ed = $n - 2;

    // Iterate while pointers haven't crossed each other
    while ($st <= $ed) {
        // Swap elements at st and ed for zig-zag pattern
        $temp = $a[$st];
        $a[$st] = $a[$ed];
        $a[$ed] = $temp;
        $st++;
        $ed--;
    }

    // Print the zig-zag sequence
    foreach ($a as $num) {
        echo $num . " ";
    }
    echo "\n"; // Add a newline after each test case
}

$test_cases = readline("Enter the number of test cases: ");
for ($cs = 0; $cs < $test_cases; $cs++) {
    $n = readline("Enter the number of array elements: ");
    $input = readline("Enter the array elements separated by space: ");
    $a = explode(" ", $input);
    findZigZagSequence($a, $n);
}

?>