# Gold & Silver Fair-Value Bot

*Updated Tue Sep 29, 7:13 AM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

🔴 **Losing.** Not beating Kalshi's prices after fees.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 77 | 76 | 27 (36%) | 40¢ | 48% | -$44.48 | -14% |
| Silver | 39 | 38 | 12 (32%) | 34¢ | 42% | -$16.28 | -12% |
| Gold | 38 | 38 | 15 (39%) | 45¢ | 53% | -$28.20 | -16% |

*Earlier half -$11.70 / later half -$32.78.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 77 | 25 (32%) | -$68.90 | -22% |
| 4¢+ ← live bot | 74 | 25 (34%) | -$24.82 | -9% |
| 6¢+ | 66 | 26 (39%) | $32.38 | +14% |
| 8¢+ | 57 | 23 (40%) | $44.27 | +24% |
| 10¢+ | 47 | 15 (32%) | $6.81 | +5% |
| 15¢+ | 26 | 9 (35%) | $22.43 | +33% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 1906 | -1.5% |
| Hyperliquid price vs Kalshi's target | 1906 | +4.4% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 7:02:34 AM | Silver | DOWN | 12.4 min | 36¢ | 45% | 8¢ | Open | — |
| 9/29 6:46:04 AM | Gold | UP | 13.9 min | 26¢ | 32% | 5¢ | ❌ Lost | -$2.74 |
| 9/29 6:46:04 AM | Silver | UP | 13.9 min | 22¢ | 29% | 5¢ | ❌ Lost | -$2.33 |
| 9/29 6:32:30 AM | Gold | DOWN | 12.5 min | 36¢ | 46% | 8¢ | ❌ Lost | -$3.77 |
| 9/29 6:32:18 AM | Silver | UP | 12.7 min | 26¢ | 32% | 5¢ | ❌ Lost | -$2.74 |
| 9/29 6:19:10 AM | Gold | UP | 10.8 min | 51¢ | 58% | 5¢ | ✅ Won | $4.72 |
| 9/29 6:16:56 AM | Silver | DOWN | 13.1 min | 29¢ | 36% | 6¢ | ❌ Lost | -$3.05 |
| 9/29 6:05:26 AM | Silver | DOWN | 9.6 min | 26¢ | 33% | 5¢ | ✅ Won | $7.26 |
| 9/29 6:03:11 AM | Gold | UP | 11.8 min | 63¢ | 70% | 6¢ | ❌ Lost | -$6.47 |
| 9/29 5:48:47 AM | Gold | DOWN | 11.2 min | 61¢ | 67% | 4¢ | ❌ Lost | -$6.25 |
| 9/29 5:47:19 AM | Silver | UP | 12.7 min | 39¢ | 46% | 5¢ | ✅ Won | $5.93 |
| 9/29 5:32:02 AM | Gold | UP | 12.9 min | 26¢ | 32% | 4¢ | ❌ Lost | -$2.74 |
