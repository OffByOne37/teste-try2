for Index in range(26):
    screenMagic.plot_at(Index)
    basic.pause(1000)

def on_forever():
    pass
basic.forever(on_forever)
