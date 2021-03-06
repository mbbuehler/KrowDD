<?php

global $S;
global $S_LAYPERSON;
global $S_EXPERT;
global $S_DOMAIN;

$S_EXPERT = array(
    // upwork
    'DATASET' => 'Student',
    'TITLE' => 'Rank Features',
    'HEADER' => 'Rank Features',
    'TASK_DESCRIPTION' => 'Task Description',
    'LABEL_NAME' => 'E-Mail',
    'THANKS' => 'Thank you for your work',
    'TASK_AFTER_SUBMIT' => 'Please go ahead with the next task or fill the form if you have already solved the three given tasks. Make sure to keep the token.',
    'RANKHERE' => 'Ranking',
    'LABEL_COMMENT' => 'Comment',
    'RESET' => 'Reset',
    'FINISHED' => 'Finished',
    
);

$S_LAYPERSON = array(
    // AMT
    'DATASET' => 'Student',
    'TITLE' => 'Rank Aspects According to Relevance',
    'HEADER' => 'Ranking Aspects',
    'TASK_DESCRIPTION' => 'Task Description',
//    'LABEL_NAME' => 'Identifier', // Change again for AMT
    'LABEL_NAME' => 'Name',
    'THANKS' => 'Thank you for your work',
    'TASK_AFTER_SUBMIT' => 'Please copy the complete token bellow and submit it on Amazon Mechanical Turk in order to finish this HIT.',
    'RANKHERE' => 'Ranking',
    'LABEL_COMMENT' => 'Comment',
    'RESET' => 'Reset',
    'FINISHED' => 'Finished',
    'ONMOBILE' => 'You seem to be accessing this page via a mobile or a tablet browser. You might not be able to complete the ranking task on this device. If so, please use a desktop browser. Thank you.',
    'FORMINVALID' => 'Form invalid. Did you enter your name?',
);

$S_DOMAIN = array(
    // AMT
    'DATASET' => 'Student',
    'TITLE' => 'Aspekte nach Relevanz sortieren',
    'HEADER' => 'Aspekte sortieren',
    'TASK_DESCRIPTION' => 'Aufgaben-Beschreibung',
    'LABEL_NAME' => 'Name',
    'THANKS' => 'Vielen Dank für deinen Einsatz',
    'TASK_AFTER_SUBMIT' => 'Dein Ranking wurde gespeichert.',
    'RANKHERE' => 'Hier sortieren (ziehe die Felder über Klick auf das Kreuz nach links)',
    'LABEL_COMMENT' => 'Dein Bezug zum Thema / Kommentar',
    'RESET' => 'Zurücksetzen',
    'FINISHED' => 'Fertig',
    'ONMOBILE' => 'Du scheinst einen mobilen Browser zu benutzen. Unter Umständen funktioniert das Ranking mit diesem Gerät nicht. Bitte benutze in diesem Fall einen Desktop-Browser. Vielen Dank für dein Verständnis.',    'ONMOBILE' => 'Du scheinst einen mobilen Browser zu benutzen. Unter Umständen funktioniert das Ranking mit diesem Gerät nicht. Bitte benutze in diesem Fall einen Desktop-Browser. Vielen Dank für dein Verständnis.',
    'FORMINVALID' => 'Formular ungültig. Hast du deinen Namen eingetragen?',
);



function get_S($condition){
    switch ($condition){
        case 1:
            $S = $GLOBALS['S_LAYPERSON'];
            break;
        case 2:
            $S = $GLOBALS['S_DOMAIN'];
            break;
        case 3:
            $S = $GLOBALS['S_EXPERT'];
            break;
        default:
            $S = $GLOBALS['S_LAYPERSON'];
            break;
    }
    return $S;
}

$S = $S_LAYPERSON;

