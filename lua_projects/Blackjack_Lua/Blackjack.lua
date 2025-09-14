--[[ By Honkyrot
Rules:
Single-player only
Dealer must hit on 16 or less
Dealer must stand on 17 or more
There are soft aces and hard aces.
Soft aces are aces that can be 1 or 11.
There is no splitting or doubling down.
Alternating turns between player and dealer for fair game.

Lua version of Blackjack
This is my best attempt at it.
Always remember, Lua arrays start at 1, not 0.

OOP version with classes i guess.
]]--

Blackjack = {}

function Blackjack:start_game()
    local game = {}
    setmetatable(game, self)
    self.__index = self
    self.current_deck = {}
    self.player_hand = {}
    self.dealer_hand = {}
    self.player_score = 0
    self.dealer_score = 0
    self.game_end = false
    return game
end

function Blackjack:create_deck() -- creates the deck with 52 cards
    local short_general_deck = {"Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"}
    for _ = 1,4 do
        for _, card in ipairs(short_general_deck) do
            table.insert(self.current_deck, card)
        end
    end
end

function Blackjack:shuffle_deck() -- Fisher-Yates shuffle
    for i = 1, #self.current_deck do
        local e = math.random(1, #self.current_deck)
        self.current_deck[i], self.current_deck[e] = self.current_deck[e], self.current_deck[i]
    end
end

function Blackjack:deal_card(player, output) -- deals 1 card from the deck
    is_player = false
    if player == "player" then
        player = self.player_hand
        is_player = true
    elseif player == "dealer" then
        player = self.dealer_hand
    else
        error("Invalid player")
    end

    local card = table.remove(self.current_deck, 1)
--    print("Dealt " .. card)--debug
    table.insert(player, card)
    if is_player and output then
        print("You were dealt a " .. card)
        print()  --Blank prints for new lines
    end
    return card
end

function table.clone(org)  --quick way to clone a table
    return {table.unpack(org)}
end

function Blackjack:read_cards(player)  --Print out the cards in the player's hand
    if player == "player" then
        player = self.player_hand
        print("Your hand:")
        for _, card in ipairs(player) do
            print(card)
        end
    elseif player == "dealer" then --Dealer has their first card hidden
        temp_hand = table.clone(self.dealer_hand)
        print("Dealer's hand is currently showing:")
        table.remove(temp_hand, 1)
        for _, card in ipairs(temp_hand) do
            print(card)
        end
    else
        error("Invalid player")
    end
end

function Blackjack:calculate_score(player) -- calculates the score of the player's hand
    if player == "player" then
        player = self.player_hand
    elseif player == "dealer" then
        player = self.dealer_hand
    else
        error("Invalid player")
    end

    local score = 0
    local ace_count = 0
    for _, card in ipairs(player) do -- count the aces first and then add the rest
        if card == "Ace" then
            ace_count = ace_count + 1
        elseif card == "Jack" or card == "Queen" or card == "King" then
            score = score + 10
        else
            score = score + tonumber(card)
        end
    end

    if ace_count > 0 then -- if there are aces in the hand
        for _ = 1, ace_count do
            if score + 11 > 21 then
                score = score + 1
            else
                score = score + 11
            end
        end
    end

    return score
end

function Blackjack:set_scores() -- sets the scores of the player and dealer
    self.player_score = self:calculate_score("player")
    self.dealer_score = self:calculate_score("dealer")
end

function Blackjack:win_check() -- checks if the player or dealer has won
    self:set_scores()
    if self.player_score > 21 then
        print("You busted!")
        return "lost"
    elseif self.dealer_score > 21 then
        print("Dealer busted!")
        return "win"
    elseif self.player_score == 21 and self.dealer_score == 21 then
        print("Draw! Both you and the dealer have 21!")
        return "draw"
    elseif self.player_score == 21 then
        print("You got Blackjack!")
        return "win"
    elseif self.dealer_score == 21 then
        print("Dealer got Blackjack!")
        return "lost"
    elseif self.game_end and self.dealer_score > self.player_score then
        print("Dealer wins "..self.dealer_score.." to "..self.player_score)
        return "lost"
    elseif self.game_end and self.dealer_score < self.player_score then
        print("Player wins "..self.player_score.." to "..self.dealer_score)
        return "lost"
    else
        return nil
    end
end

function Blackjack:dealer_turn() -- does the AI for the dealer
    if self.dealer_score < 17 then
        local new_card = self:deal_card("dealer")
        self:set_scores()
        print("Dealer drew a card: "..new_card)
    else
        print("Dealer stands.")
        print("Checking scores...")
        self.game_end = true
    end
end

function get_user_input_as_y_or_n(message) -- gets user input to turn into true false
    while true do
        print(message)
        io.write()
        local input = io.read()
        input = string.lower(input)
        if input == "y" or input == "yes" then
            return true
        elseif input == "n" or input == "no" then
            return false
        else
            print("Invalid input. Please enter yes or no (or y/n).")
        end
    end
end

function player_action()
    while true do
        print("What would you like to do?", "Your total: "..game.player_score)
        print("[1] Hit")
        print("[2] Stand")
        io.write()
        local input = io.read()
        if input == "1" then
            return "hit"
        elseif input == "2" then
            return "stand"
        else
            print("Invalid input. Please enter 1 or 2.")
        end
    end
end

function static_win_end_check()  --display end game message, stats, and asks to restart game
    print()
    print("Your hand: ["..game.player_score.."]")
    for _, card in ipairs(game.player_hand) do
        print(card)
    end
    print()
    print("Dealer's hand: ["..game.dealer_score.."]")
    for _, card in ipairs(game.dealer_hand) do
        print(card)
    end
    print()
    try_again = get_user_input_as_y_or_n("Do you want to play again? (y/n)")
    if not try_again then
        return false
    else
        return true
    end
end

user_start = get_user_input_as_y_or_n("Do you want to play a game of Blackjack? (y/n)")
if user_start then
    print("Welcome to blackjack!")
    local active = true
    local games_played = 0
    while active do
        print()
        games_played = games_played + 1
        print("Game "..games_played)
        game = Blackjack:start_game()
        game:create_deck()
        game:shuffle_deck()
        for _ = 1,2 do
            game:deal_card("player")
            game:deal_card("dealer")
        end
        startup_win_check = game:win_check()
        if startup_win_check then  --checks win conditions at the start of the game
            active = static_win_end_check()
        end
        print()
        game:read_cards("player")
        print()
        game:read_cards("dealer")
        while true do
            print()
            player_input = player_action()
            if player_input == "hit" then
                game:deal_card("player", true)
                game:read_cards("player")
                print()
                game:read_cards("dealer")
                print()
                win_check = game:win_check()
                if win_check then
                    active = static_win_end_check()
                    break
                end
            elseif player_input == "stand" then
                print()
                print("You stand.")
                print("Dealer's turn...")
                print()
                game:dealer_turn()
                win_check = game:win_check()
                if win_check or game.game_end then
                    active = static_win_end_check()
                    break
                end
                game:read_cards("player")
                print()
                game:read_cards("dealer")
            end
        end
    end
end
