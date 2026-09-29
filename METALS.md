# Gold & Silver Fair-Value Bot

*Updated Tue Sep 29, 8:04 AM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

🔴 **Losing.** Not beating Kalshi's prices after fees.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 84 | 82 | 27 (33%) | 40¢ | 48% | -$70.15 | -21% |
| Silver | 43 | 42 | 12 (29%) | 34¢ | 42% | -$30.63 | -20% |
| Gold | 41 | 40 | 15 (38%) | 46¢ | 54% | -$39.52 | -21% |

*Earlier half -$19.70 / later half -$50.45.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 85 | 28 (33%) | -$77.32 | -22% |
| 4¢+ ← live bot | 82 | 28 (34%) | -$32.39 | -10% |
| 6¢+ | 72 | 28 (39%) | $27.80 | +11% |
| 8¢+ | 60 | 25 (42%) | $50.76 | +25% |
| 10¢+ | 50 | 17 (34%) | $13.30 | +8% |
| 15¢+ | 26 | 9 (35%) | $22.43 | +33% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 2106 | -1.8% |
| Hyperliquid price vs Kalshi's target | 2106 | +1.9% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 8:01:24 AM | Gold | DOWN | 13.6 min | 19¢ | 25% | 5¢ | Open | — |
| 9/29 8:01:02 AM | Silver | DOWN | 13.9 min | 17¢ | 23% | 5¢ | Open | — |
| 9/29 7:46:04 AM | Silver | DOWN | 13.9 min | 37¢ | 43% | 4¢ | ❌ Lost | -$3.87 |
| 9/29 7:39:00 AM | Silver | UP | 6.0 min | 34¢ | 41% | 6¢ | ❌ Lost | -$3.56 |
| 9/29 7:31:22 AM | Gold | UP | 13.6 min | 71¢ | 77% | 4¢ | ❌ Lost | -$7.25 |
| 9/29 7:19:22 AM | Silver | DOWN | 10.6 min | 30¢ | 37% | 6¢ | ❌ Lost | -$3.15 |
| 9/29 7:16:02 AM | Gold | UP | 13.9 min | 39¢ | 46% | 6¢ | ❌ Lost | -$4.07 |
| 9/29 7:02:34 AM | Silver | DOWN | 12.4 min | 36¢ | 45% | 8¢ | ❌ Lost | -$3.77 |
| 9/29 6:46:04 AM | Gold | UP | 13.9 min | 26¢ | 32% | 5¢ | ❌ Lost | -$2.74 |
| 9/29 6:46:04 AM | Silver | UP | 13.9 min | 22¢ | 29% | 5¢ | ❌ Lost | -$2.33 |
| 9/29 6:32:30 AM | Gold | DOWN | 12.5 min | 36¢ | 46% | 8¢ | ❌ Lost | -$3.77 |
| 9/29 6:32:18 AM | Silver | UP | 12.7 min | 26¢ | 32% | 5¢ | ❌ Lost | -$2.74 |
