# Gold & Silver Fair-Value Bot

*Updated Tue Sep 29, 11:00 AM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

🔴 **Losing.** Not beating Kalshi's prices after fees.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 90 | 88 | 28 (32%) | 39¢ | 47% | -$79.50 | -22% |
| Silver | 46 | 45 | 13 (29%) | 34¢ | 41% | -$28.21 | -18% |
| Gold | 44 | 43 | 15 (35%) | 45¢ | 53% | -$51.29 | -25% |

*Earlier half -$29.67 / later half -$49.83.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 91 | 29 (32%) | -$87.58 | -23% |
| 4¢+ ← live bot | 88 | 29 (33%) | -$36.74 | -11% |
| 6¢+ | 77 | 29 (38%) | $27.02 | +10% |
| 8¢+ | 64 | 26 (41%) | $51.57 | +25% |
| 10¢+ | 53 | 18 (34%) | $15.81 | +10% |
| 15¢+ | 28 | 9 (32%) | $16.74 | +23% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 2232 | -2.4% |
| Hyperliquid price vs Kalshi's target | 2232 | +1.5% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 10:50:18 AM | Silver | DOWN | 9.7 min | 29¢ | 36% | 6¢ | Open | — |
| 9/29 10:46:06 AM | Gold | UP | 13.9 min | 32¢ | 39% | 6¢ | Open | — |
| 9/29 10:38:20 AM | Gold | UP | 6.7 min | 48¢ | 55% | 5¢ | ❌ Lost | -$4.98 |
| 9/29 10:37:40 AM | Silver | DOWN | 7.3 min | 17¢ | 26% | 8¢ | ✅ Won | $8.20 |
| 9/29 8:18:54 AM | Silver | DOWN | 11.1 min | 38¢ | 44% | 4¢ | ❌ Lost | -$3.98 |
| 9/29 8:16:12 AM | Gold | DOWN | 13.8 min | 46¢ | 52% | 4¢ | ❌ Lost | -$4.78 |
| 9/29 8:01:24 AM | Gold | DOWN | 13.6 min | 19¢ | 25% | 5¢ | ❌ Lost | -$2.01 |
| 9/29 8:01:02 AM | Silver | DOWN | 13.9 min | 17¢ | 23% | 5¢ | ❌ Lost | -$1.80 |
| 9/29 7:46:04 AM | Silver | DOWN | 13.9 min | 37¢ | 43% | 4¢ | ❌ Lost | -$3.87 |
| 9/29 7:39:00 AM | Silver | UP | 6.0 min | 34¢ | 41% | 6¢ | ❌ Lost | -$3.56 |
| 9/29 7:31:22 AM | Gold | UP | 13.6 min | 71¢ | 77% | 4¢ | ❌ Lost | -$7.25 |
| 9/29 7:19:22 AM | Silver | DOWN | 10.6 min | 30¢ | 37% | 6¢ | ❌ Lost | -$3.15 |
