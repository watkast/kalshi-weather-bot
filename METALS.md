# Gold & Silver Fair-Value Bot

*Updated Tue Sep 29, 8:24 AM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

🔴 **Losing.** Not beating Kalshi's prices after fees.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 86 | 84 | 27 (32%) | 39¢ | 47% | -$73.96 | -22% |
| Silver | 44 | 43 | 12 (28%) | 34¢ | 42% | -$32.43 | -21% |
| Gold | 42 | 41 | 15 (37%) | 45¢ | 53% | -$41.53 | -22% |

*Earlier half -$22.65 / later half -$51.31.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 87 | 28 (32%) | -$81.14 | -22% |
| 4¢+ ← live bot | 84 | 28 (33%) | -$36.10 | -11% |
| 6¢+ | 73 | 28 (38%) | $26.42 | +10% |
| 8¢+ | 60 | 25 (42%) | $50.76 | +25% |
| 10¢+ | 50 | 17 (34%) | $13.30 | +8% |
| 15¢+ | 26 | 9 (35%) | $22.43 | +33% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 2156 | -2.0% |
| Hyperliquid price vs Kalshi's target | 2156 | +1.9% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 8:18:54 AM | Silver | DOWN | 11.1 min | 38¢ | 44% | 4¢ | Open | — |
| 9/29 8:16:12 AM | Gold | DOWN | 13.8 min | 46¢ | 52% | 4¢ | Open | — |
| 9/29 8:01:24 AM | Gold | DOWN | 13.6 min | 19¢ | 25% | 5¢ | ❌ Lost | -$2.01 |
| 9/29 8:01:02 AM | Silver | DOWN | 13.9 min | 17¢ | 23% | 5¢ | ❌ Lost | -$1.80 |
| 9/29 7:46:04 AM | Silver | DOWN | 13.9 min | 37¢ | 43% | 4¢ | ❌ Lost | -$3.87 |
| 9/29 7:39:00 AM | Silver | UP | 6.0 min | 34¢ | 41% | 6¢ | ❌ Lost | -$3.56 |
| 9/29 7:31:22 AM | Gold | UP | 13.6 min | 71¢ | 77% | 4¢ | ❌ Lost | -$7.25 |
| 9/29 7:19:22 AM | Silver | DOWN | 10.6 min | 30¢ | 37% | 6¢ | ❌ Lost | -$3.15 |
| 9/29 7:16:02 AM | Gold | UP | 13.9 min | 39¢ | 46% | 6¢ | ❌ Lost | -$4.07 |
| 9/29 7:02:34 AM | Silver | DOWN | 12.4 min | 36¢ | 45% | 8¢ | ❌ Lost | -$3.77 |
| 9/29 6:46:04 AM | Gold | UP | 13.9 min | 26¢ | 32% | 5¢ | ❌ Lost | -$2.74 |
| 9/29 6:46:04 AM | Silver | UP | 13.9 min | 22¢ | 29% | 5¢ | ❌ Lost | -$2.33 |
