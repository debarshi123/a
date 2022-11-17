basic.forever(function () {
    if (input.compassHeading() < 45 && input.compassHeading() > 315) {
        basic.showArrow(ArrowNames.North)
    } else if (input.compassHeading() > 45 && input.compassHeading() < 135) {
        basic.showArrow(ArrowNames.East)
    } else if (input.compassHeading() > 135 && input.compassHeading() < 225) {
        basic.showArrow(ArrowNames.South)
    } else if (input.compassHeading() > 225 && input.compassHeading() < 315) {
        basic.showArrow(ArrowNames.West)
    } else {
        basic.showArrow(ArrowNames.North)
    }
})
