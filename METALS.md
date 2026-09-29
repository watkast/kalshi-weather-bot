# Gold & Silver Fair-Value Bot

*Updated Tue Sep 29, 5:03 AM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

🔴 **Losing.** Not beating Kalshi's prices after fees.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 61 | 60 | 23 (38%) | 40¢ | 48% | -$20.85 | -8% |
| Silver | 30 | 30 | 10 (33%) | 35¢ | 43% | -$9.55 | -9% |
| Gold | 31 | 30 | 13 (43%) | 45¢ | 53% | -$11.30 | -8% |

*Earlier half -$0.60 / later half -$20.25.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 61 | 20 (33%) | -$61.47 | -24% |
| 4¢+ ← live bot | 58 | 20 (34%) | -$20.70 | -9% |
| 6¢+ | 53 | 21 (40%) | $27.93 | +15% |
| 8¢+ | 48 | 18 (38%) | $28.61 | +19% |
| 10¢+ | 40 | 13 (32%) | $14.02 | +12% |
| 15¢+ | 22 | 9 (41%) | $33.56 | +59% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 1505 | -1.8% |
| Hyperliquid price vs Kalshi's target | 1505 | +4.3% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 5:01:26 AM | Gold | DOWN | 13.6 min | 37¢ | 45% | 6¢ | Open | — |
| 9/29 4:54:40 AM | Silver | UP | 5.3 min | 25¢ | 31% | 5¢ | ✅ Won | $7.36 |
| 9/29 4:46:03 AM | Gold | UP | 13.9 min | 53¢ | 60% | 5¢ | ✅ Won | $4.52 |
| 9/29 4:33:10 AM | Silver | UP | 11.8 min | 36¢ | 43% | 5¢ | ✅ Won | $6.23 |
| 9/29 4:31:21 AM | Gold | UP | 13.7 min | 46¢ | 57% | 9¢ | ✅ Won | $5.22 |
| 9/29 4:18:16 AM | Silver | UP | 11.7 min | 30¢ | 36% | 4¢ | ❌ Lost | -$3.15 |
| 9/29 4:17:30 AM | Gold | DOWN | 12.5 min | 51¢ | 60% | 7¢ | ❌ Lost | -$5.28 |
| 9/29 4:02:01 AM | Silver | UP | 13.0 min | 75¢ | 81% | 4¢ | ✅ Won | $2.36 |
| 9/29 4:01:05 AM | Gold | UP | 13.9 min | 45¢ | 51% | 4¢ | ✅ Won | $5.32 |
| 9/29 3:51:54 AM | Silver | UP | 8.1 min | 24¢ | 32% | 7¢ | ❌ Lost | -$2.49 |
| 9/29 3:47:14 AM | Gold | UP | 12.8 min | 61¢ | 69% | 6¢ | ✅ Won | $3.73 |
| 9/29 3:32:14 AM | Silver | DOWN | 12.8 min | 35¢ | 41% | 4¢ | ❌ Lost | -$3.66 |
