def on_forever():
    if input.compass_heading() < 45 and input.compass_heading() > 315:
        basic.show_arrow(ArrowNames.NORTH)
    else:
        if input.compass_heading() > 45 and input.compass_heading() < 135:
            basic.show_arrow(ArrowNames.EAST)
        else:
            if input.compass_heading() > 135 and input.compass_heading() < 225:
                basic.show_arrow(ArrowNames.SOUTH)
            else:
                if input.compass_heading() > 225 and input.compass_heading() < 315:
                    basic.show_arrow(ArrowNames.WEST)
                else:
                    basic.show_arrow(ArrowNames.NORTH)
basic.forever(on_forever)
