# Gold & Silver Fair-Value Bot

*Updated Tue Sep 29, 4:33 AM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

🔴 **Losing.** Not beating Kalshi's prices after fees.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 57 | 56 | 19 (34%) | 40¢ | 48% | -$44.18 | -19% |
| Silver | 28 | 28 | 8 (29%) | 35¢ | 43% | -$23.14 | -22% |
| Gold | 29 | 28 | 11 (39%) | 45¢ | 53% | -$21.04 | -16% |

*Earlier half -$0.54 / later half -$43.64.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 57 | 16 (28%) | -$82.07 | -34% |
| 4¢+ ← live bot | 54 | 16 (30%) | -$42.60 | -21% |
| 6¢+ | 49 | 17 (35%) | $5.21 | +3% |
| 8¢+ | 44 | 14 (32%) | $5.89 | +4% |
| 10¢+ | 36 | 9 (25%) | -$8.70 | -9% |
| 15¢+ | 19 | 6 (32%) | $13.37 | +29% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 1405 | -6.2% |
| Hyperliquid price vs Kalshi's target | 1405 | -2.9% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 4:31:21 AM | Gold | UP | 13.7 min | 46¢ | 57% | 9¢ | Open | — |
| 9/29 4:18:16 AM | Silver | UP | 11.7 min | 30¢ | 36% | 4¢ | ❌ Lost | -$3.15 |
| 9/29 4:17:30 AM | Gold | DOWN | 12.5 min | 51¢ | 60% | 7¢ | ❌ Lost | -$5.28 |
| 9/29 4:02:01 AM | Silver | UP | 13.0 min | 75¢ | 81% | 4¢ | ✅ Won | $2.36 |
| 9/29 4:01:05 AM | Gold | UP | 13.9 min | 45¢ | 51% | 4¢ | ✅ Won | $5.32 |
| 9/29 3:51:54 AM | Silver | UP | 8.1 min | 24¢ | 32% | 7¢ | ❌ Lost | -$2.49 |
| 9/29 3:47:14 AM | Gold | UP | 12.8 min | 61¢ | 69% | 6¢ | ✅ Won | $3.73 |
| 9/29 3:32:14 AM | Silver | DOWN | 12.8 min | 35¢ | 41% | 4¢ | ❌ Lost | -$3.66 |
| 9/29 3:31:07 AM | Gold | DOWN | 13.9 min | 47¢ | 56% | 7¢ | ❌ Lost | -$4.88 |
| 9/29 3:22:33 AM | Silver | UP | 7.5 min | 56¢ | 66% | 8¢ | ❌ Lost | -$5.78 |
| 9/29 3:16:18 AM | Gold | DOWN | 13.7 min | 39¢ | 50% | 9¢ | ❌ Lost | -$4.07 |
| 9/29 3:04:34 AM | Silver | DOWN | 10.4 min | 32¢ | 40% | 7¢ | ✅ Won | $6.64 |
