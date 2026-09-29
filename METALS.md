# Gold & Silver Fair-Value Bot

*Updated Tue Sep 29, 12:31 AM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

🔴 **Losing.** Not beating Kalshi's prices after fees.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 42 | 42 | 15 (36%) | 40¢ | 48% | -$22.65 | -13% |
| Silver | 21 | 21 | 6 (29%) | 34¢ | 42% | -$13.50 | -18% |
| Gold | 21 | 21 | 9 (43%) | 46¢ | 53% | -$9.15 | -9% |

*Earlier half $26.69 / later half -$49.34.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 42 | 12 (29%) | -$56.10 | -32% |
| 4¢+ ← live bot | 41 | 13 (32%) | -$17.79 | -12% |
| 6¢+ | 38 | 12 (32%) | $1.14 | +1% |
| 8¢+ | 34 | 12 (35%) | $23.31 | +24% |
| 10¢+ | 29 | 8 (28%) | $6.09 | +8% |
| 15¢+ | 14 | 5 (36%) | $18.25 | +57% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 1051 | -6.1% |
| Hyperliquid price vs Kalshi's target | 1051 | -13.4% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 12:16:42 AM | Silver | UP | 13.3 min | 28¢ | 35% | 5¢ | ❌ Lost | -$2.95 |
| 9/29 12:16:24 AM | Gold | UP | 13.6 min | 28¢ | 37% | 8¢ | ❌ Lost | -$2.95 |
| 9/29 12:03:03 AM | Gold | DOWN | 11.9 min | 36¢ | 45% | 7¢ | ❌ Lost | -$3.77 |
| 9/29 12:03:03 AM | Silver | DOWN | 11.9 min | 12¢ | 18% | 5¢ | ❌ Lost | -$1.28 |
| 9/28 11:46:05 PM | Gold | UP | 13.9 min | 28¢ | 34% | 5¢ | ✅ Won | $7.05 |
| 9/28 11:46:05 PM | Silver | UP | 13.9 min | 33¢ | 42% | 8¢ | ❌ Lost | -$3.46 |
| 9/28 11:34:38 PM | Silver | DOWN | 10.4 min | 81¢ | 92% | 10¢ | ❌ Lost | -$8.21 |
| 9/28 11:31:34 PM | Gold | DOWN | 13.4 min | 75¢ | 83% | 6¢ | ❌ Lost | -$7.64 |
| 9/28 11:18:01 PM | Silver | DOWN | 12.0 min | 28¢ | 46% | 16¢ | ✅ Won | $7.05 |
| 9/28 11:17:37 PM | Gold | DOWN | 12.4 min | 58¢ | 66% | 6¢ | ❌ Lost | -$5.98 |
| 9/28 11:02:38 PM | Gold | UP | 12.4 min | 65¢ | 73% | 7¢ | ✅ Won | $3.34 |
| 9/28 11:01:02 PM | Silver | DOWN | 13.9 min | 31¢ | 39% | 6¢ | ❌ Lost | -$3.25 |
