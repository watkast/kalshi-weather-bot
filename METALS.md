# Gold & Silver Fair-Value Bot

*Updated Tue Sep 29, 3:12 AM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

🔴 **Losing.** Not beating Kalshi's prices after fees.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 46 | 44 | 15 (34%) | 39¢ | 47% | -$29.67 | -17% |
| Silver | 23 | 22 | 6 (27%) | 34¢ | 42% | -$17.06 | -22% |
| Gold | 23 | 22 | 9 (41%) | 45¢ | 53% | -$12.61 | -12% |

*Earlier half $23.44 / later half -$53.11.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 45 | 12 (27%) | -$67.91 | -36% |
| 4¢+ ← live bot | 43 | 13 (30%) | -$24.71 | -16% |
| 6¢+ | 40 | 12 (30%) | -$6.69 | -5% |
| 8¢+ | 36 | 12 (33%) | $19.18 | +19% |
| 10¢+ | 31 | 8 (26%) | $1.75 | +2% |
| 15¢+ | 16 | 5 (31%) | $15.52 | +45% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 1105 | -7.0% |
| Hyperliquid price vs Kalshi's target | 1105 | -12.2% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 3:04:34 AM | Silver | DOWN | 10.4 min | 32¢ | 40% | 7¢ | Open | — |
| 9/29 3:02:03 AM | Gold | DOWN | 12.9 min | 31¢ | 38% | 6¢ | Open | — |
| 9/29 12:33:04 AM | Gold | DOWN | 11.9 min | 33¢ | 42% | 7¢ | ❌ Lost | -$3.46 |
| 9/29 12:31:29 AM | Silver | DOWN | 13.5 min | 34¢ | 40% | 4¢ | ❌ Lost | -$3.56 |
| 9/29 12:16:42 AM | Silver | UP | 13.3 min | 28¢ | 35% | 5¢ | ❌ Lost | -$2.95 |
| 9/29 12:16:24 AM | Gold | UP | 13.6 min | 28¢ | 37% | 8¢ | ❌ Lost | -$2.95 |
| 9/29 12:03:03 AM | Gold | DOWN | 11.9 min | 36¢ | 45% | 7¢ | ❌ Lost | -$3.77 |
| 9/29 12:03:03 AM | Silver | DOWN | 11.9 min | 12¢ | 18% | 5¢ | ❌ Lost | -$1.28 |
| 9/28 11:46:05 PM | Gold | UP | 13.9 min | 28¢ | 34% | 5¢ | ✅ Won | $7.05 |
| 9/28 11:46:05 PM | Silver | UP | 13.9 min | 33¢ | 42% | 8¢ | ❌ Lost | -$3.46 |
| 9/28 11:34:38 PM | Silver | DOWN | 10.4 min | 81¢ | 92% | 10¢ | ❌ Lost | -$8.21 |
| 9/28 11:31:34 PM | Gold | DOWN | 13.4 min | 75¢ | 83% | 6¢ | ❌ Lost | -$7.64 |
