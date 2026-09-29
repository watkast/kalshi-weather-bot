# Gold & Silver Fair-Value Bot

*Updated Tue Sep 29, 2:22 PM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

🔴 **Losing.** Not beating Kalshi's prices after fees.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 117 | 115 | 40 (35%) | 39¢ | 47% | -$65.68 | -14% |
| Silver | 59 | 58 | 19 (33%) | 34¢ | 42% | -$14.78 | -7% |
| Gold | 58 | 57 | 21 (37%) | 44¢ | 52% | -$50.90 | -20% |

*Earlier half -$38.96 / later half -$26.72.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 118 | 41 (35%) | -$82.66 | -17% |
| 4¢+ ← live bot | 115 | 42 (37%) | -$13.15 | -3% |
| 6¢+ | 103 | 45 (44%) | $92.80 | +26% |
| 8¢+ | 90 | 39 (43%) | $104.76 | +37% |
| 10¢+ | 77 | 30 (39%) | $68.91 | +30% |
| 15¢+ | 46 | 18 (39%) | $63.48 | +54% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 2940 | -0.2% |
| Hyperliquid price vs Kalshi's target | 2940 | +2.2% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 2:17:22 PM | Gold | DOWN | 12.6 min | 50¢ | 56% | 5¢ | Open | — |
| 9/29 2:16:04 PM | Silver | UP | 13.9 min | 30¢ | 38% | 7¢ | Open | — |
| 9/29 2:02:20 PM | Silver | UP | 12.7 min | 19¢ | 25% | 4¢ | ❌ Lost | -$2.01 |
| 9/29 2:01:04 PM | Gold | UP | 13.9 min | 43¢ | 57% | 12¢ | ❌ Lost | -$4.48 |
| 9/29 1:49:06 PM | Silver | UP | 10.9 min | 34¢ | 41% | 5¢ | ✅ Won | $6.44 |
| 9/29 1:46:02 PM | Gold | UP | 13.9 min | 30¢ | 50% | 18¢ | ✅ Won | $6.85 |
| 9/29 1:33:34 PM | Silver | UP | 11.4 min | 35¢ | 42% | 5¢ | ✅ Won | $6.34 |
| 9/29 1:31:03 PM | Gold | UP | 13.9 min | 36¢ | 50% | 12¢ | ✅ Won | $6.23 |
| 9/29 1:19:47 PM | Silver | DOWN | 10.2 min | 33¢ | 44% | 9¢ | ❌ Lost | -$3.46 |
| 9/29 1:16:19 PM | Gold | DOWN | 13.7 min | 46¢ | 54% | 6¢ | ❌ Lost | -$4.78 |
| 9/29 1:02:33 PM | Gold | UP | 12.4 min | 41¢ | 48% | 5¢ | ❌ Lost | -$4.27 |
| 9/29 1:02:03 PM | Silver | UP | 12.9 min | 41¢ | 47% | 4¢ | ❌ Lost | -$4.27 |
