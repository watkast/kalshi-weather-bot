# Gold & Silver Fair-Value Bot

*Updated Tue Sep 29, 3:12 PM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

🔴 **Losing.** Not beating Kalshi's prices after fees.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 123 | 121 | 42 (35%) | 39¢ | 47% | -$67.74 | -14% |
| Silver | 62 | 61 | 20 (33%) | 34¢ | 41% | -$14.03 | -7% |
| Gold | 61 | 60 | 22 (37%) | 44¢ | 52% | -$53.71 | -20% |

*Earlier half -$20.85 / later half -$46.89.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 124 | 43 (35%) | -$84.42 | -16% |
| 4¢+ ← live bot | 121 | 44 (36%) | -$14.91 | -3% |
| 6¢+ | 109 | 47 (43%) | $92.60 | +25% |
| 8¢+ | 96 | 40 (42%) | $97.72 | +32% |
| 10¢+ | 83 | 31 (37%) | $61.88 | +25% |
| 15¢+ | 50 | 18 (36%) | $52.85 | +42% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 3092 | -0.9% |
| Hyperliquid price vs Kalshi's target | 3092 | +2.0% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 3:02:32 PM | Gold | DOWN | 12.5 min | 41¢ | 52% | 9¢ | Open | — |
| 9/29 3:01:02 PM | Silver | DOWN | 13.9 min | 14¢ | 49% | 34¢ | Open | — |
| 9/29 2:46:28 PM | Silver | UP | 13.5 min | 30¢ | 37% | 5¢ | ❌ Lost | -$3.15 |
| 9/29 2:46:03 PM | Gold | UP | 13.9 min | 32¢ | 52% | 18¢ | ❌ Lost | -$3.36 |
| 9/29 2:32:20 PM | Silver | DOWN | 12.7 min | 28¢ | 35% | 5¢ | ❌ Lost | -$2.95 |
| 9/29 2:31:04 PM | Gold | UP | 13.9 min | 41¢ | 50% | 7¢ | ✅ Won | $5.73 |
| 9/29 2:17:22 PM | Gold | DOWN | 12.6 min | 50¢ | 56% | 5¢ | ❌ Lost | -$5.18 |
| 9/29 2:16:04 PM | Silver | UP | 13.9 min | 30¢ | 38% | 7¢ | ✅ Won | $6.85 |
| 9/29 2:02:20 PM | Silver | UP | 12.7 min | 19¢ | 25% | 4¢ | ❌ Lost | -$2.01 |
| 9/29 2:01:04 PM | Gold | UP | 13.9 min | 43¢ | 57% | 12¢ | ❌ Lost | -$4.48 |
| 9/29 1:49:06 PM | Silver | UP | 10.9 min | 34¢ | 41% | 5¢ | ✅ Won | $6.44 |
| 9/29 1:46:02 PM | Gold | UP | 13.9 min | 30¢ | 50% | 18¢ | ✅ Won | $6.85 |
