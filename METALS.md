# Gold & Silver Fair-Value Bot

*Updated Tue Sep 29, 3:52 PM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

🔴 **Losing.** Not beating Kalshi's prices after fees.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 129 | 127 | 44 (35%) | 38¢ | 47% | -$68.63 | -13% |
| Silver | 65 | 64 | 20 (31%) | 33¢ | 41% | -$20.69 | -9% |
| Gold | 64 | 63 | 24 (38%) | 44¢ | 52% | -$47.94 | -17% |

*Earlier half -$25.28 / later half -$43.35.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 130 | 44 (34%) | -$98.04 | -18% |
| 4¢+ ← live bot | 127 | 46 (36%) | -$14.75 | -3% |
| 6¢+ | 115 | 49 (43%) | $92.16 | +23% |
| 8¢+ | 102 | 42 (41%) | $97.28 | +30% |
| 10¢+ | 89 | 33 (37%) | $60.83 | +23% |
| 15¢+ | 56 | 20 (36%) | $52.81 | +36% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 3246 | -4.6% |
| Hyperliquid price vs Kalshi's target | 3246 | +1.7% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 3:48:49 PM | Silver | DOWN | 11.2 min | 15¢ | 20% | 4¢ | Open | — |
| 9/29 3:46:33 PM | Gold | DOWN | 13.4 min | 28¢ | 36% | 6¢ | Open | — |
| 9/29 3:31:30 PM | Gold | UP | 13.5 min | 49¢ | 56% | 5¢ | ❌ Lost | -$5.08 |
| 9/29 3:31:18 PM | Silver | DOWN | 13.7 min | 27¢ | 35% | 7¢ | ❌ Lost | -$2.84 |
| 9/29 3:23:32 PM | Silver | UP | 6.5 min | 22¢ | 37% | 14¢ | ❌ Lost | -$2.33 |
| 9/29 3:16:35 PM | Gold | DOWN | 13.4 min | 47¢ | 53% | 4¢ | ✅ Won | $5.12 |
| 9/29 3:02:32 PM | Gold | DOWN | 12.5 min | 41¢ | 52% | 9¢ | ✅ Won | $5.73 |
| 9/29 3:01:02 PM | Silver | DOWN | 13.9 min | 14¢ | 49% | 34¢ | ❌ Lost | -$1.49 |
| 9/29 2:46:28 PM | Silver | UP | 13.5 min | 30¢ | 37% | 5¢ | ❌ Lost | -$3.15 |
| 9/29 2:46:03 PM | Gold | UP | 13.9 min | 32¢ | 52% | 18¢ | ❌ Lost | -$3.36 |
| 9/29 2:32:20 PM | Silver | DOWN | 12.7 min | 28¢ | 35% | 5¢ | ❌ Lost | -$2.95 |
| 9/29 2:31:04 PM | Gold | UP | 13.9 min | 41¢ | 50% | 7¢ | ✅ Won | $5.73 |
