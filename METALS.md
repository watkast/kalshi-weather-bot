# Gold & Silver Fair-Value Bot

*Updated Tue Sep 29, 6:53 AM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

🔴 **Losing.** Not beating Kalshi's prices after fees.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 76 | 74 | 27 (36%) | 40¢ | 48% | -$39.41 | -13% |
| Silver | 38 | 37 | 12 (32%) | 35¢ | 43% | -$13.95 | -10% |
| Gold | 38 | 37 | 15 (41%) | 46¢ | 54% | -$25.46 | -15% |

*Earlier half -$18.75 / later half -$20.66.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 75 | 25 (33%) | -$63.83 | -20% |
| 4¢+ ← live bot | 72 | 25 (35%) | -$19.75 | -7% |
| 6¢+ | 64 | 26 (41%) | $36.82 | +16% |
| 8¢+ | 56 | 23 (41%) | $46.07 | +25% |
| 10¢+ | 46 | 15 (33%) | $8.30 | +6% |
| 15¢+ | 26 | 9 (35%) | $22.43 | +33% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 1856 | -1.2% |
| Hyperliquid price vs Kalshi's target | 1856 | +5.4% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 6:46:04 AM | Gold | UP | 13.9 min | 26¢ | 32% | 5¢ | Open | — |
| 9/29 6:46:04 AM | Silver | UP | 13.9 min | 22¢ | 29% | 5¢ | Open | — |
| 9/29 6:32:30 AM | Gold | DOWN | 12.5 min | 36¢ | 46% | 8¢ | ❌ Lost | -$3.77 |
| 9/29 6:32:18 AM | Silver | UP | 12.7 min | 26¢ | 32% | 5¢ | ❌ Lost | -$2.74 |
| 9/29 6:19:10 AM | Gold | UP | 10.8 min | 51¢ | 58% | 5¢ | ✅ Won | $4.72 |
| 9/29 6:16:56 AM | Silver | DOWN | 13.1 min | 29¢ | 36% | 6¢ | ❌ Lost | -$3.05 |
| 9/29 6:05:26 AM | Silver | DOWN | 9.6 min | 26¢ | 33% | 5¢ | ✅ Won | $7.26 |
| 9/29 6:03:11 AM | Gold | UP | 11.8 min | 63¢ | 70% | 6¢ | ❌ Lost | -$6.47 |
| 9/29 5:48:47 AM | Gold | DOWN | 11.2 min | 61¢ | 67% | 4¢ | ❌ Lost | -$6.25 |
| 9/29 5:47:19 AM | Silver | UP | 12.7 min | 39¢ | 46% | 5¢ | ✅ Won | $5.93 |
| 9/29 5:32:02 AM | Gold | UP | 12.9 min | 26¢ | 32% | 4¢ | ❌ Lost | -$2.74 |
| 9/29 5:31:28 AM | Silver | UP | 13.5 min | 34¢ | 42% | 6¢ | ❌ Lost | -$3.56 |
