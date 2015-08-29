<?php
function calculateValues ($a, $b)
{
    $c = $a +$b;
    return calculateMoreValues ($c, $a);
    
}

function calculateMoreValues ($a, $b)
{
    return $a - $b;
}

echo calculateValues(10,20);

?>
