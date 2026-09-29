# Gold & Silver Fair-Value Bot

*Updated Tue Sep 29, 2:02 PM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

🔴 **Losing.** Not beating Kalshi's prices after fees.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 114 | 113 | 40 (35%) | 39¢ | 47% | -$59.19 | -13% |
| Silver | 57 | 57 | 19 (33%) | 34¢ | 42% | -$12.77 | -6% |
| Gold | 57 | 56 | 21 (38%) | 44¢ | 52% | -$46.42 | -18% |

*Earlier half -$44.18 / later half -$15.01.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 116 | 41 (35%) | -$72.80 | -15% |
| 4¢+ ← live bot | 113 | 42 (37%) | -$3.29 | -1% |
| 6¢+ | 101 | 44 (44%) | $93.95 | +27% |
| 8¢+ | 88 | 39 (44%) | $109.20 | +39% |
| 10¢+ | 75 | 30 (40%) | $72.72 | +32% |
| 15¢+ | 45 | 18 (40%) | $64.06 | +55% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 2890 | +0.1% |
| Hyperliquid price vs Kalshi's target | 2890 | +2.5% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 2:01:04 PM | Gold | UP | 13.9 min | 43¢ | 57% | 12¢ | Open | — |
| 9/29 1:49:06 PM | Silver | UP | 10.9 min | 34¢ | 41% | 5¢ | ✅ Won | $6.44 |
| 9/29 1:46:02 PM | Gold | UP | 13.9 min | 30¢ | 50% | 18¢ | ✅ Won | $6.85 |
| 9/29 1:33:34 PM | Silver | UP | 11.4 min | 35¢ | 42% | 5¢ | ✅ Won | $6.34 |
| 9/29 1:31:03 PM | Gold | UP | 13.9 min | 36¢ | 50% | 12¢ | ✅ Won | $6.23 |
| 9/29 1:19:47 PM | Silver | DOWN | 10.2 min | 33¢ | 44% | 9¢ | ❌ Lost | -$3.46 |
| 9/29 1:16:19 PM | Gold | DOWN | 13.7 min | 46¢ | 54% | 6¢ | ❌ Lost | -$4.78 |
| 9/29 1:02:33 PM | Gold | UP | 12.4 min | 41¢ | 48% | 5¢ | ❌ Lost | -$4.27 |
| 9/29 1:02:03 PM | Silver | UP | 12.9 min | 41¢ | 47% | 4¢ | ❌ Lost | -$4.27 |
| 9/29 12:46:21 PM | Gold | UP | 13.7 min | 41¢ | 50% | 7¢ | ✅ Won | $5.73 |
| 9/29 12:46:03 PM | Silver | UP | 13.9 min | 39¢ | 50% | 9¢ | ✅ Won | $5.93 |
| 9/29 12:33:37 PM | Gold | UP | 11.4 min | 24¢ | 35% | 10¢ | ✅ Won | $7.47 |
