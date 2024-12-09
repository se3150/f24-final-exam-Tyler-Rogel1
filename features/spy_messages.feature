Feature: encode or decode a secret message
As a secret spy
I should be able to encode and decode messages
So that I can chat with my spy friends like a pro.

Scenario: I can successfully encode a secret message
    Given I open the url "https://www.hanginghyena.com/solvers_a/caesar-cipher-decoder"
    # write your steps here
    When I set "test encode" to the inputfield "#letters"
    When I select the option with the value "1" for element "#shift-amount"
    When I click on the element "#submit"
    When I pause for 500ms
    Then I expect that element "#decoded_message" contains the text "uftu fodpef"
Scenario: I can successfully decode a secret message
    Given I open the url "https://www.hanginghyena.com/solvers_a/caesar-cipher-decoder"
    # write your steps here
    When I set "uftu efdpef" to the inputfield "#letters"
    When I select the option with the text "Decode" for element "#decoder-setting"
    When I select the option with the value "1" for element "#shift-amount"
    When I click on the element "#submit"
    When I pause for 500ms
    Then I expect that element "#decoded_message" contains the text "test decode"
