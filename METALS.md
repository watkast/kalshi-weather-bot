# Gold & Silver Fair-Value Bot

*Updated Tue Sep 29, 4:16 PM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

🔴 **Losing.** Not beating Kalshi's prices after fees.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 131 | 131 | 45 (34%) | 38¢ | 47% | -$73.49 | -14% |
| Silver | 66 | 66 | 21 (32%) | 33¢ | 41% | -$15.74 | -7% |
| Gold | 65 | 65 | 24 (37%) | 44¢ | 53% | -$57.75 | -19% |

*Earlier half -$32.30 / later half -$41.19.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 134 | 45 (34%) | -$105.83 | -19% |
| 4¢+ ← live bot | 131 | 47 (36%) | -$22.43 | -5% |
| 6¢+ | 119 | 50 (42%) | $85.79 | +21% |
| 8¢+ | 106 | 43 (41%) | $91.00 | +27% |
| 10¢+ | 92 | 34 (37%) | $59.11 | +21% |
| 15¢+ | 58 | 21 (36%) | $53.21 | +34% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 3322 | -5.1% |
| Hyperliquid price vs Kalshi's target | 3322 | +1.9% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 4:01:03 PM | Gold | UP | 13.9 min | 67¢ | 89% | 21¢ | ❌ Lost | -$6.86 |
| 9/29 4:01:03 PM | Silver | UP | 13.9 min | 33¢ | 70% | 35¢ | ✅ Won | $6.54 |
| 9/29 3:48:49 PM | Silver | DOWN | 11.2 min | 15¢ | 20% | 4¢ | ❌ Lost | -$1.59 |
| 9/29 3:46:33 PM | Gold | DOWN | 13.4 min | 28¢ | 36% | 6¢ | ❌ Lost | -$2.95 |
| 9/29 3:31:30 PM | Gold | UP | 13.5 min | 49¢ | 56% | 5¢ | ❌ Lost | -$5.08 |
| 9/29 3:31:18 PM | Silver | DOWN | 13.7 min | 27¢ | 35% | 7¢ | ❌ Lost | -$2.84 |
| 9/29 3:23:32 PM | Silver | UP | 6.5 min | 22¢ | 37% | 14¢ | ❌ Lost | -$2.33 |
| 9/29 3:16:35 PM | Gold | DOWN | 13.4 min | 47¢ | 53% | 4¢ | ✅ Won | $5.12 |
| 9/29 3:02:32 PM | Gold | DOWN | 12.5 min | 41¢ | 52% | 9¢ | ✅ Won | $5.73 |
| 9/29 3:01:02 PM | Silver | DOWN | 13.9 min | 14¢ | 49% | 34¢ | ❌ Lost | -$1.49 |
| 9/29 2:46:28 PM | Silver | UP | 13.5 min | 30¢ | 37% | 5¢ | ❌ Lost | -$3.15 |
| 9/29 2:46:03 PM | Gold | UP | 13.9 min | 32¢ | 52% | 18¢ | ❌ Lost | -$3.36 |
