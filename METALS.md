# Gold & Silver Fair-Value Bot

*Updated Tue Sep 29, 5:23 AM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

🔴 **Losing.** Not beating Kalshi's prices after fees.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 64 | 62 | 23 (37%) | 40¢ | 48% | -$29.50 | -11% |
| Silver | 32 | 31 | 10 (32%) | 35¢ | 43% | -$14.33 | -13% |
| Gold | 32 | 31 | 13 (42%) | 45¢ | 53% | -$15.17 | -10% |

*Earlier half -$3.85 / later half -$25.65.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 63 | 20 (32%) | -$70.32 | -26% |
| 4¢+ ← live bot | 60 | 20 (33%) | -$29.25 | -13% |
| 6¢+ | 55 | 22 (40%) | $28.67 | +15% |
| 8¢+ | 50 | 19 (38%) | $29.35 | +18% |
| 10¢+ | 41 | 13 (32%) | $9.34 | +8% |
| 15¢+ | 23 | 9 (39%) | $28.88 | +47% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 1555 | -1.4% |
| Hyperliquid price vs Kalshi's target | 1555 | +6.3% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 5:20:37 AM | Silver | DOWN | 9.4 min | 33¢ | 42% | 7¢ | Open | — |
| 9/29 5:19:24 AM | Gold | UP | 10.6 min | 56¢ | 63% | 5¢ | Open | — |
| 9/29 5:03:59 AM | Silver | DOWN | 11.0 min | 46¢ | 53% | 5¢ | ❌ Lost | -$4.78 |
| 9/29 5:01:26 AM | Gold | DOWN | 13.6 min | 37¢ | 45% | 6¢ | ❌ Lost | -$3.87 |
| 9/29 4:54:40 AM | Silver | UP | 5.3 min | 25¢ | 31% | 5¢ | ✅ Won | $7.36 |
| 9/29 4:46:03 AM | Gold | UP | 13.9 min | 53¢ | 60% | 5¢ | ✅ Won | $4.52 |
| 9/29 4:33:10 AM | Silver | UP | 11.8 min | 36¢ | 43% | 5¢ | ✅ Won | $6.23 |
| 9/29 4:31:21 AM | Gold | UP | 13.7 min | 46¢ | 57% | 9¢ | ✅ Won | $5.22 |
| 9/29 4:18:16 AM | Silver | UP | 11.7 min | 30¢ | 36% | 4¢ | ❌ Lost | -$3.15 |
| 9/29 4:17:30 AM | Gold | DOWN | 12.5 min | 51¢ | 60% | 7¢ | ❌ Lost | -$5.28 |
| 9/29 4:02:01 AM | Silver | UP | 13.0 min | 75¢ | 81% | 4¢ | ✅ Won | $2.36 |
| 9/29 4:01:05 AM | Gold | UP | 13.9 min | 45¢ | 51% | 4¢ | ✅ Won | $5.32 |
