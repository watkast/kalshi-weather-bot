# Gold & Silver Fair-Value Bot

*Updated Mon Sep 28, 7:19 PM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

⏳ **Too early.** 0 of 30 settled trades needed before judging.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 2 | 0 | — | — | — | — | — |
| Silver | 1 | 0 | — | — | — | — | — |
| Gold | 1 | 0 | — | — | — | — | — |

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 0 | — | — | — |
| 4¢+ | 0 | — | — | — |
| 6¢+ | 0 | — | — | — |
| 8¢+ | 0 | — | — | — |
| 10¢+ | 0 | — | — | — |
| 15¢+ | 0 | — | — | — |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 0 | — |
| Hyperliquid price vs Kalshi's target | 0 | — |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 7:17:04 PM | Gold | UP | 12.9 min | 45¢ | 54% | 7¢ | Open | — |
| 9/28 7:17:00 PM | Silver | UP | 13.0 min | 29¢ | 41% | 11¢ | Open | — |
