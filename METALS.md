# Gold & Silver Fair-Value Bot

*Updated Tue Sep 29, 4:22 AM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

🔴 **Losing.** Not beating Kalshi's prices after fees.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 56 | 54 | 19 (35%) | 40¢ | 48% | -$35.75 | -16% |
| Silver | 28 | 27 | 8 (30%) | 36¢ | 44% | -$19.99 | -20% |
| Gold | 28 | 27 | 11 (41%) | 45¢ | 53% | -$15.76 | -13% |

*Earlier half $2.20 / later half -$37.95.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 55 | 16 (29%) | -$72.93 | -31% |
| 4¢+ ← live bot | 52 | 16 (31%) | -$33.56 | -17% |
| 6¢+ | 47 | 16 (34%) | $1.62 | +1% |
| 8¢+ | 42 | 14 (33%) | $12.74 | +10% |
| 10¢+ | 34 | 9 (26%) | -$1.87 | -2% |
| 15¢+ | 18 | 6 (33%) | $19.15 | +47% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 1355 | -6.0% |
| Hyperliquid price vs Kalshi's target | 1355 | -5.2% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 4:18:16 AM | Silver | UP | 11.7 min | 30¢ | 36% | 4¢ | Open | — |
| 9/29 4:17:30 AM | Gold | DOWN | 12.5 min | 51¢ | 60% | 7¢ | Open | — |
| 9/29 4:02:01 AM | Silver | UP | 13.0 min | 75¢ | 81% | 4¢ | ✅ Won | $2.36 |
| 9/29 4:01:05 AM | Gold | UP | 13.9 min | 45¢ | 51% | 4¢ | ✅ Won | $5.32 |
| 9/29 3:51:54 AM | Silver | UP | 8.1 min | 24¢ | 32% | 7¢ | ❌ Lost | -$2.49 |
| 9/29 3:47:14 AM | Gold | UP | 12.8 min | 61¢ | 69% | 6¢ | ✅ Won | $3.73 |
| 9/29 3:32:14 AM | Silver | DOWN | 12.8 min | 35¢ | 41% | 4¢ | ❌ Lost | -$3.66 |
| 9/29 3:31:07 AM | Gold | DOWN | 13.9 min | 47¢ | 56% | 7¢ | ❌ Lost | -$4.88 |
| 9/29 3:22:33 AM | Silver | UP | 7.5 min | 56¢ | 66% | 8¢ | ❌ Lost | -$5.78 |
| 9/29 3:16:18 AM | Gold | DOWN | 13.7 min | 39¢ | 50% | 9¢ | ❌ Lost | -$4.07 |
| 9/29 3:04:34 AM | Silver | DOWN | 10.4 min | 32¢ | 40% | 7¢ | ✅ Won | $6.64 |
| 9/29 3:02:03 AM | Gold | DOWN | 12.9 min | 31¢ | 38% | 6¢ | ❌ Lost | -$3.25 |
