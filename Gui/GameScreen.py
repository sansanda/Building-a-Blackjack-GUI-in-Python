import os
import tkinter as tk
from Logic.GameState import GameState
from Logic.Card import Card

assets_folder2 = os.getcwd() + "/assets"
print(os.getcwd())

class GameScreen(tk.Tk):


    def __init__(self):

        super().__init__()
        self.title("Blackjack")
        self.geometry("800x640")
        self.resizable(False, False)

        self.CARD_ORIGINAL_POSITION = 100
        self.CARD_WIDTH_OFFSET = 100

        self.PLAYER_CARD_HEIGHT = 300
        self.DEALER_CARD_HEIGHT = 100

        self.PLAYER_SCORE_TEXT_COORDS = (400, 450)
        self.WINNER_TEXT_COORDS = (400, 250)

        self.game_state = GameState()

        # The Canvas on which we will draw all of our graphics is created next.
        # We set the width and height of our game_screen to fixed values of 800 pixels and 500 pixels respectively.
        # This allows us to know the exact coordinates of where to place images (as defined earlier in our constants) and allows us to create a background
        # image which will always be the exact size of our Canvas.
        # We also know that since our application is 800 pixels by 640, we have 140 pixels left to function as the bottom part of our application.
        # This is where we will display our buttons for the user to interact with.
        #
        # In order to claim this space and make it usable, we will use a Frame widget:
        #     self.bottom_frame = tk.Frame(self, width=800, height=140, bg="red")
        #     self.bottom_frame.pack_propagate(0)
        # Our Frame widget also has a fixed width and height, as well as a background color specified by the bg argument.
        # Feel free to change this to suit your own preferences.
        #
        # Frame widgets behave differently to Canvas widgets when they have their sizes specified.
        # By default, a Frame widget will only be as big as it needs to be in order to hold all of its child widgets.
        # If we want to force the size when placing our Frame widget into its parent using the pack geometry manager, we need to call pack_propagate(0) on it.
        #
        # This forces the Frame to be the size specified by the keyword arguments of width and height.

        self.game_screen = tk.Canvas(self, bg="white", width=800, height=500)
        self.bottom_frame = tk.Frame(self, width=800, height=140, bg="red")
        self.bottom_frame.pack_propagate(0)

        # Now that we have a Frame to hold our Button widgets, let's add some Button widgets to our GameScreen class:
        # We define four buttons, which can go into our Frame.
        #
        # The hit_button and stick_button act as our main gameplay controls.
        # These will call the hit and stick methods which will be defined on this class, so we pass self.hit and self.stick to their command argument.
        #
        # For consistency, we want the buttons to all be the same size. We achieve this by passing in the width argument of 25.
        #
        # We also define two more buttons: play_again_button and quit_button.
        # At the end of the game, these buttons will display, allowing the user to decide whether or not they wish to play another game.
        # These will also call functions defined on this class, so we pass these to the command argument.


        self.hit_button = tk.Button(self.bottom_frame, text="Hit", width=25, command=self.hit)
        self.stick_button = tk.Button(self.bottom_frame, text="Stick", width=25, command=self.stick)

        self.play_again_button = tk.Button(self.bottom_frame, text="Play Again", width=25, command=self.play_again)
        self.quit_button = tk.Button(self.bottom_frame, text="Quit", width=25, command=self.destroy)

        # We only pack our hit_button and stick_button in the __init__ method since we do not need to show the other buttons until a game is over.
        #
        # We pack these over to the left so that they line up side by side.
        # We also add some padding to the hit_button, which will be over on the left-hand side, to space it away from the left edge of the screen,
        # and to put some spacing between itself and our stick_button.

        self.hit_button.pack(side=tk.LEFT, padx=(100, 200))
        self.stick_button.pack(side=tk.LEFT)

        # We now need to place our Frame and Canvas into our window to complete the layout:
        # We put our bottom frame at the bottom of the window by using side=tk.BOTTOM and stretch it horizontally by using fill=tk.X.
        #
        # We pack our game_screen to the left and use anchor=tk.N to ensure that this begins in the very top-left corner of the window.

        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.game_screen.pack(side=tk.LEFT, anchor=tk.N)

        # Now all we need to do is draw the graphical elements into our Canvas, and we will use a method named display_table to do so:
        self.display_table()

    # We allow for two arguments for this method.
    #
    # The first tells the game_screen whether or not to hide the dealer's first card. During the gameplay, ' \
    # the dealer's first card will need to be face down, but when the user chooses to stick with their hand, ' \
    # 'we will flip the dealer's card face up to reveal their score.
    #
    # We may also need to call the method with a pre-calculated table state. This also happens when the user decides to stick with their hand.
    #
    # By default, the dealer's first card will be hidden and we will not have a table_state.
    #
    # If a table state was not provided, then we need to ensure we get it.
    # We call the get_table_state method from our game_state instance to generate one.

    def display_table(self, hide_dealer=True, table_state=None):

        # Now that we definitely have our table state, we can display some card images.
        # We grab both the player's and dealer's cards from the table_state dictionary and use them within a list comprehension,
        # calling their get_file method to return the location of the relevant image file to our assets folder.
        #
        # If we are hiding the dealer's first card then we do not want to display its image. ' \
        # 'We instead replace the first element in our dealer_card_images list with the back file, which we obtain using ' \
        # 'the Card class's get_back_file method. This means the first card will appear to be face down to the player.

        if not table_state:
            table_state = self.game_state.get_table_state()

        player_card_images = [card.get_file() for card in
                              table_state['player_cards']]
        dealer_card_images = [card.get_file() for card in
                              table_state['dealer_cards']]

        if hide_dealer and not table_state['blackjack']:
            dealer_card_images[0] = Card.get_back_file()

        # Now that we have some image file locations, it's time to start drawing them onto the game_screen.
        # We begin by drawing the tabletop, which will function as our background.
        # Add the following code to our display_table method:

        # Between each draw of the screen, we will delete everything currently drawn onto our Canvas.
        # This ensures that we are only drawing what we need, and anything old will not be left over.
        # We do this using the Canvas widget's delete method and by passing the string all to instruct it to delete everything.
        # Now that we have a clean slate, we will begin by drawing the background.
        # We create a PhotoImage instance containing the tabletop.png image from our assets folder and keep a reference to it
        # as the self.tabletop_image attribute.
        #
        # The tabletop.png file can be any image which is 800 pixels wide and 500 pixels tall.
        # Our PhotoImage can now be drawn onto our game_screen. We do this using the create_image method in our Canvas.
        # The first argument to create_image is a 2-tuple of the coordinates for the center of the image. Since the image is the exact size of our Canvas,
        # we want to put the center of the image at the center of our Canvas.
        # We know they are both 800 by 500, so we pass (400, 250) as our coordinates.
        # The image to place onto the Canvas is passed to the image argument. We pass our PhotoImage instance as the value here.
        #
        # With that, we now have our background on our game_screen. The next thing we need to draw is the cards:

        self.game_screen.delete("all")
        self.tabletop_image = tk.PhotoImage(file=assets_folder2 + "/tabletop.png")

        self.game_screen.create_image((400, 250), image=self.tabletop_image)

        # To correctly position our player's cards, we need to know which card we are drawing—their first, second, third, and so on.
        # We use the enumerate function to loop over our list of player_card_images and also obtain the index each is at.
        #
        # Calculating the coordinates at which to place each card is done using our classes constants.
        #
        # Each card is initially placed at the X coordinate defined by our CARD_ORIGINAL_POSITION constant,
        # then subsequent cards will be placed a distance of 100 pixels (as defined by CARD_WIDTH_OFFSET) to the right of this.
        # We get these numbers by multiplying the list index of the card we are looking to place by the CARD_WIDTH_OFFSET constant and adding
        # the result to the CARD_ORIGINAL_POSITION value.
        #
        # The Y value of our card's coordinates is always going to be the same as the number we have stored in PLAYER_CARD_HEIGHT,
        # since that defines how close to the bottom of the game_screen to draw our cards, and we always want them to line up horizontally.
        #
        # We apply the same logic when placing the dealer's card images, except we use our DEALER_CARD_HEIGHT constant to set the Y coordinate.

        for card_number, card_image in enumerate(player_card_images):
            self.game_screen.create_image(
                (self.CARD_ORIGINAL_POSITION + self.CARD_WIDTH_OFFSET * card_number, self.PLAYER_CARD_HEIGHT),
                image=card_image
            )

        for card_number, card_image in enumerate(dealer_card_images):
            self.game_screen.create_image(
                (self.CARD_ORIGINAL_POSITION + self.CARD_WIDTH_OFFSET * card_number, self.DEALER_CARD_HEIGHT),
                image=card_image
            )

        # Now that the player can see their cards, we should show their score as well so that they do not have to tally their total in their head:
        # We use the create_text method from our Canvas widget to draw text onto our screen.
        #
        # The first argument to this method is once again the coordinates as a 2-tuple.
        # We have these defined as a constant, PLAYER_SCORE_TEXT_COORDS, so we use that as the first argument.
        #
        # The text argument controls what the text drawn to the screen actually says.
        # We have the score as a string available in our game_state instance, so we can call this method and use the result as the value passed.
        #
        # In order to change the font size, we can use the font argument.
        # The font argument takes a tuple. The first value in the tuple will be a string containing the font name, for example, Ariel.
        # Since we are providing None in this case, the system's default font will be used.
        # The second value defines the font's size. We pass in 20 to make the text bigger and thus more readable.

        self.game_screen.create_text(self.PLAYER_SCORE_TEXT_COORDS, text=self.game_state.player_score_as_text(), font=(None, 20))

        # With that added, all of the graphics which should always be drawn are accounted for.
        # However, if somebody wins, we should display a message portraying this:
        # We first check whether or not the table_state contains a winner. If it does not, then we won't want to display any more text.
        #
        # If we do have a winner, then we will once again use the create_text method to draw some text onto the screen,
        # letting the player know that the current game is now over.
        #
        # If our winner string is set to p, then the player has won and we will show YOU WIN!.
        #
        # If our winner string is dp, then we have a tie and we will show TIE!.
        #
        # Otherwise, the dealer must have won, so we show DEALER WINS!.
        #
        # The location of this text is stored in our WINNER_TEXT_COORDS constant, and so this is the first argument passed to our call to create_text.
        # These coordinates are again the middle point of the Canvas so that this text will be centered on the screen.
        #
        # We again use the font argument to increase the size of our default font. This time, we want it even bigger, so we set it to 50.

        if table_state['has_winner']:
            if table_state['has_winner'] == 'p':
                self.game_screen.create_text(self.WINNER_TEXT_COORDS,
                                             text="YOU WIN!", font=(None, 50))
            elif table_state['has_winner'] == 'dp':
                self.game_screen.create_text(self.WINNER_TEXT_COORDS, text="TIE!",
                                             font=(None, 50))
            else:
                self.game_screen.create_text(self.WINNER_TEXT_COORDS,
                                             text="DEALER WINS!", font=(None, 50))

            self.show_play_again_options()


    # As the game is now over, we no longer need to offer the hit_button or stick_button—we instead need to ask the player
    # if they would like to play another game. We handle the replacing of these buttons with a method called show_play_again_options.
    # Let's look at this now:

    #   In order to unpack the hit_button and stick_button, we call the pack_forget method on them.
    #   This does not delete them but simply removes them from being displayed by the parent widget.
    #
    #   To show our play_again_button and quit_button, we pack them with the same parameters as attributed to our hit_button and stick_button.
    #   This ensures that they will be put in the exact same place as the previous buttons.

    def show_play_again_options(self):
        self.hit_button.pack_forget()
        self.stick_button.pack_forget()

        self.play_again_button.pack(side=tk.LEFT, padx=(100, 200))
        self.quit_button.pack(side=tk.LEFT)

    # Since we are on the topic of our game's buttons, let's have a look at what each will do, starting with our hit_button:
    # This method simply calls the hit method over on our game_state instance which deals with the game logic side of the player receiving a card.
    # Once that has happened, the state of the table will have changed, so we need to draw it again. We call self.display_table to do this.

    def hit(self):
        self.game_state.hit()
        self.display_table()

    # If they instead click the stick_button, we will do the following:
    # Since clicking the stick_button ends any further game logic, we need to obtain the final table state from our game_state instance.
    # We can then pass this over to display_table in order to draw it on the screen.
    # We also pass False to the hide_dealer argument in order to show the player what the dealer had in their hand.
    #
    # Now that the game has ended, our other two buttons will be displayed.
    # The quit_button calls the built-in destroy method of the Tk widget in order to close the window.

    def stick(self):
        table_state = self.game_state.calculate_final_state()
        self.display_table(False, table_state)

    # Our play_again_button will reset the game_state so that a new game can begin:
    def play_again(self):
        self.show_gameplay_buttons()
        self.game_state = GameState()
        self.display_table()

    # When a new game begins, the user will need to see the hit and stick buttons again.
    # We do this by using a method called show_gameplay_buttons, which will be covered next.
    #
    # The game_state instance we store is replaced by a new one, meaning we have a new shuffled deck and two new hands, as well as no winner.

    # The show_gameplay_buttons method just does what our show_play_again_options method did but in reverse.
    # Instead of forgetting the hit and stick buttons, it forgets the quit and play again buttons and re-packs the hit and stick buttons
    # in their place.
    #
    # This is all that is needed in order to have our game function. Now we just need to piece it together.

    def show_gameplay_buttons(self):
        self.play_again_button.pack_forget()
        self.quit_button.pack_forget()

        self.hit_button.pack(side=tk.LEFT, padx=(100, 200))
        self.stick_button.pack(side=tk.LEFT)

# To make and display a window for our game, we just need an instance of our GameScreen.
# Since this inherits from the Tk widget, we will also need to call its mainloop method to make it show.
#
# We will do this within an if __name__ == "__main__" block to allow our classes from this file to be imported into another,
# in case someone wanted to write another card game using our Card and Deck classes, for example:

# Add the preceding code to the very bottom of your code file of this lesson and run the program.
# You should now have a fully working game of blackjack:
#
# blackjack.gif
# Hopefully, you will agree that this is much more enjoyable than the command-line version.
# Feel free to have a play around with any of the constants, colors, or image files in order to make the game more personal to you.

if __name__ == "__main__":
    gs = GameScreen()
    gs.mainloop()