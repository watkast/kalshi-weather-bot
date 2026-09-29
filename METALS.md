# Gold & Silver Fair-Value Bot

*Updated Tue Sep 29, 2:42 PM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

🔴 **Losing.** Not beating Kalshi's prices after fees.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 119 | 117 | 41 (35%) | 39¢ | 47% | -$64.01 | -14% |
| Silver | 60 | 59 | 20 (34%) | 34¢ | 41% | -$7.93 | -4% |
| Gold | 59 | 58 | 21 (36%) | 44¢ | 52% | -$56.08 | -21% |

*Earlier half -$32.73 / later half -$31.28.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 120 | 42 (35%) | -$80.79 | -16% |
| 4¢+ ← live bot | 117 | 43 (37%) | -$11.28 | -3% |
| 6¢+ | 105 | 46 (44%) | $94.67 | +26% |
| 8¢+ | 92 | 40 (43%) | $107.64 | +37% |
| 10¢+ | 79 | 31 (39%) | $71.38 | +30% |
| 15¢+ | 48 | 18 (38%) | $57.59 | +47% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 2990 | -0.3% |
| Hyperliquid price vs Kalshi's target | 2990 | +2.7% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 2:32:20 PM | Silver | DOWN | 12.7 min | 28¢ | 35% | 5¢ | Open | — |
| 9/29 2:31:04 PM | Gold | UP | 13.9 min | 41¢ | 50% | 7¢ | Open | — |
| 9/29 2:17:22 PM | Gold | DOWN | 12.6 min | 50¢ | 56% | 5¢ | ❌ Lost | -$5.18 |
| 9/29 2:16:04 PM | Silver | UP | 13.9 min | 30¢ | 38% | 7¢ | ✅ Won | $6.85 |
| 9/29 2:02:20 PM | Silver | UP | 12.7 min | 19¢ | 25% | 4¢ | ❌ Lost | -$2.01 |
| 9/29 2:01:04 PM | Gold | UP | 13.9 min | 43¢ | 57% | 12¢ | ❌ Lost | -$4.48 |
| 9/29 1:49:06 PM | Silver | UP | 10.9 min | 34¢ | 41% | 5¢ | ✅ Won | $6.44 |
| 9/29 1:46:02 PM | Gold | UP | 13.9 min | 30¢ | 50% | 18¢ | ✅ Won | $6.85 |
| 9/29 1:33:34 PM | Silver | UP | 11.4 min | 35¢ | 42% | 5¢ | ✅ Won | $6.34 |
| 9/29 1:31:03 PM | Gold | UP | 13.9 min | 36¢ | 50% | 12¢ | ✅ Won | $6.23 |
| 9/29 1:19:47 PM | Silver | DOWN | 10.2 min | 33¢ | 44% | 9¢ | ❌ Lost | -$3.46 |
| 9/29 1:16:19 PM | Gold | DOWN | 13.7 min | 46¢ | 54% | 6¢ | ❌ Lost | -$4.78 |
