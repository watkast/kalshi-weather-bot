# Gold & Silver Fair-Value Bot

*Updated Tue Sep 29, 6:33 AM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

🔴 **Losing.** Not beating Kalshi's prices after fees.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 74 | 72 | 27 (38%) | 40¢ | 48% | -$32.90 | -11% |
| Silver | 37 | 36 | 12 (33%) | 35¢ | 43% | -$11.21 | -9% |
| Gold | 37 | 36 | 15 (42%) | 46¢ | 54% | -$21.69 | -13% |

*Earlier half -$15.29 / later half -$17.61.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 73 | 25 (34%) | -$57.43 | -19% |
| 4¢+ ← live bot | 70 | 25 (36%) | -$15.52 | -6% |
| 6¢+ | 62 | 26 (42%) | $41.05 | +19% |
| 8¢+ | 55 | 22 (40%) | $39.84 | +22% |
| 10¢+ | 45 | 15 (33%) | $12.98 | +9% |
| 15¢+ | 26 | 9 (35%) | $22.43 | +33% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 1806 | -1.0% |
| Hyperliquid price vs Kalshi's target | 1806 | +4.9% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 6:32:30 AM | Gold | DOWN | 12.5 min | 36¢ | 46% | 8¢ | Open | — |
| 9/29 6:32:18 AM | Silver | UP | 12.7 min | 26¢ | 32% | 5¢ | Open | — |
| 9/29 6:19:10 AM | Gold | UP | 10.8 min | 51¢ | 58% | 5¢ | ✅ Won | $4.72 |
| 9/29 6:16:56 AM | Silver | DOWN | 13.1 min | 29¢ | 36% | 6¢ | ❌ Lost | -$3.05 |
| 9/29 6:05:26 AM | Silver | DOWN | 9.6 min | 26¢ | 33% | 5¢ | ✅ Won | $7.26 |
| 9/29 6:03:11 AM | Gold | UP | 11.8 min | 63¢ | 70% | 6¢ | ❌ Lost | -$6.47 |
| 9/29 5:48:47 AM | Gold | DOWN | 11.2 min | 61¢ | 67% | 4¢ | ❌ Lost | -$6.25 |
| 9/29 5:47:19 AM | Silver | UP | 12.7 min | 39¢ | 46% | 5¢ | ✅ Won | $5.93 |
| 9/29 5:32:02 AM | Gold | UP | 12.9 min | 26¢ | 32% | 4¢ | ❌ Lost | -$2.74 |
| 9/29 5:31:28 AM | Silver | UP | 13.5 min | 34¢ | 42% | 6¢ | ❌ Lost | -$3.56 |
| 9/29 5:20:37 AM | Silver | DOWN | 9.4 min | 33¢ | 42% | 7¢ | ❌ Lost | -$3.46 |
| 9/29 5:19:24 AM | Gold | UP | 10.6 min | 56¢ | 63% | 5¢ | ✅ Won | $4.22 |
