let X_0 = 10000.0;;
let Y = 1000.0;;
let H = 1.01;;
let N = 120;;
let rec calcMoney (x0: float) (y: float) (h: float) (nMonth: int): float =
    match nMonth with
    | 0 -> x0
    | _ when (nMonth > 0) ->
        let previousValue = calcMoney (x0) (y) (h) (nMonth - 1)
        (previousValue * h) + y
    | _ -> 0

let main () =
    let resultMoney = calcMoney (X_0) (Y) (H) (N)

    printfn $"""
    Initial money: %.2f{X_0}
    Addition per month: %.2f{Y}
    Increase rate per month: %.2f{H}
    Investment time: %i{N} months
    Final value: %.2f{resultMoney} moneys
    """

main ()
