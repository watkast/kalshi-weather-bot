# Gold & Silver Fair-Value Bot

*Updated Tue Sep 29, 6:03 AM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

🔴 **Losing.** Not beating Kalshi's prices after fees.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 69 | 68 | 25 (37%) | 40¢ | 48% | -$35.36 | -12% |
| Silver | 34 | 34 | 11 (32%) | 35¢ | 43% | -$15.42 | -12% |
| Gold | 35 | 34 | 14 (41%) | 45¢ | 53% | -$19.94 | -12% |

*Earlier half $0.56 / later half -$35.92.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 69 | 23 (33%) | -$64.93 | -22% |
| 4¢+ ← live bot | 66 | 23 (35%) | -$23.74 | -9% |
| 6¢+ | 58 | 23 (40%) | $25.98 | +13% |
| 8¢+ | 51 | 19 (37%) | $24.77 | +15% |
| 10¢+ | 42 | 13 (31%) | $4.76 | +4% |
| 15¢+ | 24 | 9 (38%) | $27.39 | +44% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 1705 | -1.3% |
| Hyperliquid price vs Kalshi's target | 1705 | +5.6% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 6:03:11 AM | Gold | UP | 11.8 min | 63¢ | 70% | 6¢ | Open | — |
| 9/29 5:48:47 AM | Gold | DOWN | 11.2 min | 61¢ | 67% | 4¢ | ❌ Lost | -$6.25 |
| 9/29 5:47:19 AM | Silver | UP | 12.7 min | 39¢ | 46% | 5¢ | ✅ Won | $5.93 |
| 9/29 5:32:02 AM | Gold | UP | 12.9 min | 26¢ | 32% | 4¢ | ❌ Lost | -$2.74 |
| 9/29 5:31:28 AM | Silver | UP | 13.5 min | 34¢ | 42% | 6¢ | ❌ Lost | -$3.56 |
| 9/29 5:20:37 AM | Silver | DOWN | 9.4 min | 33¢ | 42% | 7¢ | ❌ Lost | -$3.46 |
| 9/29 5:19:24 AM | Gold | UP | 10.6 min | 56¢ | 63% | 5¢ | ✅ Won | $4.22 |
| 9/29 5:03:59 AM | Silver | DOWN | 11.0 min | 46¢ | 53% | 5¢ | ❌ Lost | -$4.78 |
| 9/29 5:01:26 AM | Gold | DOWN | 13.6 min | 37¢ | 45% | 6¢ | ❌ Lost | -$3.87 |
| 9/29 4:54:40 AM | Silver | UP | 5.3 min | 25¢ | 31% | 5¢ | ✅ Won | $7.36 |
| 9/29 4:46:03 AM | Gold | UP | 13.9 min | 53¢ | 60% | 5¢ | ✅ Won | $4.52 |
| 9/29 4:33:10 AM | Silver | UP | 11.8 min | 36¢ | 43% | 5¢ | ✅ Won | $6.23 |
