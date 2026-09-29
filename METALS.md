# Gold & Silver Fair-Value Bot

*Updated Tue Sep 29, 4:02 PM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

🔴 **Losing.** Not beating Kalshi's prices after fees.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 131 | 129 | 44 (34%) | 38¢ | 46% | -$73.17 | -14% |
| Silver | 66 | 65 | 20 (31%) | 33¢ | 41% | -$22.28 | -10% |
| Gold | 65 | 64 | 24 (38%) | 44¢ | 52% | -$50.89 | -17% |

*Earlier half -$28.74 / later half -$44.43.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 132 | 44 (33%) | -$102.89 | -19% |
| 4¢+ ← live bot | 129 | 46 (36%) | -$19.49 | -4% |
| 6¢+ | 117 | 49 (42%) | $88.73 | +22% |
| 8¢+ | 104 | 42 (40%) | $93.94 | +29% |
| 10¢+ | 90 | 33 (37%) | $58.71 | +22% |
| 15¢+ | 56 | 20 (36%) | $52.81 | +36% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 3296 | -4.7% |
| Hyperliquid price vs Kalshi's target | 3296 | +1.7% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 4:01:03 PM | Gold | UP | 13.9 min | 67¢ | 89% | 21¢ | Open | — |
| 9/29 4:01:03 PM | Silver | UP | 13.9 min | 33¢ | 70% | 35¢ | Open | — |
| 9/29 3:48:49 PM | Silver | DOWN | 11.2 min | 15¢ | 20% | 4¢ | ❌ Lost | -$1.59 |
| 9/29 3:46:33 PM | Gold | DOWN | 13.4 min | 28¢ | 36% | 6¢ | ❌ Lost | -$2.95 |
| 9/29 3:31:30 PM | Gold | UP | 13.5 min | 49¢ | 56% | 5¢ | ❌ Lost | -$5.08 |
| 9/29 3:31:18 PM | Silver | DOWN | 13.7 min | 27¢ | 35% | 7¢ | ❌ Lost | -$2.84 |
| 9/29 3:23:32 PM | Silver | UP | 6.5 min | 22¢ | 37% | 14¢ | ❌ Lost | -$2.33 |
| 9/29 3:16:35 PM | Gold | DOWN | 13.4 min | 47¢ | 53% | 4¢ | ✅ Won | $5.12 |
| 9/29 3:02:32 PM | Gold | DOWN | 12.5 min | 41¢ | 52% | 9¢ | ✅ Won | $5.73 |
| 9/29 3:01:02 PM | Silver | DOWN | 13.9 min | 14¢ | 49% | 34¢ | ❌ Lost | -$1.49 |
| 9/29 2:46:28 PM | Silver | UP | 13.5 min | 30¢ | 37% | 5¢ | ❌ Lost | -$3.15 |
| 9/29 2:46:03 PM | Gold | UP | 13.9 min | 32¢ | 52% | 18¢ | ❌ Lost | -$3.36 |
